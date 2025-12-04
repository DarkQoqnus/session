from telethon import TelegramClient
import asyncio

API_ID = 34822373
API_HASH = '75c0cf49a5f69c70c000740aef0e09e8'
PHONE_NUMBER = '+989933867031'

async def main():
    client = TelegramClient('session', API_ID, API_HASH)
    await client.start(PHONE_NUMBER)
    
    session_string = client.session.save()
    print("\n" + "="*50)
    print("SESSION_STRING شما:")
    print(session_string)
    print("="*50)
    
    await client.disconnect()

asyncio.run(main())
