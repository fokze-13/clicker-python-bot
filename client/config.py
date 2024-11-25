from dataclasses import dataclass
from environs import Env


@dataclass()
class Config:
    bot_token: str

def get_config():
    env = Env()
    env.read_env()

    return Config(
        bot_token=env("BOT_TOKEN")
    )
