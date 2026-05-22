# DB 테이블 설계
from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class Post(SQLModel, table=True):
    # default=None : id는 자동으로 증가하는 숫자이므로, 사용자가 입력하지 않아도 됨
    # primary_key=True : 이 값이 테이블의 기본키
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content:str
    author: str
    views: int=0
    likes: int=0
    created_at: datetime = Field(default_factory=datetime.now)
    # 댓글은 여러 개 달릴 수 있으므로 List로 표현
    # post와 comment는 서로 연결되어 있으므로, Relationship으로 표현
    comments: List["Comment"] = Relationship(back_populates="post")

class Comment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str
    author: str
    created_at: datetime = Field(default_factory=datetime.now)
    # 이 댓글이 어떤 게시글에 달린 댓글인지 저장하는 값
    # foreign_key="post.id"는 comment.post_id가 post 테이블의 id를 참조한다는 뜻
    post_id: int = Field(foreign_key="post.id")
    # 댓글에서 자기 부모 게시글에 접근할 수 있음
    post: Post = Relationship(back_populates="comments")