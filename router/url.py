import hashlib

# import schema.board
# from db.session import conn
# from fastapi import APIRouter, Depends
# import hashlib
# import uuid
# from db.connection import get_db


from sqlalchemy.orm import Session

import schema.url
from db.connection import get_db
from crud.url import insert_url
from fastapi import APIRouter, Depends

app = APIRouter(
    prefix="/api/v1",
    )


# @app.get(path="/shortUrl", description="단축 URL 조회")
# def short_url():
#
#     with conn.cursor() as cur:
#         cur.execute("select )


@app.post(path="/url/shorten", description="URL 변환")
async def create_url(longUrl: str, db: Session = Depends(get_db)):
    return insert_url(longUrl, db)

# @app.post(path="/url/shorten", description="URL 변환")
# def shorten_url(longUrl):
#     originalUrl = longUrl
#
#     url_id = str(uuid.uuid4())
#
#     shotUrl = hashlib.md5(url_id.encode()).hexdigest()[:8]
#
#     with conn.cursor() as cur:
#         cur.execute("INSERT INTO url (url_id, short_url, long_url) VALUES (%s, %s, %s)", (url_id, shotUrl, originalUrl))
#         conn.commit()
#
#     return {"short_url": shotUrl}
