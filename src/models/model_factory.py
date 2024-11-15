# src/models/model_factory.py

from typing import Dict, Any
from .text_generation import TextGenerationModel

class ModelFactory:
    @staticmethod
    def create_model(model_type: str, config: Dict[Any, Any] = None) -> Any:
        if model_type == "text":
            model_id = config.get("model_id", "amazon.titan-text-express-v1")
            return TextGenerationModel(model_id=model_id)
        raise ValueError(f"Unknown model type: {model_type}")