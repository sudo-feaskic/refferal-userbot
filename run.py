import asyncio

from utils.loader import start_bot
from core.userbot import process

async def main():
    asyncio.gather(
        start_bot(),
        process()
    )