from pydantic import BaseModel


class AuthSchemaInput(BaseModel):
    """Represents a role model for the role API."""

    user_name: str
    password: str
