from fastapi import FastAPI
from api.routes.hero import hero_router 
from api.routes.user import user_router
from api.routes.auth import auth_router
from api.routes.game import game_router
from api.routes.preferences import pref_router
from middlewares.corsMiddleware import cors_regex_middleware
from infrastructure.database.dbchallenge import  create_db_and_tables
from api.services.scheduler import start_scheduler

app = FastAPI()

# Middleware appliqué à l'objet app donc à l'application pour les échanges front/back
app.middleware("http")(cors_regex_middleware)

# Inclure les routes
app.include_router(hero_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(pref_router)
app.include_router(game_router)

import threading
@app.on_event("startup")
def on_startup():
    # Création des tables dans la base de données
    create_db_and_tables()
    # Démarre le scheduler dans un thread séparé
    threading.Thread(target=start_scheduler, daemon=True).start()
    
