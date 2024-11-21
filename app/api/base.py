# backend/app/api/base.py
from fastapi import APIRouter
from .content import router as content_router
from .user import router as user_router

api_router = APIRouter()
api_router.include_router(content_router, prefix="/content", tags=["content"])
api_router.include_router(user_router, prefix="/users", tags=["users"])