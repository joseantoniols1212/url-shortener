import jwt
import os

def create_jwt(user_id, roles):
    secret = os.environ["JWT_SECRET"]
    return jwt.encode({
            "sub": user_id, "user": {"id": user_id, "roles": roles}
            },
            secret,
            algorithm='HS256'
        )