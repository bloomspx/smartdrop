# AWS IOT Core Configurations
ENDPOINT = "a3f2k66wa7dxq0-ats.iot.ap-southeast-1.amazonaws.com"
CLIENT_ID = "Raspberry-Pi"
PATH_TO_CERTIFICATE = "certificates/f602ee93434ed4a581339e1cee4ae277c0834ef4e4dd25a03a2c3069d71675b6-certificate.pem.crt"
PATH_TO_PRIVATE_KEY = "certificates/f602ee93434ed4a581339e1cee4ae277c0834ef4e4dd25a03a2c3069d71675b6-private.pem.key"
PATH_TO_AMAZON_ROOT_CA_1 = "certificates/AmazonRootCA1.pem"

# AWS MQTT Topics
AWS_VALIDATE_TOPIC = "cciot/validate"
AWS_VALIDATED_TOPIC = "cciot/validated"
ESP32_TAKE_PHOTO_TOPIC = "cciot/take-photo"
ESP32_PHOTO_UPLOADED_TOPIC = "cciot/photo-uploaded"
