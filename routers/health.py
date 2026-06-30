from fastapi import APIRouter

from settings import settings


router = APIRouter()


@router.get("/")
async def root() -> dict[str, str]:
    return {"message": f"{settings.app_name} is running"}


@router.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
