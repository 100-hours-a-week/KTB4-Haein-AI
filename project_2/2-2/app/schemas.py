# API로 들어오는 요청 데이터와 나가는 응답 데이터의 모양 정함
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

class CommentCreate(BaseModel):
    content: str
    author: str

class CommentRead(BaseModel):
    id: int
    content: str
    author: str
    created_at: datetime

# 사용자가 게시글 만들 때 보내는 데이터
class PostCreate(BaseModel):
    title: str
    content: str
    author: str

# 게시글 수정할 때 보내는 데이터 
class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

# 서버가 사용자에게 응답할 때 보내는 데이터
class PostRead(BaseModel):
    id: int
    title: str
    content: str
    author: str
    views: int
    likes: int
    created_at: datetime
    comments: List[CommentRead] = []

class SummaryRead(BaseModel):
    summary: str

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class CommentUpdate(BaseModel):
    content: Optional[str] = None