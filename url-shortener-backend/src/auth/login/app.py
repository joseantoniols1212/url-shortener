import json
import boto3
import os
import jwt

def handler(event, _context):

    token = jwt.encode({'key': 'value'}, 'secret', algorithm='HS256')

    body = json.dumps({ "token": token })

    return {
        "statusCode": 200,
        "body": body
    }