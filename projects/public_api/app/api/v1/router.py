from fastapi import APIRouter

from app.api.v1.endpoint.platform import router as platform_router

router = APIRouter()


routers = [
    platform_router,
]

for _router in routers:
    router.include_router(_router)
