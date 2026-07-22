import aiohttp
from app.config import settings
from app.utils.logger import logger

BASE_URL = "https://v3.football.api-sports.io"


class APIFootball:

    def __init__(self):
        self.headers = {
            "x-apisports-key": settings.api_football_key
        }

    async def request(self, endpoint: str, params=None):

        async with aiohttp.ClientSession(headers=self.headers) as session:

            async with session.get(
                BASE_URL + endpoint,
                params=params
            ) as response:

                if response.status != 200:
                    text = await response.text()
                    logger.error(text)
                    raise Exception(text)

                return await response.json()

    async def get_live_matches(self):

        return await self.request(
            "/fixtures",
            {
                "live": "all"
            }
        )

    async def get_fixture_statistics(self, fixture_id: int):

        return await self.request(
            "/fixtures/statistics",
            {
                "fixture": fixture_id
            }
        )
