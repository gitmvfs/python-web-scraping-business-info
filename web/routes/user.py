from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from models.tables.user import User
from models.validation import user_data as UserValidation
from utils.jwt_token import create_jwt

router = APIRouter(prefix='/user',tags=["user"])

user_table = User()


@router.post("/login", status_code = 200)
def login(email: str = Form(..., description= 'User email'), 
          password: str = Form(..., description= 'User password')):
    
    """
    Authenticate a user and return a JWT token if credentials are valid.

    This endpoint:
        - Verifies if the provided email exists in the database.
        - Checks if the password matches the stored hash.
        - Generates a JWT token valid for 6 hours.

    Args:
        email (str): The email of the user (from form data).
        password (str): The password of the user (from form data).

    Returns:
        JSONResponse:
            - 200: Successful login with a JWT token.
            - 401: Invalid email or password.
            - 500: Internal server error.
    """
    try:
        user_input = {'email': email, 'password': password}
        user_database = user_table.find_by_email(email)

        user_database = UserValidation.user_data_parse_dict(user_database) 
        login_result = user_table.login(user_input, user_database)

        if user_database is None or login_result is False:
            return JSONResponse(
                {'message': 'Email or Password Invalid', 'status_code': 401},
                status_code=401
            )

        token = create_jwt(user_database['uuid'])
        return JSONResponse(
            {'message': 'login success', 'token': token, 'status_code': 200},
            status_code=200
        )

    except Exception:
        return JSONResponse(
            {'message': 'Internal Server Error, contact an admin or check console log'},
            status_code=500
        )