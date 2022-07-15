from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import configs

engine = create_engine(configs.db_url)
session = sessionmaker(bind=engine)()
base = declarative_base()


class Article(base):
    __tablename__ = 'article'

    link = Column(String, primary_key=True, nullable=False, unique=True)
    title = Column(String, nullable=False)
    article = Column(String, nullable=False)
    date = Column(String, nullable=False)


class User(base):
    __tablename__ = 'user'

    telegram_id = Column(Integer, primary_key=True, unique=True)


def init_db():
    base.metadata.create_all(engine)


def add_user(telegram_id):
    user = User(telegram_id=telegram_id)
    session.add(user)
    session.commit()


def get_users():
    return session.query(User.telegram_id).all()


def remove_user(telegram_id):
    session.query(User).filter(User.telegram_id == telegram_id).delete()
    session.commit()


def check_if_user_exists(telegram_id):
    exists = session.query(session.query(User).filter(User.telegram_id == telegram_id).exists()).scalar()
    return exists
