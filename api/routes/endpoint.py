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
    return EndpointService().get_endpoints()


@router.post(
    "",
    response_model=EndpointSchema,
    status_code=status.HTTP_201_CREATED,
    name="create_endpoint"
)
async def create_endpoint(endpoint: CreateEndpointSchema):
    return EndpointService().CreateEndpoint(endpoint)


@router.delete(
    "",
    response_model=str,
    status_code=status.HTTP_200_OK,
    name="delete_endpoint"
)
async def create_endpoint(api_id: str):
    EndpointService().delete_endpoint(api_id)
    return f"{api_id} has been deleted"
