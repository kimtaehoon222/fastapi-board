# coding=utf-8
from sqlalchemy import Column, Integer, VARCHAR, DateTime
from datetime import datetime

from db.session import Base


class Board(Base):
    __tablename__ = "board"

    no = Column(Integer, primary_key=True, autoincrement=True)
    writer = Column(VARCHAR(30), nullable=False)
    title = Column(VARCHAR(30), nullable=False)
    content = Column(VARCHAR(100), nullable=False)
    create_date = Column(DateTime, nullable=False, default=datetime.now())
    del_yn = Column(VARCHAR(1), nullable=False, default='Y')
