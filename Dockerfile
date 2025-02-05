# Utiliser une image de base légère avec Python
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système nécessaires (optionnel mais recommandé)
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Copier les fichiers nécessaires pour installer les dépendances
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du projet
COPY . .

# Exposer le port utilisé par FastAPI (Cloud Run attend 8080)
EXPOSE 8080

# Définir la variable d'environnement pour le port (Cloud Run définit automatiquement PORT=8080)
ENV PORT=8080

# Lancer l’application avec Uvicorn sur le bon port
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
