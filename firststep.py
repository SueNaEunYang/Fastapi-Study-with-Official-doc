from fastapi import FastAPI 
#FastAPI는 Starlette를 직접 상속하는 클래스

app = FastAPI() 
#FastAPI 인스턴스 생성 (=app =uvicorn이 참조하는 app과 동일)

#path operation 생성 
    # path는 endpoint, route로도 불림
    # Opertation : HTTP method 중 하나. POST, GET, PUT, DELETE, ...

@app.get("/") # decorator
async def root(): # async 말고 일반함수로 정의해도 됨 (def root():)
    return {"message": "Hello Sue World"}

# 실행하려면 : uvicorn firststep:app --reload
# uvicorn main:app --reload
    # main: 파일 main.py (파이썬 "모듈").
    # app: main.py 내부의 app = FastAPI() 줄에서 생성한 오브젝트.
    # --reload: 코드 변경 후 서버 재시작. 개발에만 사용.

# 이제 http://127.0.0.1:8000/docs 로 가면 API 문서 (스웨거)
# http://127.0.0.1:8000/redoc 에서는 대안API 문서 (ReDoc)

# OPEN API, 스키마
    #  http://127.0.0.1:8000/openapi.json

