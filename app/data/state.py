from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class MenuState(StatesGroup):
    menu = State()
    media_menu = State()
    films = State()
    books = State()
    notes_menu = State()