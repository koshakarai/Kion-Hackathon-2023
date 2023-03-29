# signup endpoint
""" auth app router 

    Api endpoints:
        /auth/signup
        /auth/login
        /auth/ping
"""
import json
from fastapi import APIRouter, Depends, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse



from .services import create_user



router = APIRouter(
    prefix = '/example',
    responses = {404: {"description": "Not found"}},
)

# /auth/signup
@router.post("/signup", include_in_schema=False)
async def signup(request: Request):
    
   req = await request.json()
   
   email = req['email']
   password = req['password']
   
   if email is None:
       return HTTPException(detail={'message': 'Error! Missing Email'}, 
                            status_code=400)
   if password is None:
       return HTTPException(detail={'message': 'Error! Missing Password'}, 
                            status_code=400)
   
   try:
       user = create_user(
           email=email,
           password=password
           ) # create_user
       return JSONResponse(content={'message': f'Successfully created user {user.uid}'}, status_code=200)    
   except:
       return HTTPException(detail={'message': 'Error Creating User'}, status_code=400)
   
# /auth/login
@router.post("/login", include_in_schema=False)
async def login(request: Request):
   req_json = await request.json()
   
   email = req_json['email']
   password = req_json['password']
   
   if email is None:
       return HTTPException(detail={'message': 'Error! Missing Email'}, 
                            status_code=400)
   if password is None:
       return HTTPException(detail={'message': 'Error! Missing Password'}, 
                            status_code=400)
   try:
       user = pyrebase.auth().sign_in_with_email_and_password(email, password)# login user
       jwt = user['idToken']
       return JSONResponse(content={'token': jwt}, status_code=200)
   except:
       return HTTPException(detail={'message': 'There was an error logging in'}, status_code=400)
   
#/auth/ping
@router.post("/ping", include_in_schema=False)
async def validate(request: Request):
   headers = request.headers
   jwt = headers.get('authorization')
   print(f"jwt:{jwt}")
   user = auth.verify_id_token(jwt) #get_user_by_token
   return user["uid"]