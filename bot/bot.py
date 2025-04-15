import asyncio
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

from utils import download_instagram

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {message.from_user.full_name}!")

@dp.message(F.text.startswith(("https://www.instagram.com", "https://instagram.com")))
async def download_handler(message:Message):
    if message.text:
        result = download_instagram(link=message.text)
        if result.get("media"):
            url = result["media"][0].get("url")
            await message.answer_video(video=url, caption="Test")
# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot starting....")
    asyncio.run(main())
