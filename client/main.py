from aiogram import Bot, Dispatcher
import logging
from aiogram.client.default import DefaultBotProperties
from config import get_config, Config
import asyncio


config: Config = get_config()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(config.bot_token, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
