# backend/app/database.py
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.client = None
        self.db = None

    async def connect_db(self):
        self.client = AsyncIOMotorClient("mongodb://mongo:27017")
        return self.client
        """
        Connect to the MongoDB database.

        This method retrieves the MongoDB URI from environment variables,
        establishes a connection to the MongoDB server, and sets the database
        instance to 'contentai'.
        Returns:
            The database instance if the connection is successful.
        """

    async def disconnect_db(self):
        """
        Disconnects from the MongoDB database and resets the client and db attributes.

        This method closes the connection to the MongoDB server and sets the client and
        database attributes to None.
        """
        try:
            if self.client:
                self.client.close()
            self.client = None
            self.db = None
        except Exception as e:
            logging.error(f"MongoDB disconnection error: {e}")
            raise ConnectionError("Failed to disconnect from MongoDB")
        try:
            await self.client.close()
        except Exception as e:
            logging.error(f"Error closing MongoDB connection: {e}")
            raise ConnectionError("Failed to disconnect from MongoDB")
        self.client = None
        self.db = None
        logging.info("MongoDB connection closed")