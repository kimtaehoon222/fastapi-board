# coding=utf-8
from sqlalchemy.orm import Session
from sqlalchemy import and_
from models.url import Url
from schema.url import ShortenUrl
import hashlib
import time


def insert_url(long_url: str, db: Session):

    timestamp_ms = int(time.time() * 1000)

    # 64비트 ID 생성 (시간 + 랜덤 값)
    url_id = (timestamp_ms << 16) | (hash(str(timestamp_ms)) & 0xFFFF)

    short_url = hashlib.md5(str(url_id).encode()).hexdigest()[:7]
    post = Url(
        url_no=url_id,
        long_url=long_url,
        short_url=short_url
        )

    db.add(post)
    db.commit()

    return post.short_url
