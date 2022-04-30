from app import dp
from aiogram import types
from aiogram.dispatcher import FSMContext

from app.data.state import MenuState
from app.keyboards.default.general import get_menu


@dp.message_handler(commands='start', state='*')
async def handler(message: types.Message, state: FSMContext):
    if message.from_user['id'] == 871212687:
        await state.set_state(MenuState.menu)
        await message.answer('Ok', reply_markup=get_menu())