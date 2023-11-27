# AWS IOT Core Configurations
ENDPOINT = "a3f2k66wa7dxq0-ats.iot.ap-southeast-1.amazonaws.com"
CLIENT_ID = "Raspberry-Pi"
PATH_TO_CERTIFICATE = "certificates/f602ee93434ed4a581339e1cee4ae277c0834ef4e4dd25a03a2c3069d71675b6-certificate.pem.crt"
PATH_TO_PRIVATE_KEY = "certificates/f602ee93434ed4a581339e1cee4ae277c0834ef4e4dd25a03a2c3069d71675b6-private.pem.key"
PATH_TO_AMAZON_ROOT_CA_1 = "certificates/AmazonRootCA1.pem"

# AWS MQTT Topics
AWS_VALIDATE_TOPIC = "cciot/validate" #rpi pub, cloud iot core sub  - deviceID, passcode
AWS_VALIDATED_TOPIC = "cciot/validated" #cloud iot core pub, rpi sub - deviceID, passcode, isValidated
ESP32_TAKE_PHOTO_TOPIC = "cciot/take-photo" #rpi pub, esp32 sub - deviceID, passcode
ESP32_PHOTO_UPLOADED_TOPIC = "cciot/photo-uploaded" #esp32 pub, rpi sub
ESP32_PUBLISH_PHOTO_TOPIC = "cciot/publish-photo" #esp32 pub, cloud iot core sub - imageURL, deviceID, passcode
ESP32_PHOTO_PUBLISHED_TOPIC = "cciot/photo-published" #cloud iot core pub, esp32 sub