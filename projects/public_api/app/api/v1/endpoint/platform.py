from fastapi import APIRouter, Depends, HTTPException, Query, status

router = APIRouter(
    prefix="/platform",
    tags=["platform"],
)


@router.get("/")
async def read_platform_root():
    return {"Hello": "World"}
