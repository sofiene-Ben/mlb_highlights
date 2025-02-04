import google.generativeai as genai
from infrastructure.config.app import settings
from datetime import datetime
from api.services.match_service import get_match_highlights
from api.repositories.game_repository import store_game_summary


# Configuration de l'API Generative AI
genai.configure(api_key=settings.generative_ai_api_key)


def generate_game_summary(highlights, user_favorite_team):
    """
    Génère un résumé narratif détaillé d'un match de baseball à partir des highlights.

    Args:
        highlights (list): Liste des faits marquants d'un match.
        user_favorite_team (str): Équipe favorite de l'utilisateur.

    Returns:
        str: Résumé généré du match.
    """
    try:
                # Vérifie que highlights est bien une liste
        if not isinstance(highlights, list):
            raise Exception("Les highlights doivent être une liste.")
        
        # Concatène les éléments de la liste en une chaîne
        # combined_highlights = " ".join(highlights)

        # Construire le prompt à partir des données fournies
        game_prompt = f"""
        Agis comme un journaliste sportif avec une approche unique et personnalisée. Ton objectif est d’écrire un résumé captivant et varié d’un match de baseball, en mettant en lumière les moments importants tout en prenant en compte les préférences de l’utilisateur.
        Fais en sorte que chaque résumé soit distinct, en utilisant des descriptions imaginatives, des métaphores, et des émotions qui vont au-delà des faits bruts. 
        Rédige un résumé détaillé avec les points suivants en tête :

        - Rédige une introduction vivante et originale qui capte l’essence du match, les enjeux et l’ambiance. N’hésite pas à surprendre par un angle inattendu.
        - Organise les moments clés du match d’une manière originale, que ce soit par l’intensité, la surprise, ou l’élément narratif qui se dégage de l’histoire du match.
        - Mettez en lumière les héros du match, mais également les moments où les joueurs ont montré une résilience ou une créativité particulières. 
        - Prends en compte l’équipe favorite de l’utilisateur : {user_favorite_team}, et construit un fil narratif qui la met en valeur sans oublier de nuancer le reste du match.
        - Conclus par une réflexion sur les implications du match, mais aussi en jetant un regard plus créatif sur l’avenir des équipes, de la saison ou de la rivalité.

        Rappelle-toi de varier les métaphores et d’apporter de la profondeur à chaque événement. Les résumés doivent toujours être captivants et surprenants, mais éviter les répétitions.
        ne fait pas toujours les meme debut de resumer.
        je ne veux voir aucune contenant "[Nom d'utilisateur]"

        si les donnees du match n'existe pas donne un message de resumer de match non disponible
        toute tes reponses doivent etre en anglais.

        Données importantes du match :
        """
        #         Comporte toi comme un redacteur sportif travaillant pour une plateforme, qui propose des resumer personnaliser pour chacun de ses utilisateur.
        # Ton role est d'ecrire un article qui resume de façon personnaliser des highlight d'un match de baseball en fonction des preferences de l'utilisateur.
        # Rédige un résumé narratif détaillé d’un match de baseball en utilisant les informations suivantes. 
        # Le résumé doit être captivant, mettre en avant les moments clés, les performances des joueurs, et inclure une progression dramatique. 
        # Utilise un ton professionnel mais vivant, comme celui d’un commentateur sportif ou d’un journaliste.
        # Veille a prendre en compte l'equipe favorite du jouer afin de tourner le resumer en sa faveur.

        # Données importantes du match :
        # Ajouter les highlights au prompt
        for highlight in highlights:
            game_prompt += f"- {highlight}\n"
        
        # Ajouter des consignes pour la génération
       # game_prompt += f"""
        # Consignes :
        # - Commence par une introduction captivante présentant les équipes, l'enjeu du match, et l'ambiance générale.  (tu n'es pas obliger de mettre la vitesse du vents)
        # - Décris les moments marquants du match dans l’ordre chronologique ou selon leur importance.
        # - Mets en avant les joueurs clés et leurs performances individuelles.
        # - Tourne le résumé en faveur de l'équipe favorite de l'utilisateur : {user_favorite_team}.
        # - Conclus avec une analyse de l'impact de ce match sur la saison ou la rivalité entre les équipes.
        # - Utilise un style dynamique et fluide, en évitant les listes sèches et en favorisant des descriptions imagées.
        # """

        # Configurer le modèle de génération
        generation_config = {
            "temperature": 1.2,
            "top_p": 0.95,
            "top_k": 50,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        model = genai.GenerativeModel(
          model_name="gemini-1.5-pro",
          generation_config=generation_config,
        )

        chat_session = model.start_chat(
          history=[
          ]
        )
        
        response = chat_session.send_message(game_prompt)
        return response.text

    except Exception as e:
        raise Exception(f"Erreur lors de la génération du résumé : {e}")
    
  
def generate_and_store_summaries(game_id: str, game_date: datetime, home_team: str, away_team: str, home_team_id: str, away_team_id: str):
    """
    Récupère les highlights et génère les résumés des deux équipes.
    """
    try:
        
        highlights = get_match_highlights(game_id)
        # print(f"🎥 Highlights récupérés pour {game_id}: {type(highlights)} - {highlights}")  # <-- Debug

        # print(highlights)

        # if not highlights.get("success"):
        if not highlights:

            print(f"⚠️ Pas de highlights pour {game_id}, on réessaye plus tard.")
            return False

        home_summary_text = generate_game_summary(highlights, home_team)
        away_summary_text = generate_game_summary(highlights, away_team)
        # print(f"📝 Résumé Home : {home_summary_text}")  # <-- Debug
        # print(f"📝 Résumé Away : {away_summary_text}")  # <-- Debug

        # Utilisation de store_game_summary() pour insérer les résumés
        store_game_summary(
            game_id=game_id, game_date=game_date, team_id=home_team_id, team_name=home_team, is_home_team=True,
            text_summary=home_summary_text, opponent_team=away_team
            # , home_video_summary, home_audio_summary
        )
        store_game_summary(
            game_id=game_id, game_date=game_date, team_id=away_team_id, team_name=away_team, is_home_team=False,
            text_summary=away_summary_text, opponent_team=home_team
            # , away_video_summary, away_audio_summary
        )


        print(f"✅ Résumés générés et enregistrés pour le match {game_id}")
        return True

    except Exception as e:
        # print(f"❌ Erreur lors de la génération des résumés highlights : {e}")
        print(f"❌ Erreur lors de la génération des résumés highlights:")
        # print(f"Type d'objet highlight: {type(highlights)}")
        # print(f"Contenu de highlights: {highlights}")
        # print(f"Message d'erreur: {e}")
        return False

