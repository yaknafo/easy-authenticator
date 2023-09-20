from typing import Optional

from pydantic import BaseModel
class CreateEndpointSchema(BaseModel):
    """Represents a role model for the role API."""

    endpoint_name: str
    listen_path: str
    target_url: str
