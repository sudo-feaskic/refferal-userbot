from aiogram.filters import CommandStart
from aiogram.types import Message
import logging

from utils.loader import dp


logging.basicConfig(level=logging.INFO)


@dp.message(CommandStart())
async def start_handler(message: Message, command: CommandStart):
    user_id = message.from_user.id
    username = message.from_user.username
    full_name = message.from_user.full_name
    start_arg = command.args


    response_text = (
        f"👤 User Info:\n"
        f"User ID: {user_id}\n"
        f"Username: @{username}\n"
        f"Full Name: {full_name}\n"
    )
    if start_arg:
        response_text += f"\n🔗 Start Argument: {start_arg}"
    else:
        response_text += "\nNo start argument provided."

    await message.answer(response_text)

    logging.info(f"User {user_id} ({username}) started bot with argument: {start_arg}")



