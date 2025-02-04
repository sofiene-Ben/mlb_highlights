from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class GameSummary(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    game_id: str = Field(index=True, nullable=False)  # Suppression de unique=True
    game_date: datetime = Field(nullable=True)
    team_id: str = Field(index=True, nullable=False)  # Suppression de unique=True
    team_name: str = Field(nullable=False, max_length=100)
    is_home_team: bool = Field(nullable=False)  # Correction max_length supprimé
    perspective: str = Field(nullable=False, max_length=10)  # "home" ou "away"
    text_summary: Optional[str] = Field(default=None, nullable=True)
    video_summary: Optional[str] = Field(default=None, nullable=True)
    audio_summary: Optional[str] = Field(default=None, nullable=True)
    opponent_team: Optional[str] = Field(default=None, nullable=True, max_length=100)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        unique_together = ("game_id", "team_id")  # Clé composite