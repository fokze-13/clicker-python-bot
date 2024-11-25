from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from client.lexicons import lexicon_ru
from client.keyboards import client_inline_keyboards

router: Router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(lexicon_ru.start_message, reply_markup=client_inline_keyboards.start_keyboard)
