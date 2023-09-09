from typing import Optional

from pydantic import BaseModel


class RoleSchema(BaseModel):
    """Represents a role model for the role API."""

    id: Optional[int]
    name: str
    token: str


class RoleSchemaInput(BaseModel):
    """Represents a role model for the role API."""

    name: str
    token: str

