# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0.

# Python Imports
from awscrt import mqtt, http
from awsiot import mqtt_connection_builder
import asyncio
import sys
import threading
import time
import json

# Local Imports
from config import *
from pubsub import *
received_payload = None

# Callback when the subscribed topic receives a message
def on_message_received(topic, payload, dup, qos, retain, **kwargs):
    global received_payload
    received_payload = payload
    print("Received message from topic '{}': {}".format(topic, payload))

def subscribe_to_validate_topic(mqtt_connection):
    SUB_TOPIC = AWS_VALIDATED_TOPIC
    subscribeToIOTCore(mqtt_connection, SUB_TOPIC, on_message_received)

def publish_to_validate_topic(mqtt_connection, payload):
    PUB_TOPIC = AWS_VALIDATE_TOPIC
    publishToIOTCore(mqtt_connection, PUB_TOPIC, payload)

def subscribe_to_take_photo_topic(mqtt_connection):
    SUB_TOPIC = ESP32_PHOTO_UPLOADED_TOPIC
    subscribeToIOTCore(mqtt_connection, SUB_TOPIC, on_message_received)

def publish_to_take_photo_topic(mqtt_connection, payload):
    PUB_TOPIC = ESP32_TAKE_PHOTO_TOPIC
    publishToIOTCore(mqtt_connection, PUB_TOPIC, payload)

def format_validate_payload(deviceID, passcode):
    return {
        "deviceID" : deviceID, 
        "passcode": passcode
    }

def format_take_photo_payload(deviceID, passcode):
    return {
        "deviceID" : deviceID, 
        "passcode": passcode
    }

# Helper function to decode byte array to JSON
def decodePayload(payload):
    return json.loads(payload.decode('utf-8'))

# Helper function to validate the payload
def validatePayload(payload):
    return payload["isValidated"]

def aws_setup():
    # Create a MQTT connection 
    mqtt_connection = connectToIOTCore()
    subscribe_to_validate_topic(mqtt_connection)
    subscribe_to_take_photo_topic(mqtt_connection)
    return mqtt_connection

async def wait_for_received_payload():
    global received_payload
    while received_payload is None:
        await asyncio.sleep(0.1)
    return received_payload
