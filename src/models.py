import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    name = Column(String(250), nullable=False)
    password = Column(String(40), nullable=False)
    email = Column(String(150), nullable=False)
    active = Column(Boolean)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    type = Column(String(20))
    url = Column(String(300))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    comment_text = Column(String(300))
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    user = relationship(User)
    post = relationship(Post)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e