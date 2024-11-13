from aiogram import Bot, Dispatcher, types
from core.handler import *
from config.settings import Settings

bot = Bot(token=Settings.BOT_TOKEN)
dp = Dispatcher(bot)


async def start_bot():
    bot_info = await bot.get_me()
    print(f'Telegram bot for testing has been run: @{bot_info.username}')