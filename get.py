import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# این سه تا مقدار رو خودت بذار
API_ID = int(os.environ["API_ID"])   # عددی
API_HASH = os.environ["API_HASH"]
SESSION_STRING = os.environ["SESSION_STRING"]

async def main():
    # ساخت کلاینت با سیشن
    async with TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH) as client:
        # تست: ارسال پیام به Saved Messages
        await client.send_message("me", "✅ این یک تست است. Session String درست کار می‌کند!")

        print("پیام تست به Saved Messages ارسال شد.")

if __name__ == "__main__":
    asyncio.run(main())
