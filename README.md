# OpenSearch Skills LLM Evaluation Python Tool
## AWS credentials
Create a `.env` file in the same directory with `main.py`. Configure AWS credential in it e.g.
```bash
AWS_ACCESS_KEY_ID={yous aws access key}
AWS_SECRET_ACCESS_KEY={your aws secret access key}
REGION_NAME={aws region e.g. us-east-1}
```
## Installation
Create venv
```bash
python3 -m venv skills && cd skills
```
Activate venv
```bash
source ./bin/activate
```
Install dependencies
```bash
pip3 install -r requirements.txt
```
## Run
Change json file path in main.py, then run
```bash
python3 main.py
```

