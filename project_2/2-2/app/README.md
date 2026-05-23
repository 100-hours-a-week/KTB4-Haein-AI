# Community Backend Service

FastAPI 기반 커뮤니티 서비스 백엔드 프로젝트

게시글/댓글 CRUD 기능과 AI 기반 게시글 요약 기능을 제공

---

## 기술 스택

- FastAPI
- SQLModel
- SQLite
- Ollama
- Uvicorn

---

## 프로젝트 구조

```text
project_2/
├─ 2-1/
│  └─ HTTP_정리.md
├─ 2-2/
│  ├─ app/
│  │  ├─ main.py
│  │  ├─ database.py
│  │  ├─ models.py
│  │  ├─ schemas.py
│  │  ├─ routers/
│  │  │  ├─ posts.py
│  │  │  ├─ comments.py
│  │  │  └─ ai.py
│  │  └─ services/
│  │     └─ ai_service.py
│  ├─ README.md
│  └─ requirements.txt

```

---

## 주요 기능

### 게시글 기능

- 게시글 생성
- 게시글 전체 조회
- 게시글 상세 조회
- 게시글 수정
- 게시글 삭제
- 게시글 검색 (id 또는 title로 검색 가능)
- 조회수 증가
- 좋아요 증가

### 댓글 기능

- 댓글 생성
- 댓글 수정
- 댓글 삭제

### AI 기능

- 특정 게시글 요약
- 게시글 id 또는 title로 검색 후 요약 가능

---

## 데이터베이스

SQLite 기반 데이터베이스를 사용

```text
community.db
```

SQLModel ORM을 사용하여 테이블을 관리

---

## API 구조

### Posts API

| Method | URL | Description |
|---|---|---|
| GET | `/posts/` | 게시글 전체 조회 |
| GET | `/posts/search` | 게시글 상세 조회 및 검색 |
| POST | `/posts/` | 게시글 생성 |
| PATCH | `/posts/{post_id}` | 게시글 수정 |
| DELETE | `/posts/{post_id}` | 게시글 삭제 |

---

### Comments API

| Method | URL | Description |
|---|---|---|
| POST | `/posts/{post_id}/comments/` | 댓글 생성 |
| PATCH | `/posts/{post_id}/comments/{comment_id}` | 댓글 수정 |
| DELETE | `/posts/{post_id}/comments/{comment_id}` | 댓글 삭제 |

---

### AI API

| Method | URL | Description |
|---|---|---|
| POST | `/ai/posts/summary` | 게시글 AI 요약 |

---

## 실행 방법

### 1. 가상환경 생성

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 2. 라이브러리 설치

```bash
pip install "fastapi[standard]" sqlmodel ollama
```

---

### 3. Ollama 설치 및 모델 다운로드

Ollama 설치:

https://ollama.com

모델 다운로드:

```bash
ollama pull gemma3
```

---

### 4. Ollama 서버 실행

```bash
ollama serve
```

이미 실행 중이라면 생략 가능

---

### 5. FastAPI 서버 실행

```bash
fastapi dev app/main.py
```

---

## Swagger API 문서

서버 실행 후 아래 주소에서 API 테스트 가능

```text
http://127.0.0.1:8000/docs
```

---

## AI 모델 서빙

Ollama의 `gemma3` 모델을 사용하여 게시글 요약 기능을 제공

FastAPI 서버에서 Ollama 서버를 호출하여 AI 응답을 반환

---

## 구조 설계

프로젝트는 Route - Service - Model 구조를 기반으로 구현

- Router: HTTP 요청 및 응답 처리
- Service: AI 요약 비즈니스 로직 처리
- Model: 데이터베이스 테이블 구조 관리
- Schema: 요청/응답 데이터 검증

---

## 구현 목표

본 프로젝트는 다음 목표를 중심으로 구현

- RESTful API 설계
- SQLite 기반 데이터 관리
- SQLModel ORM 적용
- Ollama 기반 AI 모델 서빙
- Router / Service / Model 구조 분리

---

## 참고 문서

- FastAPI: https://fastapi.tiangolo.com/
- SQLModel: https://sqlmodel.tiangolo.com/
- Ollama: https://ollama.com/

---

## 회고

이번 프로젝트에서는 FastAPI를 이용하여 커뮤니티 서비스 백엔드를 구현하였다.
게시글과 댓글 CRUD 기능을 구현하고, SQLite와 SQLModel을 이용하여 데이터베이스를 연결하였다. 또한 Ollama 기반 AI 모델을 활용하여 게시글 요약 기능도 추가하였다.

FastAPI 프로젝트 구조와 API 흐름이 익숙하지 않아 어려움이 있었다. Router, Model, Schema, Service 역할을 분리하는 과정에서 각 파일이 왜 필요한지 이해하는 데 시간이 걸렸다.

데이터베이스를 연결하면서 ORM(SQLModel)의 동작 방식도 배울 수 있었다. Session을 이용하여 데이터를 조회하고 commit 및 refresh를 통해 데이터 상태를 관리하는 과정을 경험할 수 있었다.

AI 기능을 구현할 때는 Ollama 서버 연결 과정에서 여러 오류를 겪었다. 모델 실행, 서버 실행, FastAPI와의 연결 과정에서 오류가 발생했지만, 로그를 확인하며 문제를 해결하는 경험을 할 수 있었다. 또한 처음에는 전체 게시글 목록을 요약하도록 구현했지만, 이후 특정 게시글만 요약하도록 수정하면서 API 설계의 중요성도 느낄 수 있었다.

이번 프로젝트를 통해 백엔드 서비스가 어떻게 구성되고 동작하는지 전체 흐름을 경험할 수 있었다. 앞으로는 인증 기능(JWT), 사용자 관리, 배포 과정 등도 추가로 학습해보고 싶다.
