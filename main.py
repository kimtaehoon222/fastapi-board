from fastapi import FastAPI
from db.session import Base
from db.session import engine
from sqlalchemy.ext.declarative import declarative_base
from router import board
from router import url

app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(url.app, tags=["url"])
app.include_router(board.app, tags=["borad"])


@app.get("/hello")
def hello():
    return {"message": "안녕하세요 파이보"}
