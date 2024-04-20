from fastapi import APIRouter, Depends, Query, status, Body
from app.core.container import Container
from app.service.platform_service import PlatformService
from app.core.middleware import inject
from dependency_injector.wiring import Provide
from shared.models.platform import PlatformDto

router = APIRouter(
    prefix="/platform",
    tags=["platform"],
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=PlatformDto.WithModelBaseInfo,
)
@inject
async def create_platform(
    upsert_platform: PlatformDto.Upsert = Body(...),
    platform_service: PlatformService = Depends(Provide[Container.platform_service]),
):
    result = await platform_service.add(dto=upsert_platform)
    return result
