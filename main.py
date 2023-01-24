from twilio.rest import Client
import random
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from pydantic import BaseModel

load_dotenv()
app = FastAPI()
app.add_middleware(CORSMiddleware)


class User(BaseModel):
    phone_number: str


@app.post("/code")
def generate_verification_code(user : User ):
    
    #phone_number = phone_number
    verification_code = random.randint(100000, 999999)
    account_sid = os.environ["account_sid"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)
    #phone_number = os.environ["phone_number"]
    
    message = client.messages.create(
        body=f"Your verification code is: {verification_code}",
        from_="+13856441601",
        to=user.phone_number

    )
    return {"message": "ok", "code": verification_code}


