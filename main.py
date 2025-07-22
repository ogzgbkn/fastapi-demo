from fastapi import FastAPI
from dotenv import load_dotenv, find_dotenv
from app.controllers import signup

load_dotenv()

app = FastAPI()
app.include_router(signup.router)