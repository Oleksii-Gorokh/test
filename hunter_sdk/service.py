from typing import Any
from hunter_sdk.client import HunterClient
from hunter_sdk.storage import Storage
from hunter_sdk.models import EmailVerificationData, DomainSearchData


class HunterService(object):
    def __init__(self, client: HunterClient, storage: Storage) -> None:
        self._client = client
        self._storage = storage

    async def verify_email(self, email: str) -> EmailVerificationData:
        raw_data = await self._client.verify_email(email)
        return EmailVerificationData(**raw_data)

    async def search_domain(self, domain: str) -> DomainSearchData:
        raw_data = await self._client.domain_search(domain)
        return DomainSearchData(**raw_data)

    def save_email_verification(self, data: EmailVerificationData) -> None:
        self._storage.create(data.email, data.model_dump())

    def save_domain_search(self, data: DomainSearchData) -> None:
        self._storage.create(data.domain, data.model_dump())

    def get_stored_data(self, key: str) -> Any:
        return self._storage.read(key)
