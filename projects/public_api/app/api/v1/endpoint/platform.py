from dependency_injector.wiring import Provide
from fastapi import APIRouter, Body, Depends, Path, Query, status
from shared.models.platform import PlatformDto

from app.core.container import Container
from app.core.middleware import inject
from app.service.platform_service import PlatformService

router = APIRouter(
    prefix="/platform",
    tags=["platform"],
)


@router.get(
    "/{platform_id}",
    status_code=status.HTTP_200_OK,
    response_model=PlatformDto.WithModelBaseInfo,
)
@inject
async def get_platform_by_id(
    platform_id: int = Path(...),
    platform_service: PlatformService = Depends(Provide[Container.platform_service]),
):
    result = await platform_service.get_by_id(platform_id=platform_id)
    return result


@router.get(
    "/{platform_name}",
    status_code=status.HTTP_200_OK,
    response_model=PlatformDto.WithModelBaseInfo,
)
@inject
async def get_platform_by_name(
    platform_name: str = Path(...),
    platform_service: PlatformService = Depends(Provide[Container.platform_service]),
):
    result = await platform_service.get_by_name(platform_name=platform_name)
    return result


@router.patch(
    "/{platform_id}",
    status_code=status.HTTP_200_OK,
    response_model=PlatformDto.WithModelBaseInfo,
)
@inject
async def patch_platform_by_id(
    platform_id: int = Path(...),
    upsert_platform: PlatformDto.Upsert = Body(...),
    platform_service: PlatformService = Depends(Provide[Container.platform_service]),
):
    result = await platform_service.patch(model_id=platform_id, dto=upsert_platform)
    return result


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


@router.delete(
    "/{platform_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
async def delete_platform_by_id(
    platform_id: int = Path(...),
    platform_service: PlatformService = Depends(Provide[Container.platform_service]),
):
    await platform_service.remove_by_id(model_id=platform_id)
    return None
