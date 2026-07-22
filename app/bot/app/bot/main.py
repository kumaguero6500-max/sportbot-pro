from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message

from app.config import settings
from app.config.check import validate
from app.utils.logger import logger

validate()

bot = Bot(
    token=settings.bot_token,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    ),
)

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 Вітаю!\n\n"
        "SportBot Pro успішно запущений.\n\n"
        "Версія: 1.0"
    )


async def main():
    logger.info("SportBot запускається...")
    await dp.start_polling(bot)


def start():
    import asyncio
    asyncio.run(main())
