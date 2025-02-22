import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': jsin.dumps("Hello from our CICD github actions workflow using VScode")

    }

