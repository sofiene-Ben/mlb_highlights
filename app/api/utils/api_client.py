from datetime import datetime
from app.infrastructure.database.dbchallenge import get_session
from app.api.services.match_service import get_upcoming_matches
from app.api.services.summary_service import generate_and_store_summaries
from app.api.repositories.game_repository import get_game_summary_from_db


def fetch_and_process_matches():
    """
    Récupère les horaires des matchs et génère les résumés des deux équipes.
    """
    print(f"Fetching and processing matches at {datetime.now()}")
    
    # Récupère les matchs à venir
    upcoming_matches = get_upcoming_matches()
    
    if not upcoming_matches:
        print("No upcoming matches found.")
        return
    
    db = next(get_session())  # ✅ Utilisation correcte du générateur

    for match in upcoming_matches:
        try:
            game_id = match['game_id']
            home_team = match['home_team']
            away_team = match['away_team']
            home_team_id = match['home_team_id']
            away_team_id = match['away_team_id']
            # game_date = match['game_date']

            # print(f"Processing game {game_id}")
            # print(f"home:  {away_team}")
            # print(f"away: {home_team}")

                    # Stocker en datetime complet
            game_datetime = datetime.strptime(match['game_date'], "%Y-%m-%d %H:%M:%S")
            
            # Extraire la date pour les comparaisons
            game_date = game_datetime.date()

            # Vérifier si les résumés existent déjà dans la base de données
            existing_summary = get_game_summary_from_db(game_id, db)
            # print(f"existing_summary : {existing_summary}")
            if existing_summary:
                print(f"✅ Résumés déjà présents pour le match {game_id}, aucune génération nécessaire.")
                # return True
            else:
                generate_and_store_summaries(game_id, game_date, home_team, away_team, home_team_id, away_team_id)


        except Exception as e:
            print(f"Error processing match {game_id}: {e}")

