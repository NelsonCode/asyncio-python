from aiohttp import ClientSession
import asyncio


async def get_character(session, url: str) -> str:
    await asyncio.sleep(300)  # 5 minutos
    response = await session.get(url)
    character = await response.json()
    return character['name']


async def main():
    async with ClientSession() as session:
        try:
            url = 'https://rickandmortyapi.com/api/character/1'
            character = await asyncio.wait_for(get_character(session, url=url), timeout=8)
            print(character)
        except asyncio.TimeoutError:
            print("Timeout error")


asyncio.run(main())
