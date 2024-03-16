from fastapi import APIRouter, Depends, HTTPException, Query, status, Body

router = APIRouter(
    prefix="/user",
    tags=["user"],
)
