from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_menu():
    films_btn = KeyboardButton('Films')
    books_btn = KeyboardButton('Books')

    menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    menu.add(films_btn, books_btn)

    return menu

def get_films_menu():
    add_btn = KeyboardButton('Add film')
    back_btn = KeyboardButton('Back')

    menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    menu.add(add_btn, back_btn)

    return menu
