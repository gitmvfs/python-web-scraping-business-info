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
