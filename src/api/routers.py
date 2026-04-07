from fastapi import APIRouter, Depends, HTTPException, status
from src.application.services import UserRegistrationService, UserAlreadyExistsError
from src.api.schemas import UserCreateRequest, UserResponse
from src.api.dependencies import get_registration_service

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(
    request: UserCreateRequest,
    service: UserRegistrationService = Depends(get_registration_service)
):
    try:
        user = service.register_user(email=request.email, username=request.username)
        return user
    except UserAlreadyExistsError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))