from datetime import datetime
import requests
import json

MLB_SCHEDULE_URL = "https://statsapi.mlb.com/api/v1/schedule?sportId=1&season=2024"


def fetch_game_data(game_pk: str) -> dict:
    """
    Récupère les données d'un match depuis l'API MLB.

    Args:
        game_pk (str): L'identifiant unique du match.

    Returns:
        dict: Les données JSON du match si la requête est réussie.
    
    Raises:
        Exception: Si la requête échoue ou que les données JSON sont invalides.
    """
    try:
        # Construire l'URL de l'API
        single_game_feed_url = f'https://statsapi.mlb.com/api/v1.1/game/{game_pk}/feed/live'
        
        # Effectuer la requête
        response = requests.get(single_game_feed_url)
        
        # Vérifier le statut HTTP
        response.raise_for_status()  # Lève une exception si le statut n'est pas 200
        
        # Charger les données JSON
        single_game_info_json = response.json()
        
        return single_game_info_json
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Erreur lors de la requête vers l'API MLB: {e}")
    except json.JSONDecodeError:
        raise Exception("Erreur lors du décodage des données JSON.")


def extract_game_summary(single_game_info_json):
    summary = []

    # Étape 1 : Extraire les informations météo
    weather_info = single_game_info_json.get("gameData", {}).get("weather", {})
    weather_summary = (
        f"Weather: {weather_info.get('condition', 'No weather info')}, "
        f"Temperature: {weather_info.get('temp', 'No temp')}°F, "
        f"Wind: {weather_info.get('wind', 'No wind info')}"
    )
    summary.append(weather_summary)

    # Étape 2 : Extraire les informations des équipes
    teams = single_game_info_json.get("gameData", {}).get("teams", {})
    home_team = teams.get("home", {}).get("name", "Unknown Home Team")
    away_team = teams.get("away", {}).get("name", "Unknown Away Team")
    summary.append(f"Teams: {home_team} (Home) vs {away_team} (Away)")

    # Étape 3 : Filtrer les événements de scoring
    play_events = single_game_info_json.get("liveData", {}).get("plays", {}).get("allPlays", [])
    scoring_events = [event for event in play_events if event['about'].get('isScoringPlay')]

    # Parcourir les événements de scoring
    for event in scoring_events:
        # Extraire les données importantes
        event_type = event['result'].get('event', 'No event')
        start_time = event['about'].get('startTime', 'No time')
        inning = event['about'].get('inning', 'No inning')
        outs = event['about'].get('outs', 'No outs')
        home_score = event['result'].get('homeScore', 0)
        away_score = event['result'].get('awayScore', 0)
        impact_level = event['about'].get('captivatingIndex', 0)

        # Infos sur le batteur et le lanceur
        batter_name = event['matchup']['batter'].get('fullName', 'Unknown Batter')
        pitcher_name = event['matchup']['pitcher'].get('fullName', 'Unknown Pitcher')

        # Formater l'heure
        time = start_time[11:16] if start_time != 'No time' else 'No time'

        # Ajouter l'événement au résumé
        if event_type == 'Home Run':
            summary.append(
                f"At {time}, {batter_name} hit a Home Run, bringing the score to {home_score}-{away_score}. "
                f"Captivating Index: {impact_level}"
            )
        elif event_type == 'Strikeout':
            summary.append(
                f"At {time}, {batter_name} struck out against pitcher {pitcher_name}. "
                f"Current score: {home_score}-{away_score}, {outs} outs in the {inning} inning."
            )
        elif event_type == 'Game Over':
            winner = 'Home' if home_score > away_score else 'Away'
            summary.append(f"Game Over: {winner} wins with a final score of {home_score}-{away_score} at {time}.")
        else:
            summary.append(
                f"At {time}, a {event_type} occurred. The score is {home_score}-{away_score} "
                f"in the {inning} inning with {outs} outs."
            )

    return summary


def get_upcoming_matches():
    """
    Récupère les matchs prévus dans les 24 prochaines heures.
    """
    # today = datetime.utcnow().date()
    # tomorrow = today + timedelta(days=30)

    # url = f"{MLB_SCHEDULE_URL}&startDate={today}&endDate={tomorrow}"
    # response = requests.get(url)

    # """
    # Récupère les matchs prévus lors de la semaine dernière.
    # """
    # # Récupérer la date d'aujourd'hui
    # today = datetime.utcnow().date()
    
    # # Calculer la date de la semaine dernière
    # last_week_start = today - timedelta(days=30)
    # last_week_end = today - timedelta(days=1)
    
    # Formatage des dates pour l'API
    # start_date = last_week_start.strftime("%Y-%m-%d")
    # end_date = last_week_end.strftime("%Y-%m-%d")
    start_date = '2024-08-01'
    end_date = '2025-03-01'

        # Récupérer la date d'aujourd'hui
    # today = datetime.utcnow().date()
    
    # # Calculer la date de 30 jours à partir d'aujourd'hui
    # next_month = today + timedelta(days=30)

    # # Formatage des dates pour l'API
    # start_date = today.strftime("%Y-%m-%d")
    # end_date = next_month.strftime("%Y-%m-%d")
    
    # Construire l'URL avec les dates calculées
    url = f"{MLB_SCHEDULE_URL}&startDate={start_date}&endDate={end_date}"
    
    response = requests.get(url)
    
    
    if response.status_code != 200:
        print("❌ Erreur lors de la récupération du calendrier MLB")
        return []

    data = response.json()
    games = []
    
    for date in data.get("dates", []):
        for game in date.get("games", []):
                    # Stocker en datetime complet
            game_datetime = datetime.strptime(game['gameDate'], "%Y-%m-%dT%H:%M:%SZ")


            
            # Extraire la date pour les comparaisons
            game_date = game_datetime.date()

            games.append({
                "game_id": str(game["gamePk"]),
                "home_team": game["teams"]["home"]["team"]["name"],
                "away_team": game["teams"]["away"]["team"]["name"],
                "home_team_id": str(game["teams"]["home"]["team"]["id"]),
                "away_team_id": str(game["teams"]["away"]["team"]["id"]),
                "game_time": game_date,  # Heure UTC
            })

    # print(games)
    return games

def get_match_highlights(game_pk: str):
    """
    Combine les étapes pour récupérer et analyser les données d'un match.
    """
    game_data = fetch_game_data(game_pk)
    # highlights = extract_highlights(game_data)
    highlights = extract_game_summary(game_data)

    return highlights