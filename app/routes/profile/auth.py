
from fastapi import status, HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.models import Token,User
from app.helpers.config import settings
from app.src.auth.oauth2 import create_access_token

router = APIRouter(
    tags=["Auth"],
    prefix="/v1/auth"
)

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)  # Implement this
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    print(user)
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


def authenticate_user(username: str, password: str):
    # TO-DO 
    # Implement your user authentication logic here
    # For example, check if the user exists and the password is correct
    # Return the user object if authenticated, otherwise return None
    return User(username=username, email="user@example.com", full_name="John Doe", disabled=False)
    
