from environs import Env
from dataclasses import dataclass

@dataclass
class Config:
    db_url: str
    db_user: str
    db_password: str

def get_config() -> Config:
    env = Env()
    env.read_env()

    return Config(
        db_url=env("DB_URL"),
        db_user=env("DB_USER"),
        db_password=env("DB_PASSWORD")
    )
