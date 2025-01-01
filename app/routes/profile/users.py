
from fastapi import Depends, APIRouter
from app.models import User
from app.src import get_current_active_user

router = APIRouter(
    tags=["Users"],
    prefix="/v1/users"
)

@router.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

# Protected route example
@router.get("/protected-resource")
async def protected_route(current_user: User = Depends(get_current_active_user)):
    return {"message": "This is a protected resource", "user": current_user}
