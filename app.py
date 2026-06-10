from fastapi import FastAPI
from backend.routes.upload import router as upload_router
from backend.routes.process import router as process_router

app = FastAPI()
app.include_router(upload_router)
app.include_router(process_router)

@app.get("/")
def home():
    return {"message": "Incident Resolution Assistant Running"}