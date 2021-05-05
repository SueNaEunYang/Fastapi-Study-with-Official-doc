from fastapi import FastAPI
app = FastAPI()

@app.get("/items/{item_id}") #item_id (경로 파라미터)
async def read_item(item_id: int): #item_id (argument), int로 선언됨 (타입이 있는 매개변수)
    return {"item_id": item_id}

# uvicorn path_parameter:app --reload
# http://127.0.0.1:8000/items/3
# http://127.0.0.1:8000/docs (자동문서화)
# 데이터 검증은 Pydantic에 의해 수행됨

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# /users/me를 먼저 선언하고 /users/{user_id} 해야함

#Enum Class
from enum import Enum
#from fastapi import FastAPI (위에 있어서 생략)

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

#app = FastAPI() (위에 있어서 생략)

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName): 
#enum클래스를 사용하는 타입 어노테이션으로 경로 매개변수 생성
    
    #compare enumeration members
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    #get the enumeration value
    if model_name.value == "lenet":
        # your_enum_member.value
        # ModelName.lenet.value
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

#경로를 갖고있는 path parameter
    #Starlette의 내부 도구를 사용해서 
    # /files/{file_path:path} 
    # ===>> file_path (매개변수의 이름)
    # ===>> :path (tells it that the parameter should match any path)

    @app.get("/files/{file_path:path}")
    async def read_file(file_path: str):
        return {"file_path": file_path}