import json
import boto3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    print("event:", event)
    
    # Specify the fixed offset for Singapore (UTC+8)
    singapore_offset = timedelta(hours=8)
    # Get the current UTC time
    utc_now = datetime.utcnow()
    singapore_timezone = timezone(singapore_offset)
    localized_time = utc_now.replace(tzinfo=timezone.utc).astimezone(singapore_timezone)

    # change parameters accordingly
    mqtt = boto3.client('iot-data', region_name='ap-southeast-1')
    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
    deviceIDString = event['deviceID']
    passcodeString = event['passcode']
    url = "https://cciot-smart-delivery.s3.ap-southeast-1.amazonaws.com/" + deviceIDString + "_" + passcodeString + ".jpg";
    table = dynamodb.Table('Order')
    
    
    try:
        response = table.update_item(
            Key={
                'deviceID': deviceIDString,
                'passcode': passcodeString
            },
            UpdateExpression='SET imageURL = :url, isDelivered = :isDelivered, deliveredDate = :deliveredDate',
            ExpressionAttributeValues={
                ':url': url,
                ':isDelivered': True,
                ':deliveredDate': localized_time.strftime('%m/%d/%Y, %I:%M:%S %p')
            },
            ReturnValues='UPDATED_NEW'
        )
    
        if 'Attributes' in response:
            published = True
        
        res = {
            'deviceID': event['deviceID'],
            'passcode': event['passcode'],
            'published': published
        }

        json_string = json.dumps(res)
    
        response = mqtt.publish(
                topic='cciot/photo-published',
                qos=0,
                payload=json_string
            )
    except Exception as e:
        print("Error updating item:", e)
    return "PUB to cciot/photo-published"