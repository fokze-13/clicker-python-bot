from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from client.lexicons import lexicon_ru

start_keyboard_button = InlineKeyboardButton(text=lexicon_ru.start_button, callback_data="start")
start_keyboard = InlineKeyboardMarkup(inline_keyboard=[[start_keyboard_button]])

clicker_keyboard_button = InlineKeyboardButton(text=lexicon_ru.clicker_button, callback_data="click")
clicker_keyboard = InlineKeyboardMarkup(inline_keyboard=[[clicker_keyboard_button]])
