import os
import glob
from pyrogram import Client
from config.settings import Settings

def get_session_names() -> list[str]:
    session_names = sorted(glob.glob("sessions/*.session"))
    return [os.path.splitext(os.path.basename(file))[0] for file in session_names]


async def get_tg_client(session_name: str, proxy: str | None) -> Client:
    if not session_name:
        raise FileNotFoundError(f"Not found session {session_name}")

    if not Settings.APP_ID or not Settings.APP_HASH:
        raise ValueError("API_ID and API_HASH not found in the .env file.")
    tg_client = Client(
        name=session_name,
        api_id=Settings.APP_ID,
        api_hash=Settings.APP_HASH,
        workdir="sessions/",
        plugins=dict(root="bot/plugins"),
        proxy=proxy
    )

    return tg_client