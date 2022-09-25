__all__ = (
    "db",
    "Post",
)

from .database import db, Base
from models.post import Post