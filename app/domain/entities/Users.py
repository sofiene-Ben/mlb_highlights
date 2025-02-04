from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

# Définition du modèle UserInDB
class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # Identifiant unique de l'utilisateur
    username: str  # Nom d'utilisateur
    email: Optional[str] = None  # Email de l'utilisateur
    full_name: Optional[str] = None  # Nom complet de l'utilisateur
    hashed_password: str  # Mot de passe haché
    disabled: Optional[bool] = False  # Indicateur si l'utilisateur est désactivé

    team_fav: Optional[int] = Field(default=None)
    player_fav: Optional[int] = Field(default=None)


    # Clés étrangères
    recurrence_id: Optional[int] = Field(default=None, foreign_key="recurrences.id")
    media_pref_id: Optional[int] = Field(default=None, foreign_key="mediapref.id")

    # Relations
    recurrence: Optional["Recurrences"] = Relationship(back_populates="users")
    media_pref: Optional["MediaPref"] = Relationship(back_populates="users")

class Recurrences(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)  # Exemple : "Weekly", "Monthly", etc.

    # Relation avec User
    users: List["Users"] = Relationship(back_populates="recurrence")  # Corrigé

class MediaPref(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    type: str = Field(nullable=False)  # Exemple : "Video", "Audio", "Text"

    # Relation avec User
    users: List["Users"] = Relationship(back_populates="media_pref")