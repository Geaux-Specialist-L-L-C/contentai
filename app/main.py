# backend/app/main.py
from fastapi import FastAPI
from .database import Database
from .api.base import api_router

app = FastAPI(title="ContentAI")
app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
async def startup():
    await Database.connect_db()

@app.on_event("shutdown")
async def shutdown():
    await Database.disconnect_db()