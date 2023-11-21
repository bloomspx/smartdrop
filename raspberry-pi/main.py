# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0.

# Python Imports
from awscrt import mqtt, http
from awsiot import mqtt_connection_builder
import sys
import threading
import time
import json

# Local Imports
from config import *
from pubsub import *

"""
RPI send device ID and passcode to AWS IOT Core for Authentication (Sean)
"""
def validate(deviceId, passcode, imageURL=None):
    # Create a MQTT connection 
    mqtt_connection = connectToIOTCore()
    TOPIC = AWS_VALIDATE_TOPIC
    PAYLOAD = {"deviceId" : deviceId, "passcode": passcode}
    # Publish to the topic
    publishToIOTCore(mqtt_connection, TOPIC, PAYLOAD)
    # Disconnect
    disconnectFromIOTCore(mqtt_connection)

"""
RPI send device ID and passcode to ESP32 (Sean)
"""
def takePhoto(deviceId, passcode):
    # Create a MQTT connection 
    mqtt_connection = connectToIOTCore()
    TOPIC = ESP32_TAKE_PHOTO_TOPIC
    PAYLOAD = {"deviceId" : deviceId, "passcode": passcode}
    # Publish to the topic
    publishToIOTCore(mqtt_connection, TOPIC, PAYLOAD)
    # Disconnect
    disconnectFromIOTCore(mqtt_connection)

"""
ESP32 send device ID, passcode and imageURL to AWS IOT Core to edit order in dynamoDB (Ryan)
"""
def uploadPhoto(deviceId, passcode, imageURL):
    # Create a MQTT connection 
    mqtt_connection = connectToIOTCore()
    TOPIC = ESP32_PUBLISH_PHOTO_TOPIC
    PAYLOAD = {"deviceId" : deviceId, "passcode": passcode, "imageURL": imageURL}
    # Publish to the topic
    publishToIOTCore(mqtt_connection, TOPIC, PAYLOAD)
    # Disconnect
    disconnectFromIOTCore(mqtt_connection)
    
"""
AWS inform RPI on the status of the validation (Sean)
"""
def subscribeToValidatedTopic():
    # Callback when the subscribed topic receives a message
    def on_message_received(topic, payload, dup, qos, retain, **kwargs):
        print("Received message from topic '{}': {}".format(topic, payload))

    # Create a MQTT connection 
    mqtt_connection = connectToIOTCore()
    TOPIC = AWS_VALIDATED_TOPIC
    # Subscribe to the topic
    subscribeToIOTCore(mqtt_connection, TOPIC, on_message_received)
    # Disconnect
    disconnectFromIOTCore(mqtt_connection)

"""
AWS inform ESP32 that the photo has been uploaded (Ryan)
"""
def subscribeToPhotoPublishedTopic():
    # Callback when the subscribed topic receives a message
    def on_message_received(topic, payload, dup, qos, retain, **kwargs):
        print("Received message from topic '{}': {}".format(topic, payload))

    # Create a MQTT connection 
    mqtt_connection = connectToIOTCore()
    TOPIC = ESP32_PHOTO_PUBLISHED_TOPIC
    # Subscribe to the topic
    subscribeToIOTCore(mqtt_connection, TOPIC, on_message_received)
    # Disconnect
    disconnectFromIOTCore(mqtt_connection)


"""
ESP32 inform RPI that the photo has been uploaded (Sean)
"""
def subscribeToPhotoUploadedTopic():
    # Callback when the subscribed topic receives a message
    def on_message_received(topic, payload, dup, qos, retain, **kwargs):
        print("Received message from topic '{}': {}".format(topic, payload))

    # Create a MQTT connection 
    mqtt_connection = connectToIOTCore()
    TOPIC = ESP32_PHOTO_UPLOADED_TOPIC
    # Subscribe to the topic
    subscribeToIOTCore(mqtt_connection, TOPIC, on_message_received)
    # Disconnect
    disconnectFromIOTCore(mqtt_connection)

deviceID = "Raspberry-Pi"
passcode = "123456"
imageURL = "test"

# validate(deviceID, passcode)
takePhoto(deviceID, passcode)
# uploadPhoto(deviceID, passcode, imageURL)
# subscribeToValidatedTopic()
# subscribeToPhotoUploadedTopic()
# subscribeToPhotoPublishedTopic()