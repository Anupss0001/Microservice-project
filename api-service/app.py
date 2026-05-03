from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API Service Running"}

@app.get("/data")
def get_data():
    return {"data": "Protected Data"}
