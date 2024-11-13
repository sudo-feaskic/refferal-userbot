from pyrogram import Client

import asyncio

app = Client("my_account",workdir='sessions')

username = 'skillswapacademy_bot'

async def main():
  async with app:
        chat = await app.get_chat(username)
        async for message in app.get_chat_history(chat.id, limit=3):
            print(f"\nMessage ID: {message.id}")
            print(f"Date: {message.date}")
            print(f"Text: {message.text}")
            
            if message.reply_markup:
                print("Inline Keyboard:")
                for row in message.reply_markup.keyboard:
                    print(" | ".join([button for button in row]))

# TODO GET LINK AND FOLLOW, THEN VERIFY, THEN AWAIT 30 SECONDS AND DELETE CHAT




asyncio.get_event_loop().run_until_complete(main())