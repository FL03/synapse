"""
    Appellation: settings
    Contributors: FL03 <jo3mccain@icloud.com>
    Description:
        ... Summary ...
"""
from functools import lru_cache

from pydantic import BaseModel, BaseSettings


class Server(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8080
    reload: bool

    def from_mode(self, stage: str = "development"):
        if "dev" in stage or "development" == stage:
            self.reload = True
        else:
            self.reload = False


class Settings(BaseSettings):
    db_uri: str = "sqlite://:memory:"
    dev_mode: bool = False
    domain: str = "http://localhost:8080"
    openai_api_key: str
    server: Server = Server(reload=dev_mode)
    secret_token: str
    stripe_public_key: str
    stripe_secret_key: str
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

        @classmethod
        def customise_sources(cls, init_settings, env_settings, file_secret_settings):
            return init_settings, env_settings, file_secret_settings


@lru_cache
def settings() -> Settings:
    return Settings()
