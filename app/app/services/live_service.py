from app.api.api_football import APIFootball

api = APIFootball()


async def get_live_matches():

    data = await api.get_live_matches()

    return data.get("response", [])
