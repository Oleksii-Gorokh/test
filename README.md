# Hunter SDK

Test task: Hunter.io SDK + FastAPI.

## Setup
1. `pip install -r requirements.txt`
2. `uvicorn main:app --reload`

## API Endpoints
Local testing links:
- `http://127.0.0.1:8000/verify/test@gmail.com` — email verification
- `http://127.0.0.1:8000/search/google.com` — domain search
- `http://127.0.0.1:8000/storage/google.com` — view stored data

## Code Quality
- `mypy .`
- `flake8 .`
