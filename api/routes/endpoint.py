from fastapi import APIRouter, status

from schema.endpoint import CreateEndpointSchema
from service.endpoint_service import EndpointService

router = APIRouter()

@router.post(
    "",
    response_model=str,
    status_code=status.HTTP_201_CREATED,
    name="create_endpoint"
)
async def create_role(endpoint: CreateEndpointSchema):
    EndpointService().CreateEndpoint(endpoint)
    return f"endpoint {endpoint.endpoint_name} successfully created"
