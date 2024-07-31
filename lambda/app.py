import json

import boto3

client = boto3.client('iot-data')

def lambda_handler(event, context):
    print(event)
    topic = 'coop/led/color'
    message = {'LED': 'LED_FLASHING_BLUE'}
    response = client.publish(
        topic=topic,
        qos=1,
        payload=json.dumps(message)
    )
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('MQTT message published')
    }
