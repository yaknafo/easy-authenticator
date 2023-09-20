from typing import Optional

from pydantic import BaseModel


class RoleEndpointSchema(BaseModel):
    """Represents a role_endpoint model for the role API."""

    role_id: int
    api_id: str


class RoleSchema(BaseModel):
    """Represents a role model for the role API."""

    id: Optional[int]
    name: str
    token: str
    endpoint: list[RoleEndpointSchema]


class RoleSchemaInput(BaseModel):
    """Represents a role model for the role API."""

    name: str
    token: str


