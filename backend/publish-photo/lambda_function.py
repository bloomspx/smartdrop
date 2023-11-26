import json
import boto3

def lambda_handler(event, context):
    print("event:", event)

    # change parameters accordingly

    mqtt = boto3.client('iot-data', region_name='ap-southeast-1')
    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')

    table = dynamodb.Table('Order')
    response = table.update_item(
        Key={
            'deviceID': event['deviceID'],
            'passcode': event['passcode']
        },
        UpdateExpression='SET imageURL = :url',
        ExpressionAttributeValues={
            ':url': event['imageURL']
        },
        ReturnValues='UPDATED_NEW'
    )
    
    json_string = json.dumps(event)

    response = mqtt.publish(
            topic='cciot/photo-published',
            qos=0,
            payload=json_string
        )
    return "PUB to cciot/photo-published"