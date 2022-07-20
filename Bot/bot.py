import asyncio
from aiogram import Bot, Dispatcher
import logging
from DB.postgresql import PostgreSQL
from Config import bot_config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=bot_config.TOKEN)
dp = Dispatcher(bot)
loop = asyncio.get_event_loop()

db = loop.run_until_complete(PostgreSQL.create())

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Сәлем, {0.full_name}'.format(message.from_user))
    