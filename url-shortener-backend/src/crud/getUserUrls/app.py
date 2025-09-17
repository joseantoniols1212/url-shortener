import json
import boto3
import os
import hashlib
import base64

dynamodb = boto3.resource("dynamodb")
user_table = dynamodb.Table(os.environ["USER_TABLE_NAME"])

hash_object = hashlib.sha256()

def handler(event, context):

    auth_context = event["requestContext"]["authorizer"]
    user_id = auth_context.get("id", None)

    # This should never happen
    if not user_id:
        return {
            "statusCode": 403,
            "error": "Unauthorized"
        }

    query_response = user_table.get_item(Key={"id": user_id })

    user = query_response["Item"]
    urls = user["urls"]

    return {
        "statusCode": 200,
        "body": json.dumps({
            "urls": urls
        }),
    }