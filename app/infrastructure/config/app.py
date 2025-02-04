from dotenv import load_dotenv
import os

load_dotenv()

class Settings():
    database_url: str = os.getenv("DATABASE_URL")
    secret_key: str = os.getenv("SECRET_KEY")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    refresh_token_expire_minutes: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES", 1440))
    algorithm: str = str(os.getenv("ALGORITHM", 'HS256'))
    cors: str = str(os.getenv("CORS", r'https?://(localhost|127\.0\.0\.1|0\.0\.0\.0)(:\d+)?'))
    generative_ai_api_key: str = str(os.getenv("GENERATIVE_AI_API_KEY"))    

settings = Settings()