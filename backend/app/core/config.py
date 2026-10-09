from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "NASA Microgravity Combustion Data Analysis"
    database_url: str = "sqlite:///./dev.db"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
