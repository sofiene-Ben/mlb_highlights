from fastapi import APIRouter, Form, Depends, HTTPException
from app.infrastructure.database.dbchallenge import SessionDep
from app.api.auth.security import get_current_active_user
from typing import Annotated
from app.domain.schemas.auth import User
from app.domain.entities.Users import MediaPref
from app.domain.entities.Users import Recurrences
from app.domain.entities.Users import Users


pref_router = APIRouter(prefix="/api")

@pref_router.post("/submit-preferences/")
async def preferences_form(
    session: SessionDep,
    current_user: Annotated[User, Depends(get_current_active_user)],
    # user_id: int = Form(...),  # ID de l'utilisateur (obligatoire)
    media_type: str = Form(...),  # Type de média préféré (exemple : "Video", "Audio", etc.)
    recurrence: str = Form(...),
    fav_player: str = Form(...),
    fav_team: str = Form(...),  # Récurrence (exemple : "Weekly", "Monthly", etc.)
):
    
    # Récupérer l'utilisateur connecté (l'ID est dans current_user.id)
    user_id = current_user.id
    print(f"Utilisateur connecté : {user_id}")

    # Vérifiez si le type de média existe dans la base
    media_pref = session.query(MediaPref).filter(MediaPref.type == media_type).first()
    if not media_pref:
        raise HTTPException(
            status_code=400,
            detail=f"Le type de média '{media_type}' n'est pas valide.",
        )

    # Vérifiez si la récurrence existe dans la base
    recurrence_pref = session.query(Recurrences).filter(Recurrences.name == recurrence).first()
    if not recurrence_pref:
        raise HTTPException(
            status_code=400,
            detail=f"La récurrence '{recurrence}' n'est pas valide.",
        )

    # Mettez à jour les informations de l'utilisateur
    user = session.query(Users).filter(Users.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")

    user.media_pref_id = media_pref.id
    user.recurrence_id = recurrence_pref.id
    user.team_fav = fav_team
    user.player_fav = fav_player

    # Enregistrez les modifications dans la base
    session.add(user)
    session.commit()

    return {
        "message": "Les préférences ont été mises à jour avec succès.",
        "data": {
            "user_id": user_id,
            "media_type": media_type,
            "recurrence": recurrence,
            "fav_player": fav_player,
            "fav_team": fav_team,
        },
    }