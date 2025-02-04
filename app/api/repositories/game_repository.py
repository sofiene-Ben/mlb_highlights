from sqlmodel import Session, select, or_
from datetime import datetime
from infrastructure.database.dbchallenge import engine
from domain.entities.GameSummary import GameSummary

def store_game_summary(
    game_id: str,
    game_date: datetime,
    team_id: str,
    team_name: str,
    is_home_team: bool,
    text_summary: str = None,
    video_summary: str = None,
    audio_summary: str = None,
    opponent_team: str = None
):
    """
    Enregistre ou met à jour un résumé de match pour une équipe spécifique.
    """

    with Session(engine) as session:
        # Vérifier si un résumé existe déjà pour cette équipe et ce match
        statement = select(GameSummary).where(
            or_(
                (GameSummary.game_id == game_id) & (GameSummary.team_id == team_id),
                (GameSummary.team_id == team_id) & (GameSummary.game_date == game_date)
            )
        )
        
        # Exécuter la requête pour récupérer les résultats
        existing_summary = session.exec(statement).all()


        if existing_summary:
            # Accéder au premier (et probablement unique) résumé trouvé
            record = existing_summary[0]
            record.text_summary = text_summary or record.text_summary
            record.video_summary = video_summary or record.video_summary
            record.audio_summary = audio_summary or record.audio_summary
            record.created_at = datetime.utcnow()  # 
        else:
            # Insérer un nouveau résumé
            new_summary = GameSummary(
                game_id=game_id,
                game_date=game_date,
                team_id=team_id,
                team_name=team_name,
                is_home_team=is_home_team,
                text_summary=text_summary,
                video_summary=video_summary,
                audio_summary=audio_summary,
                perspective="home" if is_home_team else "away",
                opponent_team=opponent_team,
                created_at=datetime.utcnow(),
            )
            session.add(new_summary)

        session.commit()
        print(f"✅ Résumé enregistré pour {team_name} ({'domicile' if is_home_team else 'extérieur'}).")

def get_game_summary_from_db(game_id: str, db: Session) -> dict:
    """
    Récupère les résumés du match à partir de la base de données.
    """
    try:
        # Récupérer les deux résumés du match
        statement = select(GameSummary).where(GameSummary.game_id == game_id)
        summaries = db.exec(statement).all()

        if not summaries:
            print(f"❌ Aucun résumé trouvé pour le match {game_id}.")
            return None

        # Organiser les résumés par équipe
        game_summaries = {}
        for summary in summaries:
            game_summaries[summary.perspective] = {
                "team_name": summary.team_name,
                "text_summary": summary.text_summary,
                "video_summary": summary.video_summary,
                "audio_summary": summary.audio_summary
            }

        print(f"✅ Résumé du match {game_id} récupéré avec succès.")
        return game_summaries

    except Exception as e:
        print(f"❌ Erreur lors de la récupération du résumé du match {game_id} : {e}")
        return None
