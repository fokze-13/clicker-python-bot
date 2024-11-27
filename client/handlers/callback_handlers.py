from aiogram.types import CallbackQuery
from aiogram import Router
from aiogram import F
from client.keyboards.client_inline_keyboards import start_keyboard_button, clicker_keyboard
from client.lexicons import lexicon_ru

router: Router = Router()

@router.callback_query(F.data == start_keyboard_button.callback_data)
async def start_callback(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(lexicon_ru.clicker_message,
                                  reply_markup=clicker_keyboard)

