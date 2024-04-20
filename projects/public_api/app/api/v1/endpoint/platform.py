from fastapi import APIRouter, Depends, HTTPException, Query, status, Body
from app.core.container import Container
from app.service.platform_service import PlatformService
from app.core.middleware import inject
from dependency_injector.wiring import Provide
from shared.models.platform import PlatformDto

router = APIRouter(
    prefix="/platform",
    tags=["platform"],
)


# @router.get(
#     "/",
#     status_code=status.HTTP_200_OK,
#     response_model=PlatformDto.ListResponse,
# )
# @inject
# async def get_platforms(
#     offset: int = Query(0, ge=0),
#     limit: int = Query(10, le=100),
#     name: str = Query(None),
#     platform_service: PlatformService = Depends(Provide[Container.platform_service]),
# ):
#     results = await platform_service.get_platform_list(
#         offset=offset,
#         limit=limit,
#         name=name,
#     )
#     return PlatformDto.ListResponse(
#         offset=offset,
#         limit=limit,
#         total=len(results),
#         results=results,
#     )


@router.post("/")
async def create_platform():
    return {"message": "Platform created successfully"}
