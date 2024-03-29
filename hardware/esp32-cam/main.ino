#include "secrets.h"
#include "esp_camera.h"
#include "esp_http_client.h"
#include <ArduinoJson.h>
#include <PubSubClient.h>
#include "WiFi.h"
#include <WiFiClientSecure.h>
#include "soc/soc.h"           // Disable brownout problems
#include "soc/rtc_cntl_reg.h"  // Disable brownout problems
#include "driver/rtc_io.h"
#include "time.h"
#include <string>
#include "Base64.h"
#include "mbedtls/base64.h"

// MQTT Topics 
#define ESP32_TAKE_PHOTO_TOPIC "cciot/take-photo" //rpi pub, esp32 sub - deviceID, passcode
#define ESP32_PHOTO_UPLOADED_TOPIC   "cciot/photo-uploaded" //esp32 pub, rpi sub
#define ESP32_PUBLISH_PHOTO_TOPIC "cciot/publish-photo" //esp32 pub, cloud iot core sub - imageURL, deviceID, passcode
#define ESP32_PHOTO_PUBLISHED_TOPIC "cciot/photo-published" //cloud iot core pub, esp32 sub

// ESP32 Cam Configuration
#define CAM_PIN_PWDN 32
#define CAM_PIN_RESET -1 //software reset will be performed
#define CAM_PIN_XCLK 0
#define CAM_PIN_SIOD 26
#define CAM_PIN_SIOC 27
#define CAM_PIN_D7 35
#define CAM_PIN_D6 34
#define CAM_PIN_D5 39
#define CAM_PIN_D4 36
#define CAM_PIN_D3 21
#define CAM_PIN_D2 19
#define CAM_PIN_D1 18
#define CAM_PIN_D0 5
#define CAM_PIN_VSYNC 25
#define CAM_PIN_HREF 23
#define CAM_PIN_PCLK 22
#define FLASH_GPIO_NUM 4
 
// Global Variables
WiFiClientSecure wifiClient = WiFiClientSecure();
PubSubClient mqttClient(wifiClient);

// Variables
bool internetConnected = false;

//Initialize camera
void initCamera(){
  // OV5640 camera module
  camera_config_t config;

  // Assign pins
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = CAM_PIN_D0;
  config.pin_d1 = CAM_PIN_D1;
  config.pin_d2 = CAM_PIN_D2;
  config.pin_d3 = CAM_PIN_D3;
  config.pin_d4 = CAM_PIN_D4;
  config.pin_d5 = CAM_PIN_D5;
  config.pin_d6 = CAM_PIN_D6;
  config.pin_d7 = CAM_PIN_D7;
  config.pin_xclk = CAM_PIN_XCLK;
  config.pin_pclk = CAM_PIN_PCLK;
  config.pin_vsync = CAM_PIN_VSYNC;
  config.pin_href = CAM_PIN_HREF;
  config.pin_sscb_sda = CAM_PIN_SIOD;
  config.pin_sscb_scl = CAM_PIN_SIOC;
  config.pin_pwdn = CAM_PIN_PWDN;
  config.pin_reset = CAM_PIN_RESET;
  config.xclk_freq_hz = 5000000;
  config.pixel_format = PIXFORMAT_JPEG;
  config.grab_mode = CAMERA_GRAB_WHEN_EMPTY;
  
  // Set JPEG quality
  if(psramFound()){
    Serial.printf("PSRAM found");
    config.frame_size = FRAMESIZE_UXGA;
    config.jpeg_quality = 10;
    config.fb_count = 2;
  } else {
    Serial.printf("PSRAM not found");
    config.frame_size = FRAMESIZE_SVGA;
    config.jpeg_quality = 12;
    config.fb_count = 1;
  }
  
  // Init Camera
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    ESP.restart();
  } 
}

// Initialize Wifi connection
bool initWifi() {
    WiFi.mode(WIFI_STA);
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
    Serial.println("Connecting to Wi-Fi");
    while (WiFi.status() != WL_CONNECTED)
    {
      delay(500);
      Serial.print(".");
    }
    return true;
}

