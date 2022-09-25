from os import getenv
# DB_ASYNC_URL = "postgresql+asyncpg://username:passwd!@localhost:5433/blog"





SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+asyncpg://username:passwd!@localhost:5433/blog",
)

DB_ECHO = True
