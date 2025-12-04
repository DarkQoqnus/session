from telethon import TelegramClient
import asyncio

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
PHONE_NUMBER = os.environ["PHONE_NUMBER"]

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
