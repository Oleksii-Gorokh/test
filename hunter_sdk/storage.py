"""Storage layer implementation for Hunter SDK."""

import json
import os
from typing import Any, Dict, Optional


class Storage(object):
    """Base class for key-value storage."""

    def __init__(self) -> None:
        """Initialize in-memory storage."""
        self._data: Dict[str, Any] = {}

    def create(self, key: str, value: Any) -> None:
        """Create new key-value pair in storage."""
        self._data[key] = value

    def read(self, key: str) -> Optional[Any]:
        """Read value by key from storage."""
        return self._data.get(key)

    def update(self, key: str, value: Any) -> None:
        """Update existing key with new value."""
        if key not in self._data:
            raise KeyError(f'Key {key} not found in storage')
        self._data[key] = value

    def delete(self, key: str) -> None:
        """Delete key from storage."""
        if key not in self._data:
            raise KeyError(f'Key {key} not found in storage')
        del self._data[key]


class FileStorage(Storage):
    """File-backed key-value storage implementation."""

    def __init__(self, file_path: str) -> None:
        """Initialize file storage with file path."""
        super().__init__()
        self._file_path = file_path
        self._load()

    def create(self, key: str, value: Any) -> None:
        """Create new key-value pair and save to file."""
        super().create(key, value)
        self._save()

    def update(self, key: str, value: Any) -> None:
        """Update existing key and save to file."""
        super().update(key, value)
        self._save()

    def delete(self, key: str) -> None:
        """Delete key and save to file."""
        super().delete(key)
        self._save()

    def _load(self) -> None:
        """Load data from JSON file if it exists."""
        if os.path.exists(self._file_path):
            with open(self._file_path, 'r') as file_obj:
                self._data = json.load(file_obj)

    def _save(self) -> None:
        """Save current data to JSON file."""
        with open(self._file_path, 'w') as file_obj:
            json.dump(self._data, file_obj)
