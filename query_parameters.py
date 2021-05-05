#The query is the set of key-value pairs that go after the ? in a URL, separated by & characters.

from fastapi import FastAPI
app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

#default
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

#optional
@app.get("/items/{item_id}") #경로 매개변수
async def read_item(item_id: str, q: Optional[str] = None):
    if q: #쿼리 매개변수
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

#형 변환
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

#Required query parameters
# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
    ## 쿼리 매개변수 needy는 str타입의 필수 쿼리 매개변수
    ## ==>> needy를 url에 넣지 않으면 오류가 뜸 (value_error.missing)
    ## ===>> http://127.0.0.1:8000/items/foo-item?needy=sooooneedy 와 같이 넣어줘야함
    ## 이것도 가능 :::
    ##    item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None
):
#     return item

##경로 매개변수처럼 쿼리 매개변수도 Enum을 사용할 수 있음