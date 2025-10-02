from jwt import encode, types
import os
from dotenv  import load_dotenv, find_dotenv
from datetime import datetime, timedelta

config = load_dotenv(find_dotenv())
JWT_SECRET = os.getenv("JWT_SECRET")

def create_jwt( uuid: str):

    create_at = datetime.today()
    expire_at = create_at + timedelta(hours = 6) #token duration

    payload = {
        'uuid': uuid,
        'create_at': str(create_at),
        'expire_at': str(expire_at)
    }
    print(payload)
    token = encode(payload, JWT_SECRET, algorithm='HS256')

    return token

