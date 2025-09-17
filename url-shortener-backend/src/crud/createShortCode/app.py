import json
import boto3
import os
import hashlib
import base64

dynamodb = boto3.resource("dynamodb")
url_table = dynamodb.Table(os.environ["URL_TABLE_NAME"])
user_table = dynamodb.Table(os.environ["USER_TABLE_NAME"])

hash_object = hashlib.sha256()


def create_short_code(original_url):
    hash_object.update(original_url.encode("utf-8"))
    h = hash_object.hexdigest()[:10]
    return base64.urlsafe_b64encode(h.encode("utf-8")).decode("utf-8")[:-2]


def handler(event, context):

    body = json.loads(event["body"])
    original_url = body["url"]

    short_code = create_short_code(original_url)

    url_entry = {"shortCode": short_code, "originalUrl": original_url}

    url_table.put_item(Item=url_entry)

    auth_context = event["requestContext"]["authorizer"]

    user_id = auth_context.get("id", None)

    # This should never happen
    if not user_id:
        return {
            "statusCode": 403,
            "error": "Unauthorized"
        }

    user_table.update_item(
        Key={"id": user_id },
        UpdateExpression= "SET urls.#shortcode = :originalUrl",
        ExpressionAttributeNames={
            "#shortcode": short_code
        },
        ExpressionAttributeValues={
            ":originalUrl": original_url
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps(
            {"url": original_url, "shortCode": short_code }
        ),
    }