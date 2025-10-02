from ..abstract.models import AbstractDatabaseModel
import textwrap
from repositories.database import Database
from models.validation.user_data import UserData, UserInputLogin

class User(AbstractDatabaseModel):

    def __init__(self):
        self.database = Database()
        pass

import textwrap
from sqlite3 import IntegrityError
from typing import Any

class UserTable:

    def create_table(self) -> int:
        """
        Create the `USERS` table in the database if it does not already exist.

        The table includes:
            - id (INTEGER PRIMARY KEY AUTOINCREMENT)
            - uuid (TEXT NOT NULL UNIQUE)
            - name (TEXT NOT NULL)
            - email (TEXT NOT NULL UNIQUE)
            - password (TEXT NOT NULL)
            - auth_token (TEXT, nullable)
            - two_factory (TEXT, nullable)

        Returns:
            int: 204 if the table is created successfully.
        """
        query = textwrap.dedent("""
            CREATE TABLE IF NOT EXISTS USERS(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                uuid TEXT NOT NULL UNIQUE,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                auth_token TEXT,
                two_factory TEXT
            );
        """)

        self.database.execute_query(query)
        print('Table USERS created with success')
        return 204

    def insert(self, user_data: dict[str, Any]) -> int:
        """
        Insert a single record into the `USERS` table.

        Args:
            user_data (dict[str, Any]): User data containing:
                - uuid (str): Unique identifier for the user.
                - name (str): User's name.
                - email (str): User's email (must be unique).
                - password (str): User's password hash.

        Returns:
            int: 204 if the record is created successfully.

        Raises:
            sqlite3.IntegrityError: If `uuid` or `email` already exists in the database.
        """
        query = textwrap.dedent("""
            INSERT INTO USERS (uuid, name, email, password)
            VALUES(?, ?, ?, ?)
        """)

        values = (user_data['uuid'], user_data['name'], user_data['email'], user_data['password'])
        self.database.execute_query(query, values)

        return 204  # Created success

    def find_all(self) -> list[tuple]:
        """
        Retrieve all records from the `USERS` table.

        Returns:
            list[tuple]: A list of all users, where each user is a tuple
            containing all columns in the USERS table.
        """
        query = "SELECT * FROM USERS"
        result = self.database.execute_query_fetchall(query)
        
        return result
