# src/models/base_model.py

from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseModel(ABC):
    """Abstract base class for all models"""
    
    @abstractmethod
    async def generate(self, prompt: str, params: Dict[Any, Any] = None) -> str:
        """Generate content based on prompt"""
        pass

    @abstractmethod
    async def batch_generate(self, prompts: list[str], params: Dict[Any, Any] = None) -> list[str]:
        """Generate content for multiple prompts"""
        pass