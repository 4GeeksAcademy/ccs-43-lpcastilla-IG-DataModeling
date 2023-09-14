import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(500), nullable=False)
    password = Column(String(500), nullable=False)
    followers = relationship('Followers', back_populates='user')
    post = relationship('Post', back_populates='user')
    comment = relationship('Comment', back_populates='user')

class Followers(Base):
    __tablename__ = 'followers'
    user_from_id = Column(Integer, nullable=False)
    id_user = Column(Integer, ForeignKey('user.id'), nullable=False, primary_key=True)
    user = relationship("User", back_populates='followers')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship("User", back_populates='post')
    comment = relationship("Comment", back_populates='post')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(2000), nullable=False)
    id_user = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship("User", back_populates='comment')
    id_post = Column(Integer, ForeignKey('post.id'), nullable=False)
    post = relationship("Post", back_populates='comment')
    
 
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

