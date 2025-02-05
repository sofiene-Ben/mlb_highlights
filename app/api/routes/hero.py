from app.infrastructure.database.dbchallenge import SessionDep
from fastapi import Depends,APIRouter, HTTPException, Query
from app.domain.entities.Hero import Hero
from typing import Annotated
from sqlmodel import  select
from app.domain.schemas.auth import User
from app.api.auth.security import get_current_active_user



# from main import get_current_active_user  # Importez la fonction pour vérifier l'utilisateur actif
from app.domain.entities.Users import Users 


hero_router = APIRouter(prefix="/api")

@hero_router.get("/")
def home():

    return {
       "hello" : "heroes"
    }

@hero_router.post("/heroes/")
def create_hero(hero: Hero, session: SessionDep) -> Hero:
    session.add(hero)
    session.commit()
    session.refresh(hero)
    
    return hero

@hero_router.get("/heroes/")
def read_heroes(
    session: SessionDep,
    current_user: Annotated[User, Depends(get_current_active_user)],
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Hero]:
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    
    return heroes

@hero_router.get("/heroes/{hero_id}")
def read_hero(hero_id: int, session: SessionDep) -> Hero:
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero

@hero_router.delete("/heroes/{hero_id}")
def delete_hero(hero_id: int, session: SessionDep):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return {"ok": True}
