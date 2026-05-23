# 댓글 관련 API 관리
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.models import Post, Comment
from app.schemas import CommentCreate, CommentRead, CommentUpdate
from app.database import get_session

router = APIRouter(prefix="/posts/{post_id}/comments", tags=["Comments"])

@router.post("/", response_model=CommentRead, status_code=status.HTTP_201_CREATED)
def create_comment(
    post_id: int,
    comment_data: CommentCreate,
    session: Session = Depends(get_session),
):
    # 댓글을 달 게시글이 존재하는지 확인
    post = session.get(Post, post_id)

    # 게시글이 존재하지 않으면 404 에러 반환
    if not post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")

    # 게시글이 존재하면 댓글 생성
    comment = Comment(
        content=comment_data.content,
        author=comment_data.author,
        # 이 댓글이 어떤 게시글에 속하는지 연결
        post_id=post_id,
    )
    
    session.add(comment)
    session.commit()
    session.refresh(comment)

    return comment

@router.patch("/{comment_id}", response_model=CommentRead)
def update_comment(
    post_id: int,
    comment_id: int,
    comment_data: CommentUpdate,
    session: Session = Depends(get_session),
):
    comment = session.get(Comment, comment_id)

    if not comment or comment.post_id != post_id:
        raise HTTPException(status_code=404, detail="댓글을 찾을 수 없습니다.")
    
    if comment_data.content is not None:
        comment.content = comment_data.content
    
    session.add(comment)
    session.commit()
    session.refresh(comment)

    return comment