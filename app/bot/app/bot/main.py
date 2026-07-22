from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message

from app.config import settings
from app.config.check import validate
from app.utils.logger import logger
from app.services.live_service import get_live_matches

validate()

bot = Bot(
    token=settings.bot_token,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):

    await message.answer(
        "SportBot Pro запущений ✅"
    )


@dp.message(Command("live"))
async def live(message: Message):

    matches = await get_live_matches()

    if not matches:
        await message.answer("Зараз немає live матчів.")
        return

    text = ""

    for match in matches[:10]:

        league = match["league"]["name"]

        home = match["teams"]["home"]["name"]

        away = match["teams"]["away"]["name"]

        minute = match["fixture"]["status"]["elapsed"]

        goals_home = match["goals"]["home"]

        goals_away = match["goals"]["away"]

        text += (
            f"🏆 {league}\n"
            f"{home} {goals_home}:{goals_away} {away}\n"
            f"⏱ {minute}'\n\n"
        )

    await message.answer(text)


async def main():

    logger.info("SportBot стартував")

    await dp.start_polling(bot)


def start():

    import asyncio

    asyncio.run(main())
