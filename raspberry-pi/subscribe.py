# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
# https://repost.aws/knowledge-center/iot-core-publish-mqtt-messages-python

from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
import time as t
import json
from config import *

def subscribeToIOTCore(topic, callback):
    print("Subscribing to topic: " + topic)
    subscribe_future, packet_id = mqtt_connection.subscribe(
        topic=topic,
        qos=mqtt.QoS.AT_LEAST_ONCE,
        callback=callback
    )
    subscribe_result = subscribe_future.result()
    print("Subscribed with {}".format(str(subscribe_result['qos'])))