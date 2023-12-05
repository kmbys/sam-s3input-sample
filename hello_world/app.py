import json

def lambda_handler(event, context):
    print('event: ' + json.dumps(event))
    return ""
