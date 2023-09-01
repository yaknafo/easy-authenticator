from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class RoleSchema(BaseModel):
    """Represents a role model for the role API."""

    id: Optional[UUID]
    name: str
    token: str
