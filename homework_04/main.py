
"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

# async def created_db_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#
#
# async def save_user_in_db(u_data):
#     async with Session() as session:
#         async with session.begin():
#             for user in u_data:
#                 name = user['name']
#                 email = user['email']
#                 user = User(name=name, email=email)
#                 session.add(user)  # добавляем данные юзера в сессию
#                 # session.commit() делается авт
#
#             async def save_post_in_db(p_data):
#                 async with Session() as session:
#                     async with session.begin():
#                         for post in p_data:
#                             title = post['title']
#                             description = post['body']
#                             user_id = post['userId']
#                             post = Post(title=title, description=description, user_id=user_id)
#                             session.add(post)
import asyncio

from jsonplaceholder_requests import USERS_DATA_URL, POSTS_DATA_URL, fetch_json

from models import create_pg_docker, save_users_and_post, cmd, created_db_tables


async def async_main():
    await create_pg_docker(cmd)
    await created_db_tables()

    users_data, posts_data = await asyncio.gather(
        fetch_json(USERS_DATA_URL),
        fetch_json(POSTS_DATA_URL),
    )

    await save_users_and_post(users_data, posts_data)
    # await save_user_in_db(posts_data)
    # user_data, post_data = await asyncio.gather(fetch_json(USERS_DATA_URL),
    #                                             (fetch_json(USERS_DATA_URL))
    # await save_user_in_db(user_data)
    # await save_user_in_db(post_data)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
