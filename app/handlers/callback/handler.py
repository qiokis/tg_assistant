from aiogram import types

from app import dp
from app.data.database import Database
from app.data.state import MenuState
from app.data.data import film_callback
from app.keyboards.inline.media import get_film_menu


@dp.callback_query_handler(film_callback.filter(action=['show']), state=MenuState.films)
async def get_film(call: types.CallbackQuery, callback_data: dict):
    await call.message.answer('Ok', reply_markup=get_film_menu(callback_data['id'],
                                                               callback_data['viewed'],
                                                               callback_data['name']))


@dp.callback_query_handler(film_callback.filter(action=['change']), state=MenuState.films)
async def get_film(call: types.CallbackQuery, callback_data: dict):
    viewed = bool(callback_data['viewed'])
    Database.change_film(callback_data['id'], 'viewed', not viewed)
    await call.message.answer('As you wish mi lord', reply_markup=get_film_menu(callback_data['id'],
                                                                                not viewed,
                                                                                callback_data['name']))
