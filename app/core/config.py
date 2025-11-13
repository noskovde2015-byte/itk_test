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
    url: str = 'sqlite+aiosqlite:///./test.db'
    echo: bool = False
    echo_pool: bool = False
    max_overflow: int = 10
    pool_size: int = 50


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DataBaseConfig = DataBaseConfig()


settings = Settings()
