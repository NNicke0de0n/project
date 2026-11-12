import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from src.handlers import common

load_dotenv()

async def main():
    token = os.getenv("BOT_TOKEN", "YOUR_TEST_TOKEN")
    bot = Bot(token=token)
    dp = Dispatcher()

    dp.include_router(common.router)

    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())