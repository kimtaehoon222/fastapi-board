# coding=utf-8
from sqlalchemy.orm import Session
from sqlalchemy import and_
from models.model import Board
from schema.board import *
from fastapi import HTTPException


def insert_board(new_post: NewPost, db: Session):

    post = Board(
        writer=new_post.writer,
        title=new_post.title,
        content=new_post.content

        )

    db.add(post)
    db.commit()

    return post.no


def list_all_board(db: Session):
    lists = db.query(Board).filter(Board.del_yn == 'Y').all()
    return [PostList(no=row.no, writer=row.writer, title=row.title, create_date=row.create_date) for row in lists]


def list_one_board(post_no: int, db: Session):
    try:
        post = db.query(Board).filter(and_(Board.no == post_no, Board.del_yn == 'Y')).first()
        return Post(no=post.no, writer=post.writer, title=post.title, content=post.content, create_date=post.create_date)
    except Exception as error:
        raise HTTPException(status_code=422, detail={"error": str(error), "msg": "존재하지 않는 게시글 입니다."})


def update_board(update_board_info : Update, db: Session):
    try:
        post = db.query(Board).filter(and_(Board.no == update_board_info.no, Board.del_yn == 'Y')).first()
        if not post :
            raise HTTPException(status_code=422, detail={"msg": "존재하지 않는 게시글 입니다."})
        post.title = update_board_info.title
        post.content = update_board_info.content
        db.commit()
        db.refresh(post)
        return list_one_board(post.no, db)

    except Exception as error:
        raise HTTPException(status_code=422, detail={"error": str(error), "msg": "존재하지 않는 게시글 입니다."})
