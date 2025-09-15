import json
import boto3
import os

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])


def handler(event, _context):

    short_code = event["pathParameters"]["shortCode"]

    response = table.get_item(Key={"shortCode": short_code})

    if "Item" not in response:
        return {"statusCode": 404, "body": json.dumps({"error": "URL not found"})}

    original_url = response["Item"]["originalUrl"]

    return {"statusCode": 302, "headers": {"Location": original_url}}
