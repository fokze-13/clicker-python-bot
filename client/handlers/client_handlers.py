from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from client.lexicons import lexicon_ru
from client.keyboards import client_inline_keyboards
import requests
from client.config import Config, get_config
import json

config: Config = get_config()

router: Router = Router()


@router.message(CommandStart())
async def start(message: Message):
    response = requests.post(
        f"{config.api_url}/user/new?user_id={message.from_user.id}")

    if response.status_code == 200:
        await message.answer(lexicon_ru.start_message, reply_markup=client_inline_keyboards.start_keyboard)
