from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data.database import Database
from app.data.data import film_callback


def get_films():
    keyboard = InlineKeyboardMarkup()
    for film in Database.get_films():
        button = InlineKeyboardButton(
            text=film['name'],
            callback_data=film_callback.new(id=film['id'],
                                            viewed=film['viewed'],
                                            name=film['name'],
                                            action='show')
        )
        keyboard.add(button)
    return keyboard


def get_film_menu(id, viewed, name):
    viewed = bool(viewed)
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text=name, callback_data=name),
                 InlineKeyboardButton(text='viewed' if viewed else 'not viewed',
                                      callback_data=film_callback.new(id=id,
                                                                      viewed='1' if viewed else '',
                                                                      name=name,
                                                                      action='change')))
    return keyboard

