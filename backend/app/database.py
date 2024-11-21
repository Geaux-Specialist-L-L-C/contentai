# backend/app/database.py
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    client = None
    
    @classmethod
    async def connect_db(cls):
        try:
            mongodb_uri = os.getenv('MONGODB_URI')
            cls.client = AsyncIOMotorClient(mongodb_uri)
            return cls.client.get_default_database()
        except Exception as e:
            print(f"MongoDB connection error: {e}")
            return None

    @classmethod
    async def disconnect_db(cls):
        if cls.client:
            cls.client.close()
            cls.client = None