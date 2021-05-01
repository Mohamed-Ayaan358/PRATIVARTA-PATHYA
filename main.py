from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
import random
from datetime import datetime
import json
from fastapi.responses import HTMLResponse

pp=FastAPI()

origins=["*"]
pp.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
class villagers(BaseModel):
   email : str
   password : str

@pp.get('/home',response_class=HTMLResponse)
def signup(villagers:villagers):
	enc=jsonable_encoder(det)
	v_name=enc['email']
	password=enc['password']
	d={
	    "email":v_name,
	    "password":password,
    }
	return 'hello '+v_name+'you have been registered,go to the Login page to Login'

