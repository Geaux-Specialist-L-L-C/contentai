# src/models/text_generation.py

from typing import Dict, Any
from .base_model import BaseModel
from .bedrock_client import BedrockClient

class TextGenerationModel(BaseModel):
    def __init__(self, model_id: str = "amazon.titan-text-express-v1"):
        self.client = BedrockClient()
        self.model_id = model_id
    
    async def generate(self, prompt: str, params: Dict[Any, Any] = None) -> str:
        if params is None:
            params = {}
        return await self.client.invoke_model(self.model_id, prompt, params)
    
    async def batch_generate(self, prompts: list[str], params: Dict[Any, Any] = None) -> list[str]:
        if params is None:
            params = {}
        results = []
        for prompt in prompts:
            result = await self.generate(prompt, params)
            results.append(result)
        return results