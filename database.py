# database.py
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# MongoDB connection URL
MONGO_DETAILS = os.getenv("MONGO_DETAILS")

# Create a client and connect to the database
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.my_database  # Replace with your database name

# Reference to a specific collection
user_collection = database.get_collection("users")
