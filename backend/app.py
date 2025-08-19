
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import motor.motor_asyncio
from uuid import UUID, uuid4
# from bson.codec_options import CodecOptions
# from bson.uuid_representation import UuidRepresentation

app = FastAPI()

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://cnu:jb1y6avC2cm6oRxg@cluster0.xiuz0db.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',uuidRepresentation='standard')

db = client.test_database

# print(db)

class User(BaseModel):
    id: UUID = Field(alias="_id", default_factory=uuid4)
    Users: str
    name : str
    email: str
    password : str
    age : int
    weight : int
    height : str
    goals :str
     
class Workouts(BaseModel):
     id: UUID = Field(alias="_id", default_factory=uuid4)
     user_id : str
     plan_name : str
     date: str
     exercises : str
     duration : str
                

 
class Nutrition(BaseModel):
     id: UUID = Field(alias="_id", default_factory=uuid4)
     user_id : str
     date: str
     meals : str
     calories : str
     macros : str
     
class Progress(BaseModel):
    id: UUID = Field(alias="_id", default_factory=uuid4)
    user_id : str
    workout_id : str
    sets : str
    reps : str
    weights : str
    notes : str
    
   
    
#  POST /auth/register - User registration
# POST /auth/login - User login
# GET /auth/user/{user_id} - Get user profile   

@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.post("/auth/register", response_model=User)
async def insert_user(user: User):
    result = await db["users"].insert_one(user.dict())
    inserted_user = await db["users"].find_one({"_id": result.inserted_id})
    return inserted_user

# @app.get("/auth/login/{email_address}/{password}", response_model=User)
# async def read_user_by_email(email_address: str,password:str):
#     user = await db["users"].find_one({"email": email_address,"password":password})
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user


@app.post("/auth/login/", response_model=User)
async def read_user_by_email(email_address: str,password:str):
    user = await db["users"].find_one({"email": email_address,"password":password})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# @app.post("/auth/user/{email_address}",response_model=User)
# async def update_user(email_address:str):
#     user = await db["users"] 

@app.put("/auth/user/{email_address}",response_model=User)
async def update_user(email_address: str, user_update: User):
    updated_result =await db["users"].update_one(
        {"email_address": email_address}, {"$set": user_update.dict(exclude_unset=True)})
    if updated_result.modified_count == 0:
        raise HTTPException(status_code=404, detail="User not found or no update needed")
    updated_user =await db["users"].find_one({"email_address": email_address})
    return updated_user



@app.post("/Workouts/addWorkout", response_model=Workouts)
async def insert_user(workouts: Workouts):
    result = await db["workouts"].insert_one(workouts.dict())
    inserted = await db["workouts"].find_one({"_id": result.inserted_id})
    return inserted


@app.get("/Workouts/",response_model=Workouts)
async def fetch_data(workouts: Workouts):
    data = await db["workouts"].find().to_list(None)
    return data

@app.put("/Workouts/update/{id}",response_model=Workouts)
async def update_user(id: str, user_update: Workouts):
    updated_result =await db["workouts"].update_one(
        {"id": id}, {"$set": user_update.dict(exclude_unset=True)})
    if updated_result.modified_count == 0:
        raise HTTPException(status_code=404, detail="User not found or no update needed")
    updated_user =await db["workouts"].find_one({"id": id})
    return updated_user


@app.delete("/Workouts/delete/{id}", response_model=dict)
async def delete_by_email(id: str):
    delete_result = await db["workouts"].delete_one({"id": id})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "deleted successfully"}







@app.post("/Nutrition/addNutrition", response_model=Nutrition)
async def insert_user(nutrition: Nutrition):
    result = await db["nutrition"].insert_one(nutrition.dict())
    inserted = await db["nutrition"].find_one({"_id": result.inserted_id})
    return inserted



@app.get("/Nutrition/",response_model=Nutrition)
async def fetch_data(nutrition: Nutrition):
    data = await db["nutrition"].find().to_list(None)
    return data

@app.put("/Nutrition/update/{id}",response_model=Nutrition)
async def update_user(id: str, user_update: Nutrition):
    updated_result =await db["nutrition"].update_one(
        {"id": id}, {"$set": user_update.dict(exclude_unset=True)})
    if updated_result.modified_count == 0:
        raise HTTPException(status_code=404, detail="User not found or no update needed")
    updated_user =await db["nutrition"].find_one({"id": id})
    return updated_user


@app.delete("/Nutrition/delete/{id}", response_model=dict)
async def delete(id: str):
    delete_result = await db["nutrition"].delete_one({"id": id})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}





@app.post("/Progress/addProgress", response_model=Progress)
async def insert_user(progress: Progress):
    result = await db["progress"].insert_one(progress.dict())
    inserted = await db["progress"].find_one({"_id": result.inserted_id})
    return inserted


@app.get("/Progress/",response_model=Progress)
async def fetch_data(progress: Progress):
    data = await db["progress"].find().to_list(None)
    return data

@app.put("/Progress/update/{id}",response_model=Progress)
async def update_user(id: str, user_update: Progress):
    updated_result =await db["progress"].update_one(
        {"id": id}, {"$set": user_update.dict(exclude_unset=True)})
    if updated_result.modified_count == 0:
        raise HTTPException(status_code=404, detail="User not found or no update needed")
    updated_user =await db["progress"].find_one({"id": id})
    return updated_user


@app.delete("/Progress/delete/{id}", response_model=dict)
async def deletel(id: str):
    delete_result = await db["progress"].delete_one({"id": id})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
