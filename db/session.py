# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base  # Base 생성
from core.config import settings
import psycopg2

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# conn = psycopg2.connect(
#     host=settings.DB_HOST,
#     database=settings.DB_DATABASE,
#     user=settings.DB_USERNAME,
#     password=settings.DB_PASSWORD,
#     )
# conn.autocommit = True

# cur = conn.cursor()
