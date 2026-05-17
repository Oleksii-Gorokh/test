import os
from fastapi import FastAPI, HTTPException
from hunter_sdk.client import HunterClient
from hunter_sdk.storage import FileStorage
from hunter_sdk.service import HunterService

app = FastAPI()

api_key = os.getenv('HUNTER_API_KEY', 'test_key')
client = HunterClient(api_key)
storage = FileStorage('storage.json')
service = HunterService(client, storage)


@app.get('/verify/{email}')
async def verify_email(email: str):
    try:
        verification_data = await service.verify_email(email)
        service.save_email_verification(verification_data)
        return verification_data
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.get('/search/{domain}')
async def search_domain(domain: str):
    try:
        domain_data = await service.search_domain(domain)
        service.save_domain_search(domain_data)
        return domain_data
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.get('/storage/{key}')
async def get_storage(key: str):
    data = service.get_stored_data(key)
    if not data:
        raise HTTPException(status_code=404, detail='Not found')
    return data
