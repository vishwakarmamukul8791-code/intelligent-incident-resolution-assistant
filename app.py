from fastapi import FastAPI
from backend.routes.upload import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Incident Resolution Assistant Running"}