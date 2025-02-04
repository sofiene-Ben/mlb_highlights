# mlb-highlight
Table des matières
1. Introduction
2. Fonctionnalités principales
3. Architecture et technologies utilisées
4. Mise en place et exécution locale
5. Déploiement
6. Sources de données
7. Apprentissages et défis rencontrés
8. Structure du projet
9. Contribuer
10. Licence



## Introduction
"Personalized Fan Highlights" est une application innovante permettant aux fans de baseball de suivre leurs équipes et joueurs préférés et de recevoir des résumés personnalisés sous forme de textes, audios et vidéos, accessibles en anglais, espagnol et japonais.

## Fonctionnalités principales
Gestion utilisateur:
    - Créer un profils utilisateur 
    - Ajouter des préférences ( sélectionner une équipe, un joueur, un type de contenue favoris parmis texte, vidéo, audio)

Collecte de données:
    - Récupérer les stats de chaque match, les commentaires, les points forts.
    Les filtrer en fonction des préférences utilisateur.

Traitement des données:
    - Générer automatiquement des résumés adaptés aux préférences utilisateurs.
    - Texte: résumé écrit des événements clés.

Multilingue:


Notification:


Interface utilisateur:
    - Les utilisateurs ont accès à une interface accessible sur mobile et desktop qui leur permet de paramétrer leurs préférences, visualiser leur contenus.

## Architecture et technologies utilisées
Backend : FastAPI pour les endpoints API.
Traitement de données : pandas pour manipuler les données MLB.
Base de données : Postgres.
Hébergement : Google Cloud pour le déploiement (Cloud Run).
Frontend : Framework choisi pour l’interface utilisateur ReactJS.

## Mise en place et exécution locale
installation: 
    1.Clonez le dépôt:
        git clone https://github.com/sofiene-Ben/mlb_highlights.git
        cd mlb_highlights
    
    2.Installez les dépendances:
        pip install -r requirements.txt

    3.Lancer le serveur backend:
        uvicorn app.main:app --reload

    4.Lancer le frontend:
        npm run start

## Deploiement



## Sources de données




## Apprentissages et défis rencontrés



## Structure du projet
```
projet/
├── app/
│   ├── api/
│   │   ├── auth/
│   │   │   └── security.py          # Gestion de l'authentification et des tokens
│   │   ├── repositories/
│   │   │   └── game_repository.py   # Accès aux données des matchs
│   │   ├── routes/
│   │   │   └── auth.py             
│   │   │   └── game.py             
│   │   │   └── hero.py              
│   │   │   └── preferences.py          
│   │   │   └── user.py              
│   │   ├── services/
│   │   │   └── match_service.py   
│   │   │   └── schelduer.py   
│   │   │   └── summary_service.py   
│   │   ├── utils/
│   │   │   └── api_client.py        # Client pour appels à des API externes
│   │
│   ├── domain/
│   │   ├── entities/
│   │   │   └── GameSummary.py             # Modèle d'entité utilisateur
│   │   │   └── Hero.py 
│   │   │   └── Users.py 
│   │   ├── schemas/
│   │   │   └── auth.py              # Schémas de validation pour l'authentification
│   │
│   ├── infrastructure/
│   │   ├── config/
│   │   │   └── app.py               # Configuration globale de l'application
│   │   ├── database/
│   │   │   └── dbchallenge.py       # Connexion à la base de données
│   │
│   ├── middlewares/
│   │   ├── corsMiddleware.py        # Middleware pour la gestion du CORS
│   │
│   ├── main.py                      # Point d'entrée de l'API FastAPI
│   ├── LICENSE                      # Licence du projet
│   ├── README.md                    # Documentation du projet
```
## Contribuer


## Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.