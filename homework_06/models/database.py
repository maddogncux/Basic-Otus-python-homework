# __all__ = ("db", "Base" )
#
# from typing import TYPE_CHECKING
#
# from flask_sqlalchemy import BaseQuery, Model, SQLAlchemy
#
# from sqlalchemy.orm import Session
# db = SQLAlchemy()
#
# class Base(Base):
#     # id = Column(Integer, primary_key=True)
#
#     if TYPE_CHECKING:
#         query: "BaseQuery"
#
#
# # class SQLAlchemy(SQLAlchemyGeneric):
# #     if TYPE_CHECKING:
# #         Model: Type[Base]
# #         session: Session
# #
# # db = SQLAlchemy(model_class=Base)

__all__ = ("db", )
from typing import TYPE_CHECKING, Type

from flask_sqlalchemy import BaseQuery
from flask_sqlalchemy import SQLAlchemy as SQLAlchemyGeneric, Model
from sqlalchemy.orm import Session


class Base(Model):
    # id = ...

    if TYPE_CHECKING:
        query: "BaseQuery"


class SQLAlchemy(SQLAlchemyGeneric):
    if TYPE_CHECKING:
        Model: Type[Base]
        session: Session


db = SQLAlchemy(model_class=Base)