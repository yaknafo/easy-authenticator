from pydantic import BaseModel


class UserSchema(BaseModel):
    """Represents a role model for the role API."""

    id: int
    user_name: str
    role_id: int


class UserSchemaInput(BaseModel):
    """Represents a role model for the role API."""

    user_name: str
    password: str
    role_id: int
