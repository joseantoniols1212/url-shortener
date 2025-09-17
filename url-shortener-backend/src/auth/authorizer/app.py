import json
import jwt
import os

from common.jwt_utils import get_claims_jwt

def handler(event, context):
    token_input = event['authorizationToken']

    if not token_input.startswith("Bearer "):
        raise Exception('Unauthorized')

    token = token_input[7:]

    try:
        claims = get_claims_jwt(token)
    except jwt.ExpiredSignatureError:
        raise Exception('Unauthorized')
    except jwt.InvalidTokenError:  # General exception of jwt decode
        raise Exception('Unauthorized')

    user_id = claims.get("sub", None)

    if not user_id:
        raise Exception('Unauthorized')
    
    #TODO: Check methodArn and roles and deny if not enough permission
    
    response = generatePolicy(user_id, [], 'Allow', event['methodArn'])

    try:
        return json.loads(response)
    except Exception as e:
        print('Exception ', str(e))
        raise Exception('Unauthorized')


def generatePolicy(id, roles, effect, resource):
    authResponse = {}
    authResponse['principalId'] = id
    if (effect and resource):
        policyDocument = {}
        policyDocument['Version'] = '2012-10-17'
        policyDocument['Statement'] = []
        statementOne = {}
        statementOne['Action'] = 'execute-api:Invoke'
        statementOne['Effect'] = effect
        statementOne['Resource'] = resource
        policyDocument['Statement'] = [statementOne]
        authResponse['policyDocument'] = policyDocument
    authResponse['context'] = {
        "id": id
    }
    authResponse_JSON = json.dumps(authResponse)
    return authResponse_JSON
