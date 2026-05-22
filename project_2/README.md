# Project 2 - Community Backend Service

FastAPI 기반 커뮤니티 서비스 백엔드 프로젝트

게시글/댓글 CRUD 기능과 AI 기반 게시글 요약 기능을 제공

---

# 기술 스택

- FastAPI
- SQLModel
- SQLite
- Ollama
- Uvicorn

---

# 프로젝트 구조

```text
project_2/
├─ app/
│  ├─ main.py
│  ├─ database.py
│  ├─ models.py
│  ├─ schemas.py
│  ├─ routers/
│  │  ├─ posts.py
│  │  ├─ comments.py
│  │  └─ ai.py
│  └─ services/
│     └─ ai_service.py
├─ requirements.txt
└─ README.md
```

---

# 주요 기능

## 게시글 기능

- 게시글 생성
- 게시글 전체 조회
- 게시글 상세 조회
- 게시글 수정
- 게시글 삭제
- 게시글 검색 (id 또는 title로 검색 가능)
- 조회수 증가
- 좋아요 증가

## 댓글 기능

- 댓글 생성
- 댓글 수정
- 댓글 삭제

## AI 기능

- 특정 게시글 요약
- 게시글 id 또는 title로 검색 후 요약 가능

---

# 데이터베이스

SQLite 기반 데이터베이스를 사용

```text
community.db
```

SQLModel ORM을 사용하여 테이블을 관리

---

# API 구조

## Posts API

| Method | URL | Description |
|---|---|---|
| GET | `/posts/` | 게시글 전체 조회 |
| GET | `/posts/search` | 게시글 상세 조회 및 검색 |
| POST | `/posts/` | 게시글 생성 |
| PATCH | `/posts/{post_id}` | 게시글 수정 |
| DELETE | `/posts/{post_id}` | 게시글 삭제 |

---

## Comments API

| Method | URL | Description |
|---|---|---|
| POST | `/posts/{post_id}/comments/` | 댓글 생성 |
| PATCH | `/posts/{post_id}/comments/{comment_id}` | 댓글 수정 |
| DELETE | `/posts/{post_id}/comments/{comment_id}` | 댓글 삭제 |

---

## AI API

| Method | URL | Description |
|---|---|---|
| POST | `/ai/posts/summary` | 게시글 AI 요약 |

---

# 실행 방법

## 1. 가상환경 생성

### Mac / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 2. 라이브러리 설치

```bash
pip install "fastapi[standard]" sqlmodel ollama
```

---

## 3. Ollama 설치 및 모델 다운로드

Ollama 설치:

https://ollama.com

모델 다운로드:

```bash
ollama pull gemma3
```

---

## 4. Ollama 서버 실행

```bash
ollama serve
```

이미 실행 중이라면 생략 가능

---

## 5. FastAPI 서버 실행

```bash
fastapi dev app/main.py
```

---

# Swagger API 문서

서버 실행 후 아래 주소에서 API 테스트 가능

```text
http://127.0.0.1:8000/docs
```

---

# AI 모델 서빙

Ollama의 `gemma3` 모델을 사용하여 게시글 요약 기능을 제공

FastAPI 서버에서 Ollama 서버를 호출하여 AI 응답을 반환

---

# 구조 설계

프로젝트는 Route - Service - Model 구조를 기반으로 구현

- Router: HTTP 요청 및 응답 처리
- Service: AI 요약 비즈니스 로직 처리
- Model: 데이터베이스 테이블 구조 관리
- Schema: 요청/응답 데이터 검증

---

# 구현 목표

본 프로젝트는 다음 목표를 중심으로 구현

- RESTful API 설계
- SQLite 기반 데이터 관리
- SQLModel ORM 적용
- Ollama 기반 AI 모델 서빙
- Router / Service / Model 구조 분리

---

# 참고 문서

- FastAPI: https://fastapi.tiangolo.com/
- SQLModel: https://sqlmodel.tiangolo.com/
- Ollama: https://ollama.com/
