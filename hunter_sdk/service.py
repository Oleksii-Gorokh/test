from typing import Any, Dict
from hunter_sdk.client import HunterClient
from hunter_sdk.storage import Storage


class HunterService(object):
    def __init__(self, client: HunterClient, storage: Storage) -> None:
        self._client = client
        self._storage = storage

    def verify_and_save(self, email: str) -> Dict[str, Any]:
        result = self._client.verify_email(email)
        self._storage.create(email, result)
        return result

    def search_and_save(self, domain: str) -> Dict[str, Any]:
        result = self._client.domain_search(domain)
        self._storage.create(domain, result)
        return result

    def get_stored_data(self, key: str) -> Any:
        return self._storage.read(key)
