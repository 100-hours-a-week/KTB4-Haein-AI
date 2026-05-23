# DB 연결 담당
# SQLite 파일 DB인 community.db 사용
from sqlmodel import SQLModel, create_engine, Session

# SQLite DB 파일 위치 정하기 (project_2/community.db)
sqlite_url = "sqlite:///community.db"

# FastAPI와 SQLite를 연결하는 DB엔진 만들기
# echo=True : 실행되는 SQL을 터미널에 보여줌
engine = create_engine(sqlite_url, echo=True)

# DB 테이블 생성 함수
def create_db_and_tables():
    # models.py에서 정의한 DB 테이블을 실제 DB에 생성
    SQLModel.metadata.create_all(engine)

# API 함수에서 DB 작업을 할 때 사용할 세션을 만드는 함수
# session : SELECT, INSERT, UPDATE 같은 DB 작업을 하는 객체
# Depends(get_session) : 이 함수에 필요한 객체를 자동으로 넣어주는 기능
def get_session():
    with Session(engine) as session:
        yield session # yield : 이 함수가 반환하는 session 객체를 API 함수에서 사용할 수 있게 해줌