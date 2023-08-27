from fastapi import APIRouter, status


router = APIRouter()

fake_db = [
    {"name": "Foo Fighters", "song": "My Hero"},
    {"name": "Metallica", "song": "Hero of the Day"}
]


@router.get(
    "",
#     response_model=list[BandRead],
    status_code=status.HTTP_200_OK,
    name="auth"
)
async def auth():
    return "aaa=="