from typing_extensions import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from src.application.services import UserRegistrationService, UserAlreadyExistsError
from src.api.schemas import UserCreateRequest, UserResponse
from src.api.dependencies import get_registration_service

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(
    request: UserCreateRequest,
    service: Annotated[UserRegistrationService, Depends(get_registration_service)]
):
    try:
        user = service.register_user(email=request.email, username=request.username)
        return user
    except UserAlreadyExistsError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    
@router.get("/email/{email}", response_model=UserResponse)
def get_user_by_email(
    email: str,
    service: Annotated[UserRegistrationService, Depends(get_registration_service)]
):
    user = service.get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.get("/username/{username}", response_model=UserResponse)
def get_user_by_username(
    username: str,
    service: Annotated[UserRegistrationService, Depends(get_registration_service)]
):
    user = service.get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user