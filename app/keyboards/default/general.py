from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_menu():
    media_btn = KeyboardButton('Media')
    notes_btn = KeyboardButton('Notes')

    menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    menu.add(media_btn, notes_btn)

    return menu
