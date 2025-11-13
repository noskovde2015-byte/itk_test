from pathlib import Path

from pydantic import BaseModel, AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    port: int = 8000
    host: str = "0.0.0.0"




class ApiPrefix(BaseModel):
    prefix: str = "/api"
    users: str = "/users"



class DataBaseConfig(BaseModel):
    url: AnyUrl
    echo: bool = False
    echo_pool: bool = False
    max_overflow: int = 10
    pool_size: int = 50


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / ".env",
        case_sensitive=False,
        env_file_encoding="utf-8",
        env_prefix="TEST__",
        env_nested_delimiter="__"
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DataBaseConfig


settings = Settings()
