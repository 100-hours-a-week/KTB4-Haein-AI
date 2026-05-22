# FastAPI 앱 시작점
# 서버를 실행하면 가장 먼저 main.py의 app 객체를 찾음

from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.database import create_db_and_tables
from app.routers import posts, comments
from app.routers import ai

# 아래 lifespan 함수를 FastAPI 시작/종료 관리 함수로 만들어줌
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

# FastAPI 앱 객체 생성
app = FastAPI(
    title = "Community API",
    description = "FastAPI 기반 커뮤니티 서비스",
    version = "1.0.0",
    lifespan = lifespan ## 그럼 이 전에 쓴 title 과 description 이 실행이 되고 그 이후에 lifespan 다음 함수가 서버가 켜지면 실행?
)

# 게시글 관련 API를 FastAPI 앱에 등록
app.include_router(posts.router)

# 여기까지 FastAPI 앱 생성 끝
# 게시글 관련 API를 FastAPI 앱에 등록
app.include_router(comments.router)
app.include_router(ai.router)

# GET / 주소로 요청이 오면 아래 함수 실행
@app.get("/")
def root():
    return {"message": "Community API"}