// Handle HTTP API Response
esp_err_t httpEventHandler(esp_http_client_event_t *evt)
{
  switch (evt->event_id) {
    case HTTP_EVENT_ERROR:
      Serial.println("HTTP_EVENT_ERROR");
      break;
    case HTTP_EVENT_ON_CONNECTED:
      Serial.println("HTTP_EVENT_ON_CONNECTED");
      break;
    case HTTP_EVENT_HEADER_SENT:
      Serial.println("HTTP_EVENT_HEADER_SENT");
      break;
    case HTTP_EVENT_ON_HEADER:
      Serial.println();
      Serial.printf("HTTP_EVENT_ON_HEADER");
      break;
    case HTTP_EVENT_ON_DATA:
      Serial.println();
      Serial.printf("HTTP_EVENT_ON_DATA");
      break;
    case HTTP_EVENT_ON_FINISH:
      Serial.println("");
      Serial.println("HTTP_EVENT_ON_FINISH");
      break;
    case HTTP_EVENT_DISCONNECTED:
      Serial.println("HTTP_EVENT_DISCONNECTED");
      break;
  }
  return ESP_OK;
}

// Take and upload photo
static esp_err_t takeAndUploadPhoto(const char* deviceID, const char* passcode) {
  camera_fb_t * fb = NULL;
  esp_err_t res = ESP_OK;

  // Skip first 3 frames (increase/decrease number as needed)
  for (int i = 0; i < 4; i++) {
    fb = esp_camera_fb_get();
    esp_camera_fb_return(fb);
    fb = NULL;
  }

  // Turn on the flash
  digitalWrite(FLASH_GPIO_NUM, HIGH);
  delay(500);

  // Take photo and save to buffer fb
  fb = esp_camera_fb_get();
  if (!fb) {
    Serial.println("Camera capture failed");
    return ESP_FAIL;
  }

  // Turn off the flash
  digitalWrite(FLASH_GPIO_NUM, LOW);
  delay(500);

  // Image Data Preparation 
  Serial.println("Uploading Photo");
  int image_buf_size = 4000 * 1000;                                                  
  uint8_t *image = (uint8_t *)ps_calloc(image_buf_size, sizeof(char));
  size_t length=fb->len;
  size_t olen;
  Serial.print("length is");
  Serial.println(length);
  int err1 = mbedtls_base64_encode(image, image_buf_size, &olen, fb->buf, length);
  String deviceIDString = deviceID;
  String passcodeString = passcode;

  // http client and config client initialization
  esp_http_client_handle_t http_client;
  esp_http_client_config_t config_client = {0};

  // API Call Data Preparation
  Serial.println(deviceIDString);
  Serial.println(passcodeString);
  String putUrl2 = "https://zoo7ealxvd.execute-api.ap-southeast-1.amazonaws.com/dev/cciot-smart-delivery/" + deviceIDString + "_" + passcodeString + ".jpg";
  Serial.println(putUrl2);
  char putUrl3[putUrl2.length() + 1];
  putUrl2.toCharArray(putUrl3, sizeof(putUrl3));
  Serial.println(putUrl3);

  // API Call Configuration
  config_client.url = putUrl3;
  config_client.cert_pem = AWS_CERT_CA;
  config_client.event_handler = httpEventHandler;
  config_client.method = HTTP_METHOD_PUT;
  
  // Initialize HTTP Client
  http_client = esp_http_client_init(&config_client);
  esp_http_client_set_post_field(http_client, (const char *)fb->buf, fb->len);
  esp_http_client_set_header(http_client, "Content-Type", "image/jpg");

  // Perform API Call
  esp_err_t err = esp_http_client_perform(http_client);
  if (err == ESP_OK) {
    Serial.print("esp_http_client_get_status_code: ");
    Serial.println(esp_http_client_get_status_code(http_client));
  }

  // Clean up HTTP Client
  esp_http_client_cleanup(http_client);
  esp_camera_fb_return(fb);

  // Publish to MQTT topic
  publishToAWS(deviceID, passcode);
}

