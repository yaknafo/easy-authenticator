from fastapi import APIRouter, status


router = APIRouter()


@router.get(
    "/all",
#     response_model=list[BandRead],
    status_code=status.HTTP_200_OK,
    name="roles"
)
async def roles():
    return ["admin", "owner"]

@router.get(
    "",
    status_code=status.HTTP_200_OK,
    name="role"
)
async def get_role(role_name: str):
    return role_name


@router.post(
    "",
    status_code=status.HTTP_200_OK,
    name="create_role"
)
async def create_role(role_name: str):
    ## Adding role
    return role_name


@router.put(
    "",
    status_code=status.HTTP_200_OK,
    name="update_role"
)
async def update_role(role_name: str):
    ## upadate role
    return role_name

