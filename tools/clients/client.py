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


class Claude1:
    def __init__(self):
        super().__init__()
        self.client = boto3.client('bedrock-runtime',
                                   aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                                   aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                                   region_name=os.getenv('REGION_NAME'))

    def run(self, prompt, temperature=0.5):
        body = {
            "prompt": prompt,
            "max_tokens_to_sample": 200,
            "temperature": temperature,
            "stop_sequences": ["\n\nHuman:"],
        }
        response = self.client.invoke_model(
            modelId="anthropic.claude-instant-v1", body=json.dumps(body)
        )
        return claud1_response_parser(response)


def claud1_response_parser(response):
    response_body = json.loads(response["body"].read())
    completion = response_body["completion"]
    return completion


def haiku_response_parser(response):
    response_body = json.loads(response.get("body").read())
    results = response_body.get("content")[0].get("text")
    return results


class Claude3Haiku:
    def __init__(self):
        super().__init__()
        self.client = boto3.client('bedrock-runtime',
                                   aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                                   aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                                   region_name=os.getenv('REGION_NAME'))

    def run(self, prompt):
        prompt_config = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 4096,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                    ],
                }
            ],
        }
        body = json.dumps(prompt_config)

        model_id = "anthropic.claude-3-haiku-20240307-v1:0"
        accept = "application/json"
        content_type = "application/json"
        response = self.client.invoke_model(
            body=body, modelId=model_id, accept=accept, contentType=content_type
        )
        ret = haiku_response_parser(response)
        return ret


