# coding=utf-8
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ShortenUrl(BaseModel):
    long_url : str

