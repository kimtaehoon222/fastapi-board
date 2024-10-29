# coding=utf-8
from sqlalchemy import Column, Integer, VARCHAR, DateTime
from datetime import datetime

from db.session import Base


class Url(Base):
    __tablename__ = "url"

    url_no = Column(Integer, primary_key=True, autoincrement=True)
    long_url = Column(VARCHAR(255), nullable=False)
    short_url = Column(VARCHAR(50), nullable=False)
    create_date = Column(DateTime, nullable=False, default=datetime.now())
