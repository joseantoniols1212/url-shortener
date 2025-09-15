import json
import boto3
import os

def handler(event, _context):
    return {
        "statusCode": 200,
        "body": "OK"
    }