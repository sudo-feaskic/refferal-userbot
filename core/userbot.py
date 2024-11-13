import asyncio
from pyrogram import Client
from pyrogram.raw import functions
from urllib.parse import urlparse, parse_qs
import random

app = Client("my_account", workdir='/sessions')

def parse_url(url: str):
    """Parse the referral URL to extract username and start parameter."""
    try:
        parsed = urlparse(url)
        username = parsed.path[1:]
        start_param = parse_qs(parsed.query).get('start', [None])[0]
        return username, start_param
    except Exception as e:
        print(f"Error parsing URL: {e}")
        return None, None


async def register_by_referral(url: str):
    """Register to a bot via referral link."""
    username, start_param = parse_url(url)
    if not username or not start_param:
        print("Invalid URL or missing start parameter")
        return

    await app.start()
    try:
        bot_peer = await app.resolve_peer(username)
        random_id = random.randint(1, 1_000_000_000)

        await app.invoke(
            functions.messages.StartBot(
                peer=bot_peer,
                bot=bot_peer,
                random_id=random_id,
                start_param=start_param
            )
        )
        print("Successfully registered via referral link!")
    except Exception as e:
        print(f"Error during registration: {e}")
    finally:
        await app.stop()
    # TODO DELETE CHAT AND CHECK SUBSRIBE

async def process():
    while True:
        url = input('Example: https://t.me/username?start=param\nInput the link:  ')
        asyncio.get_event_loop().run_until_complete(url)