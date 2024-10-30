# coding=utf-8
from sqlalchemy.orm import Session

import schema.board
from db.connection import get_db
from crud.board import *
from fastapi import APIRouter, Depends, HTTPException

app = APIRouter(
    prefix="/board",
    )


@app.post(path="/create", description="기본 게시판 - 게시글 생성")
async def create_board(new_post: schema.board.NewPost, db: Session = Depends(get_db)):
    return insert_board(new_post, db)


@app.get(path="/read", description="기본 게시판 - 게시글 조회")
async def read_board(db: Session = Depends(get_db)):
    return list_all_board(db)


@app.get(path="/read/{post_no}", description="기본 게시판 - 특정 게시글 조회", response_model=schema.board.Post)
async def read_post(post_no: int, db: Session = Depends(get_db)):
    # borad_post = list_one_board(post_no, db)
    # if borad_post:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    return list_one_board(post_no, db)


@app.put(path="/update/{post_no}", description="기본 게시판 - 특정 게시글 변경", response_model=schema.board.Update)
async def update_post(update_board_info: schema.board.Update, db: Session = Depends(get_db)):
    return update_board(update_board_info, db)
