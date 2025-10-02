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

