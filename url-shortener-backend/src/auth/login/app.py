import json
import boto3
from boto3.dynamodb.conditions import Key
import os
import jwt
import hashlib
import bcrypt

from common.jwt_utils import create_jwt

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["USER_TABLE_NAME"])
hash_object = hashlib.sha256()

JWT_SECRET = os.environ["JWT_SECRET"]

def response(status, body_dict):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps(body_dict)
    }


def handler(event, _context):

    request_body = event['body']

    try:
        parsed_body = json.loads(request_body)
        email = parsed_body['email']
        password = parsed_body['password']
    
    except Exception as e:
        return response(400, { "error": str(e) })
    
    #TODO: Check user is registered and password is correct

    # Find user by email
    query = table.query(
        IndexName="EmailIndex",
        KeyConditionExpression=Key("email").eq(email)
    )

    items = query.get("Items", [])
    user = items[0] if items else None

    if not user:
        raise Exception("Bad credentials")
    
    # Check password

    passwordBytes = password.encode('utf-8')
    passwordHash = user.get("passwordHash").encode('utf-8')
    isPasswordValid = bcrypt.checkpw(passwordBytes, passwordHash)

    if not isPasswordValid:
        raise Exception("Bad credentials")

    #TODO: extract roles of user
    roles = []

    user_id = user.get("id")

    token = create_jwt(user_id, roles)

    body = json.dumps({ 
        "token": token
    })

    return {
        "statusCode": 200,
        "body": body
    }