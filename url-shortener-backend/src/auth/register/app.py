import json
from json import JSONDecodeError
import boto3
import os
import bcrypt
from uuid import uuid4

from common.jwt_utils import create_jwt


dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["USER_TABLE_NAME"])

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

    request_body = event.get('body')

    try:
        parsed_body = json.loads(request_body)
        email = parsed_body['email']
        password = parsed_body['password']
    
    except Exception as e:
        return response(400, { "error": str(e) })

    #TODO: Check password satisfies requirements (min length, special symbols...)

    #TODO: Check if user is already registered
    # Write new user entry

    ## Hash password
    salt = bcrypt.gensalt()

    passwordBytes = password.encode('utf-8')
    passwordHash = bcrypt.hashpw(passwordBytes, salt)

    user_id = str(uuid4())

    user = {
        "id": user_id,
        "email": email,
        "passwordHash": passwordHash.decode('utf-8')
    }

    ## Write in dynamoDB
    table.put_item(Item=user)

    roles = []
    token = create_jwt(user_id, roles)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "token": token
        })
    }