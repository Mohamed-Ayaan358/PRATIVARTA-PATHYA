from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
import json
#from mongo import db, Villagers

pp=FastAPI()

origins=["*"]
pp.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

#@pp.post("/", response_description="Add new user", response_model=Villagers)
#async def create_user(user: Villagers): #= Body(...)):
  #  user = jsonable_encoder(student)
   # new_user = await db["users"].insert_one(student)
   # created_user = await db["users"].find_one({"_id": new_user.inserted_id})
   # return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)
#@pp.get("/listusers", response_description="List all users", response_model=list[Villagers])
#async def list_users():
#    users = await db["users"].find().to_list(1000)
#    return users

class Villagers(BaseModel):
    email: str
    password: str
@pp.post('/details')
def det(det:Villagers):
    enc=jsonable_encoder(det)
    mail=enc['email']
    passw=enc['password']
    d={
        "email":mail,
        "password":passw,
    }
    print("i m in")
    f=open("villagers.txt",'a')
    #f=open('D:/Downloads/details.txt','a')
    f.write(f'{mail},{str(passw)} \n')
    f.close

    return 'hello your data has been noted'   
