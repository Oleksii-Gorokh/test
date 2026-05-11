from typing import Any, Dict, Optional


class Storage(object):
    def __init__(self) -> None:
        self._data: Dict[str, Any] = {}

    def create(self, key: str, value: Any) -> None:
        self._data[key] = value

    def read(self, key: str) -> Optional[Any]:
        return self._data.get(key)

    def update(self, key: str, value: Any) -> None:
        if key in self._data:
            self._data[key] = value

    def delete(self, key: str) -> None:
        if key in self._data:
            del self._data[key]
