from hashlib import blake2b
from hmac import compare_digest
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
HASH_SECRET = os.getenv("HASH_SECRET", "").encode("utf-8")
AUTH_SIZE = 16

def generate_hash(word: str) -> bytes:
    """
    Generate a secure BLAKE2b hash for a given word using a secret key.

    This function uses a predefined secret (from environment variables)
    to generate an authenticated hash for the provided input string.
    It is suitable for password storage or token generation.

    Args:
        word (str): The string to be hashed.

    Returns:
        bytes: The resulting hexadecimal hash encoded in UTF-8.

    Raises:
        ValueError: If the secret key is not defined in the environment.
    """
    if not HASH_SECRET:
        raise ValueError("HASH_SECRET is not defined in environment variables.")

    h = blake2b(digest_size=AUTH_SIZE, key=HASH_SECRET)
    h.update(word.encode("utf-8"))
    return h.hexdigest().encode("utf-8")


def check_hash(given_hash: bytes, word: str) -> bool:
    """
    Compare a given hash with the generated hash of a provided word.

    Uses constant-time comparison to prevent timing attacks.

    Args:
        given_hash (bytes): The previously generated hash to be validated.
        word (str): The original string to compare against the stored hash.

    Returns:
        bool:
            - True if the hash matches.
            - False otherwise.
    """
    expected_hash = generate_hash(word)
    return compare_digest(expected_hash, given_hash)
