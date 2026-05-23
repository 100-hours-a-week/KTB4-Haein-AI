# 게시글 API 주소들을 모아두는 파일
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.models import Post
from app.schemas import PostCreate, PostRead, PostUpdate
from app.database import get_session
from typing import List, Optional

# 이 파일의 모든 API 주소 앞에 /posts 가 붙음
router = APIRouter(prefix="/posts", tags=["Posts"])

# GET/posts/ 요청 처리 
# response_model(응답)은 게시글 리스트
# 게시글 전체 조회 API
@router.get("/", response_model=list[PostRead])
# DB 작업을 하기 위해 세션을 주입받음
def get_posts(session: Session = Depends(get_session)):
    # DB 에서 모든 게시글 조회
    return session.exec(select(Post)).all()

# 게시글 상세 조회 API
# GET/posts/search 요청 처리
@router.get("/search", response_model=PostRead)
def get_search(
    post_id: Optional[int] = None,
    title: Optional[str] = None, 
    session: Session = Depends(get_session)
):
    if post_id is None and title is None:
        raise HTTPException(
            status_code=400, 
            detail="post_id 또는 title 중 하나는 입력되어야 합니다."
        )
    
    # DB 검색 준비
    # statement에 SQL 조건을 이어붙이는 방식
    statement = select(Post)

    # SQL 조건 이어붙이기 1
    if post_id is not None:
        statement = statement.where(Post.id == post_id)

    # SQL 조건 이어붙이기 2
    if title is not None:
        statement = statement.where(Post.title == title)
    
    # 지금까지 만든 SQL 조건을 DB에 보내서 검색
    # first()는 검색 결과 중 첫 번째 게시글만 가져오라는 뜻
    post = session.exec(statement).first()
    
    if not post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
    
    # 게시글이 존재하면 조회수 1 증가시키고 DB에 저장 -> 최신 상태로 갱신
    post.views += 1 
    session.add(post)
    session.commit()
    session.refresh(post)

    return post

# 게시글 생성 API
@router.post("/", response_model=PostRead, status_code=status.HTTP_201_CREATED)
def create_post(post_data: PostCreate, session: Session = Depends(get_session)):
    post = Post.model_validate(post_data)
    session.add(post)
    session.commit()
    session.refresh(post)
    return post

# 게시글 수정 API
@router.patch("/{post_id}", response_model=PostRead)
def update_post(
    post_id: int,
    post_data: PostUpdate,
    session: Session = Depends(get_session)
):
    post = session.get(Post, post_id)

    if not post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
    
    # 입력된 데이터가 None이 아닌 경우에만 게시글 정보 수정
    if post_data.title is not None:
        post.title = post_data.title
    
    if post_data.content is not None:
        post.content = post_data.content
    
    session.add(post)
    session.commit()
    session.refresh(post)
    return post

# 게시글 삭제 API
@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, session: Session = Depends(get_session)):
    post = session.get(Post, post_id)

    if not post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
    
    session.delete(post)
    session.commit()
    return
