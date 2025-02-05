from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException
from app.domain.schemas.auth import User
from app.domain.entities.Users import Users
from app.api.auth.security import get_current_active_user
from app.api.auth.security import get_password_hash
from app.infrastructure.database.dbchallenge import SessionDep
from sqlmodel import  select, Session
from app.infrastructure.database.dbchallenge import get_session


user_router = APIRouter(prefix="/api")

@user_router.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user


@user_router.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]


@user_router.post("/singup")
def signup(username: str, password: str, db: SessionDep):
    hashed_password = get_password_hash(password)
    user = Users(username=username, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@user_router.get("/user/favorite-team/")
async def get_favorite_team(
    current_user: Users = Depends(get_current_active_user),
    session: Session = Depends(get_session)
):
    if current_user.team_fav:
        favorite_team = session.exec(
            select(current_user.team_fav)
        ).first()
        if favorite_team:
            return {"favorite_team": favorite_team}
        else:
            raise HTTPException(status_code=404, detail="Favorite team not found")
    else:
        raise HTTPException(status_code=404, detail="User has no favorite team")