from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # 1. Project Metadata
    PROJECT_NAME: str = "FastAPI Product API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # 2. Database Configuration
    # Fallback values are provided, but these should be set in .env
    POSTGRES_USER: str = "root"
    POSTGRES_PASSWORD: str = "root"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str = "fastapi-demo_db"

    # Computed Property for the Full Connection String
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    # 3. Security (Example)
    # SECRET_KEY: str = "super-secret-key"

    # Tell Pydantic to read from a .env file
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

# Instantiate the settings object to be used across the app
settings = Settings()
