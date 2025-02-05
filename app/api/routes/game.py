from fastapi import APIRouter, HTTPException
from app.domain.entities.Users import Users
from app.domain.entities.GameSummary import GameSummary
from app.api.utils.api_client import fetch_and_process_matches
from app.api.services.match_service import get_match_highlights
from app.api.services.summary_service import generate_game_summary
from app.infrastructure.database.dbchallenge import get_session
from app.api.auth.security import get_current_active_user
from sqlmodel import Session, select

game_router = APIRouter(prefix="/api")

@game_router.get("/matches/{game_id}/highlights")
async def get_highlights(game_id: str):
    """
    Endpoint pour récupérer les moments forts d'un match.
    """
    try:
        highlights = get_match_highlights(game_id)
        return {"success": True, "highlights": highlights}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

# router = APIRouter()

@game_router.get("/game/highlight/{game_pk}")
async def generate_highlight_summary(game_pk: str, user_favorite_team: str):
    """
    Génère un résumé d'un match en récupérant les données via l'API MLB.

    Args:
        game_pk (str): Identifiant unique du match.
        user_favorite_team (str): Équipe favorite de l'utilisateur.

    Returns:
        dict: Résumé généré du match.
    """
    try:
        # Récupérer les highlights du match
        highlights = get_match_highlights(game_pk)

        # Vérifier la validité des données
        # if not highlights or not highlights.get("success"):
        if not highlights:
            raise ValueError("Impossible de récupérer les moments forts du match.")

        # Appeler le service Generative AI pour générer le résumé
        summary = generate_game_summary(
            highlights, user_favorite_team
        )
        return {"success": True, "summary": summary}
        # return {"success": True, "summary": highlights}


    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la génération du résumé : {str(e)}")
    


@game_router.get("/test/generate_summaries")
def test_generate_summaries():
    """
    Endpoint pour tester la génération de résumés manuellement avant d'activer le scheduler.
    """
    try:
        # Appeler la fonction manuellement pour tester son fonctionnement
        fetch_and_process_matches()  # Assurez-vous d'utiliser 'await' si c'est une fonction asynchrone
        return {"success": True, "message": "Résumés générés et stockés avec succès."}
    except Exception as e:
        return {"success": False, "message": str(e)}
    

from fastapi import APIRouter, Depends, HTTPException
@game_router.get("/summaries/all")
def get_all_summaries(session: Session = Depends(get_session)) -> list:
    """
    Récupère tous les résumés des matchs dans la base de données.
    """
    summaries = session.query(GameSummary).all()
    if not summaries:
        raise HTTPException(status_code=404, detail="Aucun résumé trouvé")
    return summaries


@game_router.get("/favorite-team/articles/")
async def get_favorite_team_articles(
    current_user: Users = Depends(get_current_active_user),
    session: Session = Depends(get_session)
):
    # Vérifier si l'utilisateur a une équipe favorite
    if current_user.team_fav:
        # Récupérer tous les articles associés à l'équipe favorite
        articles = session.exec(
            select(GameSummary).where(GameSummary.team_id == str(current_user.team_fav))
        ).all()
        
        if articles:
            return {"articles": articles}
        else:
            raise HTTPException(status_code=404, detail="No articles found for the favorite team")
    
    raise HTTPException(status_code=404, detail="User has no favorite team")


@game_router.get("/favorite-team/articles/{article_id}", response_model=GameSummary)
def get_article(article_id: int, session: Session = Depends(get_session)):
    article = session.exec(select(GameSummary).where(GameSummary.id == article_id)).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article
