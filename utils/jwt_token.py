from jwt import encode, decode
import os
from dotenv import load_dotenv, find_dotenv
from datetime import datetime, timedelta

config = load_dotenv(find_dotenv())
JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = 'HS256'


def create_jwt(uuid: str) -> str:
    """
    Create a JSON Web Token (JWT) for a given user UUID.

    The token will contain:
        - uuid (str): The user's unique identifier.
        - create_at (str): The token creation datetime (ISO format).
        - expire_at (str): The token expiration datetime (ISO format).

    The token is valid for 6 hours.

    Args:
        uuid (str): The user's unique identifier.

    Returns:
        str: The encoded JWT as a string.
    """
    create_at = datetime.today()
    expire_at = create_at + timedelta(hours=6)  # token duration

    payload = {
        'uuid': uuid,
        'create_at': str(create_at),
        'expire_at': str(expire_at)
    }
    print(payload)
    token = encode(payload, JWT_SECRET, algorithm=ALGORITHM)

    return token


def verify_jwt(token: str) -> bool:
    """
    Verify if a JWT is valid.

    Decodes the JWT using the configured secret key and algorithm.
    Checks if the `create_at` is earlier than the `expire_at`.

    Args:
        token (str): The encoded JWT string.

    Returns:
        bool:
            - True if the token is valid.
            - False if the token is expired or invalid.

    Raises:
        jwt.exceptions.InvalidTokenError: If the token signature or structure is invalid.
    """
    token = decode(token, JWT_SECRET, algorithms=ALGORITHM)

    expire_at = datetime.fromisoformat(token['expire_at'])
    if datetime.today() > expire_at:
        return False
    else:
        return True
