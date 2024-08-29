# crud.py
from models import UserModel, UpdateUserModel
from database import user_collection
from bson import ObjectId

# Helper function to serialize MongoDB documents
def user_serializer(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "age": user["age"],
    }

# Retrieve all users
async def retrieve_users():
    users = []
    async for user in user_collection.find():
        users.append(user_serializer(user))
    return users

# Add a new user
async def add_user(user_data: dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_serializer(new_user)

# Retrieve a user by ID
async def retrieve_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_serializer(user)

# Update a user by ID
async def update_user(id: str, data: dict):
    if len(data) < 1:
        return False
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user:
            return True
    return False

# Delete a user by ID
async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True
