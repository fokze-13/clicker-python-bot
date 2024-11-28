from dataclasses import dataclass
from environs import Env


@dataclass()
class Config:
    bot_token: str
    api_url: str

def get_config() -> Config:
    env = Env()
    env.read_env()

    return Config(
        bot_token=env("BOT_TOKEN"),
        api_url=env("API_URL")
    )
