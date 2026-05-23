# AI 요약 API 주소를 관리
from fastapi import APIRouter, Depends, HTTPException
from httpx import post
from sqlmodel import Session, select
from app.models import Post
from app.schemas import SummaryRead
from app.database import get_session
from app.services.ai_service import summarize_text
from typing import Optional

# 이 파일의 모든 API 주소 앞에 /ai 가 붙음
router = APIRouter(prefix="/ai", tags=["AI"])

@router.post("/posts/summary", response_model=SummaryRead)
def summarize_posts(
    post_id: Optional[int] = None,
    title: Optional[str] = None,
    session: Session = Depends(get_session)
):
    statement = select(Post)

    if post_id is not None:
        statement = statement.where(Post.id == post_id)

    if title is not None:
        statement = statement.where(Post.title == title)
    
    posts = session.exec(statement).first()
    
    if not posts:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
    
    text = f"제목: {posts.title}\n내용: {posts.content}"

    try:
        summary = summarize_text(text)
        return SummaryRead(summary=summary)
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"AI 요약 실패: {str(e)}",
        )