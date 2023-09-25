from fastapi import APIRouter, status

router = APIRouter()


@router.get(
    "",

    status_code=status.HTTP_200_OK,
    name="health"
)
async def health():
    return "I am up and running"
