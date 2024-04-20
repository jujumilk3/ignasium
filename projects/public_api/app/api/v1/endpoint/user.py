from fastapi import APIRouter, Body, Depends, HTTPException, Query, status

router = APIRouter(
    prefix="/user",
    tags=["user"],
)
