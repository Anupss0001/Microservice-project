from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Auth Service Running"}

@app.post("/login")
def login():
    return {"token": "fake-jwt-token"}

@app.get("/env")
def env():
    return {
        "db_host": os.getenv("DB_HOST"),
        "db_user": os.getenv("DB_USER")
    }
