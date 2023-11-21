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

# Callback when the subscribed topic receives a message
def on_message_received(topic, payload, dup, qos, retain, **kwargs):
    print("Received message from topic '{}': {}".format(topic, payload))

def main():
    # Create a MQTT connection 
    mqtt_connection = connectToIOTCore()

    TOPIC = ESP32_TAKE_PHOTO_TOPIC
    PAYLOAD = {"deviceId" : "Test", "passCode": "123456"}

    # Subscribe to the topic
    subscribeToIOTCore(mqtt_connection, ESP32_TAKE_PHOTO_TOPIC, on_message_received)

    # Publish to the topic
    publishToIOTCore(mqtt_connection, ESP32_TAKE_PHOTO_TOPIC, PAYLOAD)

    # Disconnect
    disconnectFromIOTCore(mqtt_connection)

main()