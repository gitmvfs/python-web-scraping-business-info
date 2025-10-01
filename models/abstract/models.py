from abc import ABC, abstractmethod
from sqlite3 import Cursor
from typing import Any

class AbstractDatabaseModel(ABC):
    """Base abstract class for database models with common CRUD operations."""

    @abstractmethod
    def create_table(self) -> str:
        """
        Create table in database
        
        Returns:
            str: "Create table success"
                        
        """
        pass

    def insert_single(self, cursor: Cursor, data: dict[str, Any]) -> dict[str, Any]:
        """
        Insert a single record and return the object created in the database.
        
        Args:
            cursor (Cursor): The database cursor.
            data (dict[str, Any]): Data for the new record.
        
        Returns:
            dict[str, Any]: The object data created.
        """
        pass

    def update_data(self, cursor: Cursor, data: dict[str, Any], id: int) -> dict[str, Any]:
        """
        Update a record by its ID and return both the old and new data.
        
        Args:
            cursor (Cursor): The database cursor.
            data (dict[str, Any]): The updated data for the record.
            id (int): The ID of the record to update.
        
        Returns:
            dict[str, Any]: A dict containing the old and updated object data.
        """
        pass

    def find_by_id(self, cursor: Cursor, id: int) -> dict[str, Any] | None:
        """
        Find a unique record by its ID.
        
        Args:
            cursor (Cursor): The database cursor.
            id (int): The ID of the record.
        
        Returns:
            dict[str, Any] | None: The record found, or None if not found.
        """
        pass

    def find_all(self, cursor: Cursor) -> list[dict[str, Any]]:
        """
        Return all records from the table.
        
        Args:
            cursor (Cursor): The database cursor.
        
        Returns:
            list[dict[str, Any]]: A list of all records.
        """
        pass

    def delete_by_id(self, cursor: Cursor, id: int) -> dict[str, Any] | None:
        """
        Delete a unique record by its ID.
        
        Args:
            cursor (Cursor): The database cursor.
            id (int): The ID of the record to delete.
        
        Returns:
            dict[str, Any] | None: The deleted record, or None if not found.
        """
        pass
    