from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    app_name: str = "Estimador-CAG"
    openai_api_key: str
    anthropic_api_key: str
    llm_provider: str
    llm_model: str
    app_env: str
    log_level: str
    items_per_user: int = 50
    timeout: int
    max_retries: int


settings = Settings()


def get_settings() -> Settings:
    return settings

##if __name__ == "__main__":
#    for field_name, value in settings.model_dump().items():
#        print(f"{field_name} = {value}")