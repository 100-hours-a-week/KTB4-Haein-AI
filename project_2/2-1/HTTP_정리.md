# HTTP 정리

## HTTP란?

HTTP(HyperText Transfer Protocol)는
클라이언트와 서버가 데이터를 주고받기 위한 통신 규약

웹 브라우저와 서버 간 통신, REST API 통신 등에 사용됨

예:
- 브라우저 -> 서버 요청
- 서버 -> 응답 반환 

FastAPI 역시 HTTP 기반으로 동작

---

## HTTP 요청 (Request)

클라이언트가 서버에 보내는 요청

HTTP 요청은 다음 요소로 구성됨

- Method
- URL
- Header
- Body

예시:

```http
POST /posts HTTP/1.1
Content-Type: application/json

{
    "title": "공지사항",
    "content": "내용"
}
```

---

## HTTP 응답(Response)

서버가 클라이언트에게 반환하는 데이터

응답에는 다음이 포함됨
* Status Code
* Header
* Body

예시:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "message": "success"
}
```

---

## HTTP Method

HTTP Method는 클라이언트가 서버에 어떤 작업을 요청하는 작업 종류

| Method | 설명     | 예시     |
| ------ | ------ | ------ |
| GET    | 데이터 조회 | 게시글 조회 |
| POST   | 데이터 생성 | 게시글 생성 |
| PATCH  | 데이터 수정 | 게시글 수정 |
| DELETE | 데이터 삭제 | 게시글 삭제 |

### Method 예시

```http
GET /posts
POST /posts
PATCH /posts/1
DELETE /posts/1
```

---

## HTTP 상태 코드(Status Code)

서버의 응답 상태를 숫자로 나타내는 코드

| Status Code               | 의미        | 예시          |
| ------------------------- | --------- | ----------- |
| 200 OK                    | 요청 성공     | 게시글 조회 성공   |
| 201 Created               | 데이터 생성 성공 | 게시글 생성 성공   |
| 400 Bad Request           | 잘못된 요청    | 필수값 누락      |
| 404 Not Found             | 데이터 없음    | 존재하지 않는 게시글 |
| 500 Internal Server Error | 서버 내부 오류  | AI 모델 오류    |

---

## REST API

REST API는 URL을 이용하여 자원(Resource)을 관리하는 API 설계 방식

| URL         | 의미     |
| ----------- | ------ |
| /posts      | 게시글 목록 |
| /posts/1    | 1번 게시글 |
| /comments/3 | 3번 댓글  |

REST API는 HTTP Method와 함께 사용됨

---

## FastAPI와 HTTP

FastAPI는 HTTP 기반으로 API를 구현하는 Python 프레임워크

```python
@router.get("/")
@router.post("/")
@router.patch("/{post_id}")
@router.delete("/{post_id}")
```