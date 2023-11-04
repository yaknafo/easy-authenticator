from pydantic import BaseModel


class CreateEndpointSchema(BaseModel):
    """Represents an endpoint model for the role API."""

    endpoint_name: str
    listen_path: str
    target_url: str


class EndpointSchema(BaseModel):
    """Represents an endpoint model for the role API."""
    api_id: str
    listen_path: str
    target_url: str
    auth_header_name: str
