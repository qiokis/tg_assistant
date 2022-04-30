import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types.bot_command import BotCommand
from dotenv import load_dotenv

load_dotenv('cfg/.env')

bot = Bot(token=os.environ['BOT_TOKEN'])
dp = Dispatcher(bot, storage=MemoryStorage())


async def main():

    commands = [
        BotCommand(command='/start', description='Start app')
    ]

    await bot.set_my_commands(commands)

    import app.handlers

    await dp.start_polling()
