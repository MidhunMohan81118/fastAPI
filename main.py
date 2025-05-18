from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message":"Hello World.."}

@app.get('/greet/{name}')
async def greet_name(name:str) ->dict:
    return {"message":f"hello {name}"}
    
  
###################### Query parameter ####################################
@app.get('/greet')
async def greet_name(name:str) ->dict:   #'''parameter will not pass directly with url'''
    return {"message":f"hello {name}"}

@app.get('/nameage')
async def greet(name:str,age:int) ->dict:
    return {"message":f"hello {name} , you are {age} years old"}



####################### Optional ############################
#inorder to make passing argument we can make it optional so error can be avoided
# using Optional means the user does not have to provide the parameter. If it’s missing, the default is None
from typing import Optional
@app.get('/greet_me')
async def greet_me(name:Optional[str]="User",age:int=0) ->dict:
    return {"message":f"hello {name} , you are {age} years old"}


#################################### POST #####################################
from pydantic import BaseModel

class BookCreateModel(BaseModel):
    title : str
    author : str
    
@app.post("/create_book")
async def create_book(bookdata:BookCreateModel):
    return {"Title":bookdata.title,"Author":bookdata.author}


############################# header info ####################################
from fastapi import Header, HTTPException

@app.get('/get_header')
async def get_header(accept:str=Header(None),content_type:str=Header(None),user_agent:str=Header(None),host:str=Header(None)):
    request_header={}
    request_header["Accept"]=accept
    request_header["Content-Type"]=content_type
    request_header["User-Agent"]=user_agent
    request_header["Host"]=host
    return request_header