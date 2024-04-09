from motor.motor_asyncio import AsyncIOMotorClient
from config import settings


def connect_to_database():
    try:
        client = AsyncIOMotorClient(settings.DB_URL)
        database = client[settings.DB_NAME]
        db_collection = database["students"]
        return db_collection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise


db_collection = connect_to_database()
