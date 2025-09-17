import jwt
import os
from datetime import datetime, timedelta, timezone

def create_jwt(user_id, roles):
    secret = os.environ["JWT_SECRET"]
    expiration_seconds = int(os.environ.get("JWT_EXP_SECONDS", "7200"))
    expiration = datetime.now(timezone.utc) + timedelta(seconds=expiration_seconds)
    return jwt.encode(
        {
            "sub": user_id,
            "roles": roles,
            "exp": int(expiration.timestamp())
        },
        secret,
        algorithm='HS256')

def get_claims_jwt(token):
    secret = os.environ["JWT_SECRET"]
    return jwt.decode(token, secret, algorithms=["HS256"], options={"require": ["exp", "sub", "roles"]})
