from pydantic import BaseModel

class UserData(BaseModel):
    id: int
    uuid: str
    name: str
    email: str
    password:str
    auth_token: str
    two_factory: str

class UserInputLogin(BaseModel):
    email:str
    password:str

def user_data_parse_dict(user_data: list) -> dict[str, any]:
    """
    Parse a SQLite query result into a dictionary with user fields.

    This function is designed to convert the result of a SQLite `fetchall()` or `fetchone()` 
    operation (wrapped in a list) into a dictionary with explicit column names.

    Expected order of values from the database:
        - id (int)
        - uuid (str)
        - name (str)
        - email (str)
        - password (str)
        - auth_token (str | None)
        - two_factory (str | None)

    Args:
        user_data (list): The SQLite query result (e.g., from `fetchall()`), 
            where `user_data[0]` is a tuple representing one user row.

    Returns:
        dict[str, Any]: A dictionary mapping column names to their respective values.
            Example:
            {
                "id": 1,
                "uuid": "abcd-1234",
                "name": "Marcos",
                "email": "marcos@email.com",
                "password": "hashed_pw",
                "auth_token": None,
                "two_factory": None
            }

    Raises:
        IndexError: If `user_data` is empty or not in the expected format.
    """
    columns = ['id', 'uuid', 'name', 'email', 'password', 'auth_token', 'two_factory']
    new_user_data = dict(zip(columns, user_data[0]))
    return new_user_data

def user_validate_data(user_data: dict) -> bool:
    
    user_name = user_data['name']
    user_password = user_data['password']
    user_email = user_data['email']

    if type(user_name) != str or type(user_password) != str or type(user_email) != str:
        raise Exception('Type error')
    
    result_password = validate_password(user_password)

    return False if result_password == False else ''


def validate_password(password: str) -> bool:
    """
    Validates a password according to security rules.

    The password must meet all of the following criteria:
        - Have at least 6 characters.
        - Contain at least one uppercase letter.
        - Contain at least one lowercase letter.
        - Contain at least one numeric digit.
        - Contain at least one special character (@, !, *, #).

    Args:
        password (str): The password string to validate.

    Returns:
        bool: True if the password is valid.

    Raises:
        ValueError: If the password does not meet any of the required criteria.
    """

    list_special_char = ['@', '!', '*', '#']

    if len(password) < 6:
        raise ValueError("Password length must be six characters or more.")

    have_lower_case = any(ch.islower() for ch in password)
    have_upper_char = any(ch.isupper() for ch in password)
    have_number = any(ch.isnumeric() for ch in password)
    have_special_char = any(ch in list_special_char for ch in password)

    if not have_lower_case:
        raise ValueError("Password must contain at least one lowercase letter.")

    if not have_upper_char:
        raise ValueError("Password must contain at least one uppercase letter.")

    if not have_number:
        raise ValueError("Password must contain at least one number.")

    if not have_special_char:
        raise ValueError(f"Password must contain at least one special character: {', '.join(list_special_char)}")

    return True
