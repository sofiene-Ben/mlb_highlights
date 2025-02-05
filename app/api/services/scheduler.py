from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from app.api.services.match_service import get_upcoming_matches
from app.api.services.summary_service import generate_and_store_summaries
from app.infrastructure.database.dbchallenge import get_session
from app.api.repositories.game_repository import get_game_summary_from_db
import threading


scheduler = BackgroundScheduler()

def schedule_match_summaries():
    """
    Récupère les matchs du mois et planifie la génération des résumés 3 heures après le début de chaque match.
    Si la génération est manquée de plus de 6 heures, elle est effectuée immédiatement.
    """
    upcoming_matches = get_upcoming_matches()

    if not upcoming_matches:
        print("⚠️ Aucun match trouvé pour le mois en cours.")
        return
    
    for match in upcoming_matches:
        game_id = match["game_id"]
        home_team = match["home_team"]
        away_team = match["away_team"]
        home_team_id = match['home_team_id']
        away_team_id = match['away_team_id']
        # match_start_time = datetime.strptime(match["game_time"], "%Y-%m-%dT%H:%M:%SZ")  # Convertir en objet datetime UTC
        match_start_time = datetime.combine(match["game_time"], datetime.min.time()) 

        # 📅 Ajouter un délai de 3 heures après le début du match
        summary_time = match_start_time + timedelta(hours=3)
        current_time = datetime.utcnow()

        # Vérifier si les résumés existent déjà dans la base de données
        db = next(get_session())  # ✅ Utilisation correcte du générateur

        existing_summary = get_game_summary_from_db(game_id, db)
        # print(f"existing_summary : {existing_summary}")
        if existing_summary:
            print(f"✅ Résumés déjà présents pour le match {game_id}, aucune génération nécessaire.")
            # return True
        else:
            # Vérifier si le résumé est en retard de plus de 6 heures
            if current_time > summary_time + timedelta(hours=6):
                print(f"⚠️ Génération manquée pour le match {game_id} ({home_team} vs {away_team}). Génération immédiate.")
                # Appeler la fonction pour générer et stocker les résumés immédiatement
                # generate_and_store_summaries(game_id, home_team, away_team)
                generate_and_store_summaries(game_id=game_id, game_date=match_start_time, home_team=home_team, away_team=away_team, home_team_id=home_team_id, away_team_id=away_team_id)

            else:
                # Planifier la génération du résumé si ce n'est pas en retard de plus de 6 heures
                scheduler.add_job(
                    generate_and_store_summaries,
                    'date',
                    run_date=summary_time,
                    args=[game_id, home_team, away_team],
                    id=f"summary_{game_id}",
                    misfire_grace_time=3600  # Le job sera exécuté même si légèrement en retard
                )
                print(f"📅 Résumé programmé pour {game_id} ({home_team} vs {away_team}) à {summary_time}.")


def start_scheduler():
    """
    Démarre le planificateur dans un thread séparé pour éviter qu'il ne bloque le serveur.
    """
    # Planifier les matchs dès le démarrage
    schedule_match_summaries()

    def run_scheduler():
        scheduler.start()
        print("✅ Scheduler démarré.")

    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()


