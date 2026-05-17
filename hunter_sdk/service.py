"""Service layer for Hunter SDK."""

from typing import Any
from hunter_sdk.client import HunterClient
from hunter_sdk.storage import Storage
from hunter_sdk.models import EmailVerificationData, DomainSearchData


class HunterService(object):
    """Service class for coordinating Hunter API calls and storage."""

    def __init__(self, client: HunterClient, storage: Storage) -> None:
        """Initialize Hunter service with client and storage."""
        self._client = client
        self._storage = storage

    async def verify_email(self, email: str) -> EmailVerificationData:
        """Verify email address via client."""
        raw_data = await self._client.verify_email(email)
        return EmailVerificationData(**raw_data)

    async def search_domain(self, domain: str) -> DomainSearchData:
        """Search domain via client."""
        raw_data = await self._client.domain_search(domain)
        return DomainSearchData(**raw_data)

    def save_email_verification(self, data: EmailVerificationData) -> None:
        """Save email verification data to storage."""
        self._storage.create(data.email, data.model_dump())

    def save_domain_search(self, data: DomainSearchData) -> None:
        """Save domain search data to storage."""
        self._storage.create(data.domain, data.model_dump())

    def get_stored_data(self, key: str) -> Any:
        """Retrieve stored data by key."""
        return self._storage.read(key)
