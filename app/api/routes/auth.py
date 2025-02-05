from typing import Annotated
from app.domain.schemas.auth import Token
from fastapi.security import OAuth2PasswordRequestForm
from app.api.auth.security import create_access_token, authenticate_user
from fastapi import Depends, HTTPException, status, APIRouter
from app.infrastructure.database.dbchallenge import get_session
from app.infrastructure.config.app import settings
from datetime import timedelta
from sqlmodel import Session


auth_router = APIRouter(prefix="")

ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

@auth_router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db_session: Annotated[Session, Depends(get_session)],
) -> Token:
    user = authenticate_user(db_session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")