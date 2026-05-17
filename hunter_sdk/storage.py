import json
import os
from typing import Any, Dict, Optional


class Storage(object):
    def __init__(self) -> None:
        self._data: Dict[str, Any] = {}

    def create(self, key: str, value: Any) -> None:
        self._data[key] = value

    def read(self, key: str) -> Optional[Any]:
        return self._data.get(key)

    def update(self, key: str, value: Any) -> None:
        if key not in self._data:
            raise KeyError(f'Key {key} not found in storage')
        self._data[key] = value

    def delete(self, key: str) -> None:
        if key not in self._data:
            raise KeyError(f'Key {key} not found in storage')
        del self._data[key]


class FileStorage(Storage):
    def __init__(self, file_path: str) -> None:
        super().__init__()
        self._file_path = file_path
        self._load()

    def create(self, key: str, value: Any) -> None:
        super().create(key, value)
        self._save()

    def update(self, key: str, value: Any) -> None:
        super().update(key, value)
        self._save()

    def delete(self, key: str) -> None:
        super().delete(key)
        self._save()

    def _load(self) -> None:
        if os.path.exists(self._file_path):
            with open(self._file_path, 'r') as file_obj:
                self._data = json.load(file_obj)

    def _save(self) -> None:
        with open(self._file_path, 'w') as file_obj:
            json.dump(self._data, file_obj)
