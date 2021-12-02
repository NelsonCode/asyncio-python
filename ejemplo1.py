from aiohttp import ClientSession
import asyncio


async def get_character(session, url: str) -> str:
    response = await session.get(url)
    character = await response.json()
    return character['name']


async def main():
    async with ClientSession() as session:
        url = 'https://rickandmortyapi.com/api/character/1'
        character = await get_character(session, url=url)
        print(character)


asyncio.run(main())
