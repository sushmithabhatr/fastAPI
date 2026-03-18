from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    #DATABASE_URL: str = "postgresql://user:password@db:5432/app"
    DATABASE_URL: str = "sqlite:///./test.db"
    SECRET_KEY: str = "secret"
    ALGORITHM: str = "HS256"

settings = Settings()

