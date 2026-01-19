from pydantic import BaseSettings

class Settings(BaseSettings):
    SERVICE_NAME: str = "python-microservice"

settings = Settings()
