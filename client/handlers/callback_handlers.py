from aiogram.types import CallbackQuery
from aiogram import Router
from aiogram import F
from client.keyboards.client_inline_keyboards import start_keyboard_button, clicker_keyboard
from client.lexicons import lexicon_ru
import requests
from client.config import Config, get_config

config: Config = get_config()

router: Router = Router()

@router.callback_query(F.data == start_keyboard_button.callback_data)
async def start_callback(callback: CallbackQuery):
    await callback.message.delete()
    response = requests.get(
        f"{config.api_url}/clicks/get?user_id={callback.from_user.id}"
    )

    if response.status_code == 200:
        await callback.message.answer(lexicon_ru.clicker_message.format(clicks=response.json()),
                                        reply_markup=clicker_keyboard)

