
from loguru import logger
import asyncio
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,

)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, declared_attr
import config
import os
PG_CONN_URI = os.environ.get("DB_ASYNC_URL") or "postgresql+asyncpg://username:passwd!@localhost:5433/blog"

# engine = create_async_engine(DB_ASYNC_URL, echo=DB_ECHO)
async_engine: AsyncEngine = create_async_engine(
    config.DB_ASYNC_URL,
    echo=config.DB_ECHO,
)

# Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    # expire_on_commit=True
    expire_on_commit=False
)


# Base = declarative_base()
class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


Base = declarative_base(cls=Base)


class User(Base):
    __tablename__ = 'user'

    name = Column(String, nullable=False, default='', server_default='')
    username = Column(String, nullable=False, default='', server_default='')
    email = Column(String, nullable=False, default='', server_default='')

    posts = relationship('Post', back_populates='user')

    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id}, ' \
               f'name={self.name!r}, ' \
               f'username={self.username!r},' \
               f'email={self.email}),'\


    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__ = 'posts'

    title = Column(String, nullable='', default='', server_default='')
    body = Column(String, nullable='', default='', server_default='')
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship('User', back_populates='posts')

    def __str__(self):
        return f'{self.__class__.__name__}(id={self.user_id},' \
               f' title={self.title!r},' \
               f' body={self.body!r}),' \


    def __repr__(self):
        return str(self)

# запускаем докер, вызвав команду в консоли используя create_subprocess_shell(cmd)


cmd = 'docker compose up -d'


async def create_pg_docker(cmd):
    result = await asyncio.create_subprocess_shell(cmd)
    await result.communicate()
    logger.info('____pg docker rdy')


# делаем DROP TABLE, CREATE TABLE в БД
async def created_db_tables():
    async with async_engine.begin() as conn:
        print("todo: drop all")
        await conn.run_sync(Base.metadata.drop_all)
        print("todo: create all")
        await conn.run_sync(Base.metadata.create_all)


async def save_users_and_post(u_data, p_data):
    async with Session() as session:
        async with session.begin():
            for user in u_data:
                id = user['id']
                name = user['name']
                username = user['username']
                email = user['email']
                user = User(id=id, name=name, username=username, email=email)
                session.add(user)
                # session.commit()
                for post in p_data:
                    if post["userId"] == user.id:
                        user_id = post["userId"]
                        title = post['title']
                        body = post['body']
                        post = Post(user_id=user_id, title=title, body=body)
                        session.add(post)
                    # session.commit()


# class User(Base):
#     __tablename__ = 'user'
#
#     # id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False, default='', server_default='')
#     username = Column(String, nullable=False, default='', server_default='')
#     email = Column(String, nullable=False, default='', server_default='')
#     created_at = Column(DateTime, nullable=False, default=datetime.utcnow, server_default=func.now())
# do a timestemps
#
#     posts = relationship('User_id', back_populates='id')
#
#     def __str__(self):
#         return f'{self.__class__.__name__}(user_id={self.user_id},' \
#                f'name={self.name!r},' \
#                f'username={self.username!r},' \
#                f'email={self.email},' \
#                f'created_at={self.created_at!r})'
#
#     def __repr__(self):
#         return str(self)
#
#
# class Post(Base):
#     __tablename__ = 'posts'
#
#     user_id = Column(Integer, primary_key=True)
#     title = Column(String, nullable='', default='', server_default='')
#     body = Column(String, nullable='', default='', server_default='')
#     users = relationship('id', back_populates='user_id')
#
#     def __str__(self):
#         return f'{self.__class__.__name__}(id={self.user_id},' \
#                f' title={self.title!r},' \
#                f' body={self.body!r}),' \
#
#
#
#     def __repr__(self):
#         return str(self)


# cоздаем ф-ю, которая скачивает с сайта юзеров и сохраняет их в БД
# async def save_user_in_db(userdata):
#     async with async_session() as session:
#         async with session.begin():
#             for user in data:
#                 #user_id = user["Id"]
#                 name = user['name']
#                 username = user['username']
#                 email = user['email']
#                 user = User(name=name, username=username, email=email)
#                 session.add(user)  # добавляем данные юзера в сессию
#                 session.commit()
#             # for post in data:
#             #     user_id = post['user_id']
#             #     title = post['title']
#             #     body = post['body']
#             #
#             #     post = Post(user_id=user_id, title=title, body=body)
#             #     session.add(post)
#
# # # cоздаем ф-ю, которая скачивает с сайта посты и сохраняет их в БД
# # async def save_post_in_db(p_data):
# #     async with async_session() as session:
# #         async with session.begin():
# #             for post in p_data:
# #                 user_id = post['userId']
# #                 title = post['title']
# #                 body = post['body']
# #
# #                 post = Post(user_id=user_id, title=title, body=body)
# #                 session.add(post)
#
#
# # создаем модель таблицы User и Post
