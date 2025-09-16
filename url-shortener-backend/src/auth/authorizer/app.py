import json
import jwt
import os

JWT_SECRET = os.environ["JWT_SECRET"]

def handler(event, context):
    token_input = event['authorizationToken']

    if not token_input.startswith("Bearer "):
        raise Exception('Unauthorized')

    token = token_input[7:]

    decoded_token = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])

    user = decoded_token.get("user", {})
    user_id = user.get("id", "")

    if not user_id or user_id == "":
        raise Exception('Unauthorized')
    
    #TODO: Check methodArn and roles and deny if not enough permission
    
    response = generatePolicy(user_id, [], 'Allow', event['methodArn'])

    try:
        print("a")
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