from typing import Any, Dict
from hunter_sdk.client import HunterClient
from hunter_sdk.storage import Storage
from hunter_sdk.models import EmailVerificationData, DomainSearchData


class HunterService(object):
    def __init__(self, client: HunterClient, storage: Storage) -> None:
        self._client = client
        self._storage = storage

    async def verify_and_save(self, email: str) -> EmailVerificationData:
        raw_data = await self._client.verify_email(email)
        validated_data = EmailVerificationData(**raw_data)
        self._storage.create(email, validated_data.model_dump())
        return validated_data

    async def search_and_save(self, domain: str) -> DomainSearchData:
        raw_data = await self._client.domain_search(domain)
        validated_data = DomainSearchData(**raw_data)
        self._storage.create(domain, validated_data.model_dump())
        return validated_data

    def get_stored_data(self, key: str) -> Any:
        return self._storage.read(key)
