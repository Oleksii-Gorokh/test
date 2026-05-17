"""Pydantic models for Hunter API responses."""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel


class EmailVerificationData(BaseModel):
    """Model representing email verification result."""

    result: str
    score: int
    email: str
    regexp: bool
    gibberish: bool
    disposable: bool
    webmail: bool
    mx_records: bool
    smtp_server: bool
    smtp_check: bool
    accept_all: bool
    sources: List[Dict[str, Any]]


class DomainSearchData(BaseModel):
    """Model representing domain search result."""

    domain: str
    disposable: bool
    webmail: bool
    pattern: Optional[str] = None
    organization: Optional[str] = None
    emails: List[Dict[str, Any]]
