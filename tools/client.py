import os
import json
import boto3
from dotenv import load_dotenv

load_dotenv()


class Client:
    def __init__(self):
        self.client = None

    def run(self):
        pass


class Claude:
    def __init__(self):
        super().__init__()
        self.client = boto3.client('bedrock-runtime',
                                   aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                                   aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                                   region_name=os.getenv('REGION_NAME'))

    def run(self, prompt):
        body = {
            "prompt": prompt,
            "max_tokens_to_sample": 200,
            "temperature": 0.5,
            "stop_sequences": ["\n\nHuman:"],
        }
        response = self.client.invoke_model(
            modelId="anthropic.claude-instant-v1", body=json.dumps(body)
        )
        response_body = json.loads(response["body"].read())
        completion = response_body["completion"]
        return completion

