# src/models/bedrock_client.py

import boto3
import json
from typing import Dict, Any

class BedrockClient:
    def __init__(self, region: str = "us-east-1"):
        self.client = boto3.client(
            service_name="bedrock-runtime",
            region_name=region
        )
    
    async def invoke_model(self, 
                         model_id: str,
                         prompt: str, 
                         params: Dict[Any, Any] = None) -> str:
        body = {
            "prompt": prompt,
            "max_tokens": params.get("max_tokens", 512),
            "temperature": params.get("temperature", 0.7),
            "top_p": params.get("top_p", 0.9),
        }
        
        response = self.client.invoke_model(
            modelId=model_id,
            body=json.dumps(body)
        )
        
        return json.loads(response["body"].read())["completion"]