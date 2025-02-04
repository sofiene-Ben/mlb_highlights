from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
hashed_password = pwd_context.hash("secretpassword")  # Remplace par le mot de passe réel
print(hashed_password)