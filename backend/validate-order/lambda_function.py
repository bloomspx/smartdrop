import json
import boto3

def lambda_handler(event, context):
    print("event:", event)
    isValidated = False

    # change parameters accordingly

    mqtt = boto3.client('iot-data', region_name='ap-southeast-1')
    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')

    table = dynamodb.Table('Order')
    response = table.get_item(
        Key={
            'deviceID': event['deviceID'],
            'passcode': event['passcode']
        }
    )

    if 'Item' in response:
        isValidated = True

    results = {
        'deviceID': event['deviceID'],
        'passcode': event['passcode'],
        'isValidated': isValidated
    }
    
    json_string = json.dumps(results)

    response = mqtt.publish(
            topic='cciot/validated',
            qos=0,
            payload=json_string
        )
    return "PUB to cciot/validated"