from fastapi import APIRouter, status

from schema.endpoint import CreateEndpointSchema, EndpointSchema
from service.endpoint_service import EndpointService

router = APIRouter()

@router.get(
    "/all",
    response_model=list[EndpointSchema],
    status_code=status.HTTP_200_OK,
    name="endpoints"
)
async def endpoints():
    return EndpointService().get_endpoints();


@router.post(
    "",
    response_model=EndpointSchema,
    status_code=status.HTTP_201_CREATED,
    name="create_endpoint"
)
async def create_endpoint(endpoint: CreateEndpointSchema):
    return EndpointService().CreateEndpoint(endpoint)
