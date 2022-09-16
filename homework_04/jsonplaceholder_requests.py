"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
 """
import asyncio
import aiohttp


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


if '__name__' == '__main__':
    asyncio.run(fetch_json(USERS_DATA_URL))
    print(fetch_json(USERS_DATA_URL))