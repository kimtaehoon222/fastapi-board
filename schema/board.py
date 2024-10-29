# coding=utf-8
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class NewPost(BaseModel):
    writer: str
    title: str
    content: Optional[str] = None


class PostList(BaseModel):
    no: int
    writer: str
    title: str
    create_date: datetime


class Post(BaseModel):
    no: int
    writer: str
    title: str
    content: Optional[str] = None
    create_date: datetime
