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
    - Créer un profils utilisateur (inscription par mail / google auth)
    - Ajouter des préférences ( sélectionner une équipe, un joueur, un type de contenue favoris parmis texte, vidéo, audio)

Collecte de données:
    - Récupérer les stats de chaque match, les commentaires, les points forts.
    Les filtrer en fonction des préférences utilisateur.

Traitement des données:
    - Générer automatiquement des résumés adaptés aux préférences utilisateurs.
    - Vidéo: compilations des meilleurs moments.
    - Audio: synthèse vocale pour récapituler les statistiques et commentaires.
    - Texte: résumé écrit des événements clés.

Multilingue:
    - Traduire et adapter les contenus pour les langues cibles.

Notification:
    - Les utilisateurs reçoivent (après chaque match ou 1 fois par semaine) les temps forts via un mail contenant un lien de redirection vers le résumé.

Interface utilisateur:
    - Les utilisateurs ont accès à une interface multilingue accessible sur mobile et desktop qui leur permet de paramétrer leurs préférences, visualiser leur contenus.

## Architecture et technologies utilisées
Backend : FastAPI pour les endpoints API.
Traitement de données : pandas pour manipuler les données MLB.
Base de données : MySQL (ou MongoDB si utilisé).
Machine Learning : TensorFlow pour générer les résumés.
Hébergement : Google Cloud pour le déploiement (Cloud Run).
Frontend : Framework choisi pour l’interface utilisateur ReactJS.

## Mise en place et exécution locale
installation: 
    1.Clonez le dépôt:
    ```
        git clone https://github.com/sofiene-Ben/mlb_highlights.git
        cd projet
    ```
    
    2.Installez les dépendances:
    ```
        pip install -r requirements.txt
    ```

    3.Lancer le serveur backend:
    ```
        uvicorn app.main:app --reload
```

    4.Lancer le frontend:
    ```
        npm run
    ```

## Deploiement



## Sources de données




## Apprentissages et défis rencontrés



## Structure du projet
```
projet/
├── app/                # Dossier principal pour le backend FastAPI
│   ├── main.py         # Point d'entrée de l'API
│   ├── models/         # Modèles de données
│   ├── routes/         # Endpoints API
│   ├── services/       # Logique métier
├── data/               # Données sources (si applicable)
├── frontend/           # Interface utilisateur (si applicable)
├── tests/              # Tests unitaires et d'intégration
├── Dockerfile          # Conteneurisation du projet
├── requirements.txt    # Dépendances Python
└── README.md           # Documentation du projet
```
## Contribuer


## Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.