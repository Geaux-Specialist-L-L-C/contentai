# backend/app/api/content.py
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.models.content import Content
from app.services.content import ContentService
from app.database import Database

router = APIRouter()

@router.post("/", response_model=Content)
async def create_content(content: Content):
    db = await Database.connect_db()
    service = ContentService(db)
    return await service.create(content)

@router.get("/{content_id}", response_model=Content)
async def get_content(content_id: str):
    db = await Database.connect_db()
    service = ContentService(db)
    content = await service.get(content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    return content

@router.get("/", response_model=List[Content])
async def list_contents(skip: int = 0, limit: int = 10, tags: List[str] = None):
    db = await Database.connect_db()
    service = ContentService(db)
    if tags:
        return await service.search_by_tags(tags, skip, limit)
    return await service.list(skip=skip, limit=limit)

@router.patch("/{content_id}/status", response_model=Content)
async def update_content_status(content_id: str, status: str):
    db = await Database.connect_db()
    service = ContentService(db)
    content = await service.update_status(content_id, status)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    return content