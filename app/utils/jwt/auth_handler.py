import time
from typing import Dict

import jwt
from app.config import settings
from app.schema import Token

JWT_SECRET = settings.secret
JWT_ALGORITHM = settings.algorithm


def token_response(token: str) -> Token:
    return {
        "access_token": token,
        "token_type": "Bearer"
    }

def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
