from aiogram import types
from aiogram.dispatcher import FSMContext

from app import dp
from app.keyboards.default.media import get_menu
from app.keyboards.inline.media import get_films as films
from app.keyboards.default.media import get_films_menu
from app.data.state import MenuState


@dp.message_handler(lambda message: message.text == 'Media', state=MenuState.menu)
async def media_menu(message: types.Message, state: FSMContext):
    await state.set_state(MenuState.media_menu)
    await message.answer('Choose option', reply_markup=get_menu())


@dp.message_handler(lambda message: message.text == 'Films', state=MenuState.media_menu)
async def films_menu(message: types.Message, state: FSMContext):
    await state.set_state(MenuState.films)
    await message.answer('Ok', reply_markup=get_films_menu())



# async def get_films():
#     await message.answer('You\'r films', reply_markup=films())