// Subscribe to MQTT topics 
void connectAWS() {
  // Configure WiFiClientSecure to use the AWS IoT device credentials
  wifiClient.setCACert(AWS_CERT_CA);
  wifiClient.setCertificate(AWS_CERT_CRT);
  wifiClient.setPrivateKey(AWS_CERT_PRIVATE);

  // Connect to the MQTT broker on the AWS endpoint we defined earlier
  mqttClient.setServer(AWS_IOT_ENDPOINT, 8883);

  // Create a message handler
  mqttClient.setCallback(messageHandler);
  Serial.println("Connecting to AWS IOT");
  while (!mqttClient.connect(THINGNAME))
  {
    Serial.print(".");
    delay(100);
  }
  if (!mqttClient.connected())
  {
    Serial.println("AWS IoT Timeout!");
    return;
  }

  // Subscribe to topics
  mqttClient.subscribe(ESP32_TAKE_PHOTO_TOPIC);
  mqttClient.subscribe(ESP32_PHOTO_PUBLISHED_TOPIC);
  Serial.println("AWS IoT Connected!");
}

// Publish to AWS IoT 
void publishToAWS(const char* deviceID, const char* passcode) {
  StaticJsonDocument<200> doc;
  doc["deviceID"] = deviceID;
  doc["passcode"] = passcode;
  char jsonBuffer[512];
  serializeJson(doc, jsonBuffer); // print to mqttClient
  mqttClient.publish(ESP32_PUBLISH_PHOTO_TOPIC, jsonBuffer);
}

// Publish to RPI
void publishToRPI(const char* deviceID, const char* passcode) {
  StaticJsonDocument<200> doc;
  doc["deviceID"] = deviceID;
  doc["passcode"] = passcode;
  char jsonBuffer[512];
  serializeJson(doc, jsonBuffer); // print to mqttClient
  mqttClient.publish(ESP32_PHOTO_UPLOADED_TOPIC, jsonBuffer);
}
 
// Message handler for MQTT topics
void messageHandler(char* topic, byte* payload, unsigned int length) {
  // Take photo if message received on ESP32_TAKE_PHOTO_TOPIC
  if (strcmp(topic,ESP32_TAKE_PHOTO_TOPIC)==0) {
    // Deserialize payload from RPI
    StaticJsonDocument<200> doc;
    deserializeJson(doc, payload);
    const char* deviceID = doc["deviceID"];
    const char* passcode = doc["passcode"];
    takeAndUploadPhoto(deviceID, passcode);
    Serial.println("Photo Uploaded");
  }

  // Publish to RPI if message received on ESP32_PHOTO_PUBLISHED_TOPIC
  else if (strcmp(topic, ESP32_PHOTO_PUBLISHED_TOPIC)==0) {
    // Deserialize payload from Cloud
    StaticJsonDocument<200> doc;
    deserializeJson(doc, payload);
    const char* deviceID = doc["deviceID"];
    const char* passcode = doc["passcode"];
    // Publish to RPI
    publishToRPI(deviceID, passcode);
  }
}

// Setup function 
void setup() {
  Serial.begin(9600);
  // Turn-off the 'brownout detector'
  WRITE_PERI_REG(RTC_CNTL_BROWN_OUT_REG, 0);
  // Initialize flash GPIO
  pinMode(FLASH_GPIO_NUM, OUTPUT);
  // Connect to WiFi
  if (initWifi()) {
    internetConnected = true;
    Serial.println("Internet Connected");
  }
  // Initialize camera
  initCamera();
  // Connect to AWS and execute callback function based on MQTT subscription
  connectAWS();
}

// Loop function 
void loop()
{
  // Reconnect to AWS if disconnected
  mqttClient.loop();
  delay(5000);
}