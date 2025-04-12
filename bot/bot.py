import asyncio
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {message.from_user.full_name}!")


# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot starting....")
    asyncio.run(main())
