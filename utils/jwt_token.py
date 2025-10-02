from jwt import encode, decode
import os
from dotenv  import load_dotenv, find_dotenv
from datetime import datetime, timedelta

config = load_dotenv(find_dotenv())
JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = 'HS256'

def create_jwt( uuid: str):

    create_at = datetime.today()
    expire_at = create_at + timedelta(hours = 6) #token duration

    payload = {
        'uuid': uuid,
        'create_at': str(create_at),
        'expire_at': str(expire_at)
    }
    print(payload)
    token = encode(payload, JWT_SECRET, algorithm= ALGORITHM)

    return token


def verify_jwt(token: str):
    token = decode(token, JWT_SECRET, algorithms= ALGORITHM)

    if token['create_at'] > token['expire_at']:
        return False
    else:
        return True
