from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from client.lexicons import lexicon_ru

start_button = InlineKeyboardButton(text=lexicon_ru.start_button, callback_data="start")
start_keyboard = InlineKeyboardMarkup(inline_keyboard=[[start_button]])
