import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

#hack to get around sqlalchemy needing postgresql://
db_uri = os.getenv("DATABASE_URL")  # or other relevant config var
if db_uri and db_uri.startswith("postgres://"):
    db_uri = db_uri.replace("postgres://", "postgresql://", 1)

class Settings:
    PROJECT_TITLE: str = "Stuff API"
    PROJECT_VERSION: str = "0.1.0"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL : str = db_uri if db_uri else f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SECRET_KEY :str = os.getenv("SECRET_KEY")   #new
    ALGORITHM = "HS256"                         #new
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  #in mins  #new

settings = Settings()