# main.py
from fastapi import FastAPI, HTTPException, status
from models import UserModel, UpdateUserModel
from crud import (
    retrieve_users,
    add_user,
    retrieve_user,
    update_user,
    delete_user,
)

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the FastAPI MongoDB CRUD app!"}

# Create a new user
@app.post("/users", response_description="Add new user", response_model=UserModel)
async def create_user(user: UserModel):
    user = await add_user(user.dict())
    return user

# Retrieve all users
@app.get("/users", response_description="List all users", response_model=list[UserModel])
async def get_users():
    users = await retrieve_users()
    return users

# Retrieve a user by ID
@app.get("/users/{id}", response_description="Get a user by ID", response_model=UserModel)
async def get_user(id: str):
    user = await retrieve_user(id)
    if user:
        return user
    raise HTTPException(status_code=404, detail=f"User {id} not found")

# Update a user by ID
@app.put("/users/{id}", response_description="Update a user", response_model=UserModel)
async def update_user_data(id: str, req: UpdateUserModel):
    req_data = {k: v for k, v in req.dict().items() if v is not None}
    updated = await update_user(id, req_data)
    if updated:
        return await retrieve_user(id)
    raise HTTPException(status_code=404, detail=f"User {id} not found")

# Delete a user by ID
@app.delete("/users/{id}", response_description="Delete a user")
async def delete_user_data(id: str):
    deleted = await delete_user(id)
    if deleted:
        return {"message": f"User {id} deleted successfully"}
    raise HTTPException(status_code=404, detail=f"User {id} not found")
