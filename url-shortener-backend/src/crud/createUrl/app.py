import json
import boto3
import os
import hashlib
import base64

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])
hash_object = hashlib.sha256()


def create_short_code(original_url):
    hash_object.update(original_url.encode("utf-8"))
    h = hash_object.hexdigest()[:10]
    return base64.urlsafe_b64encode(h.encode("utf-8")).decode("utf-8")[:-2]


def handler(event, _context):

    body = json.loads(event["body"])
    original_url = body["url"]

    short_code = create_short_code(original_url)

    table.put_item(Item={"shortCode": short_code, "originalUrl": original_url})

    return {
        "statusCode": 200,
        "body": json.dumps(
            {"url": original_url, "shortenedUrl": f"https://short.url/{short_code}"}
        ),
    }