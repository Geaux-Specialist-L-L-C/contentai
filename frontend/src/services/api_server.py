# src/services/api_server.py

import logging
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import boto3
import json
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="K12 Content Generation API")

# Pydantic models for request/response
class GenerationRequest(BaseModel):
    prompt: str
    grade_level: Optional[int]
    subject: Optional[str]
    max_tokens: Optional[int] = 512
    temperature: Optional[float] = 0.7

class GenerationResponse(BaseModel):
    generated_text: str
    model_used: str

# Initialize Bedrock client
bedrock_client = boto3.client(
    service_name='bedrock-runtime',
    region_name=os.getenv('AWS_REGION', 'us-east-1')
)

@app.post("/generate", response_model=GenerationResponse)
async def generate_content(request: GenerationRequest):
    try:
        # Format prompt with educational context
        formatted_prompt = f"""
        Grade Level: {request.grade_level}
        Subject: {request.subject}
        Task: {request.prompt}
        """
        
        # Prepare request body for Bedrock
        body = {
            "prompt": formatted_prompt,
            "max_tokens": request.max_tokens,
            "temperature": request.temperature,
            "top_p": 0.9,
        }

        # Call Bedrock model
        response = bedrock_client.invoke_model(
            modelId='amazon.titan-text-express-v1',
            body=json.dumps(body)
        )
        
        response_body = json.loads(response['body'].read())
        
        return GenerationResponse(
            generated_text=response_body['completion'],
            model_used='amazon.titan-text-express-v1'
        )

    except Exception as e:
        logger.error(f"Error generating content: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}