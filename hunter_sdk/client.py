"""Hunter API client implementation."""

from typing import Any, Dict
import httpx


class HunterClient(object):
    """Client for interacting with Hunter.io API."""

    def __init__(self, api_key: str) -> None:
        """Initialize Hunter client with API key."""
        self._api_key = api_key
        self._base_url = 'https://api.hunter.io/v2'

    async def verify_email(self, email: str) -> Dict[str, Any]:
        """Verify email address via Hunter API."""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f'{self._base_url}/email-verifier',
                params={'email': email, 'api_key': self._api_key},
                timeout=10,
            )
            response.raise_for_status()
            return response.json().get('data', {})

    async def domain_search(self, domain: str) -> Dict[str, Any]:
        """Search domain via Hunter API."""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f'{self._base_url}/domain-search',
                params={'domain': domain, 'api_key': self._api_key},
                timeout=10,
            )
            response.raise_for_status()
            return response.json().get('data', {})
