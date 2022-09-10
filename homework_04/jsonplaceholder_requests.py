# """
# создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
# """
#
#
#
# #import aiohttp
# #from loguru import logger
#
#
# USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
# POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"
#
# # @dataclass(frozen=True)
# # class Service:
# #     name: str
# #     url: str
# #     field: str
# #
# #
# # SERVICES = [
# #     Service(name="USERS_DATA_URL", url="http://httpbin.org/get", field="origin"),
# #     Service(name="httpbin-secure", url="https://httpbin.org/get", field="origin"),
# #     Service(name="ip-api", url="http://ip-api.com/json", field="query"),
# #     Service(name="ipify", url="https://api.ipify.org/?format=json", field="ip"),
# # ]
#
# # async def fetch_json(url):
# #     async with aiohttp.ClientSession() as session:
# #         async with session.get(url) as response:
# #             return await response.json()
#
#
# # async def fetch_json(session: aiohttp.ClientSession, url: str) -> dict:
# #     async with session.get(url) as response:  # type: aiohttp.ClientResponse
# #         data = await response.json()
# #         return data
#
# import aiohttp
# import asyncio  # нужен только для пробного запуска
#
# USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
# POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"
#
# async def fetch_json(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             return await response.json()
#
# if '__name__' == '__main__':
#     asyncio.run(fetch_json(USERS_DATA_URL))
#
#
#
#
#
import aiohttp
import asyncio  # нужен только для пробного запуска

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

if '__name__' == '__main__':
    asyncio.run(fetch_json(USERS_DATA_URL))