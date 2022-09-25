from sqlalchemy import Column, String, Integer
from models.database import db



class Post(db.Model):
    # __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    post = Column(String(300), unique=False,nullable=False)

    # def __str__(self):
    #     return f'{self.__class__.__name__}(id={self.id}, ' \
    #            f'name={self.name!r}, ' \
    #            f'post={self.post!r},' \
    #
    # def __repr__(self):
    #     return str(self)