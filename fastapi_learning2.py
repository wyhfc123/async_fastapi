# -*-coding:utf-8-*-
from typing import Optional
from fastapi import FastAPI, status, Form, File, UploadFile, HTTPException, Header,Depends
from pydantic import BaseModel,EmailStr
app = FastAPI()
#全局依赖项
# app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])
# class UserIn(BaseModel):
#     username:str
#     password:str
#     email:EmailStr
#     full_name:Optional[str] = None
# class UserOut(BaseModel):
#     username:str
#     email:EmailStr
#     full_name:Optional[str] = None
# class UserInDB(BaseModel):
#     username:str
#     hashed_password:str
#     email:EmailStr
#     full_name : Optional[str] = None
# def fake_password_hasher(raw_password:str):
#     return "supersecret"+raw_password
# def fake_save_user(user_in:UserIn):
#     hashed_password = fake_password_hasher(user_in.password)
#     # print(hashed_password,24)
#     user_in_db = UserInDB(**user_in.dict(),hashed_password = hashed_password)
#     # print(user_in_db,26)
#     print("User saved! ...... noyt really!")
#     return user_in_db
# @app.post("/user/",response_model=UserOut)
# async def create_user(user_in:UserIn,):
#     user_saved = fake_save_user(user_in)
#     return user_saved

"""减少重复"""

# class UserBase(BaseModel):
#     username:str
#     email:EmailStr
#     full_name:Optional[str] = None
# class UserIn(UserBase):
#     password:str
# class UserOut(UserBase):
#     pass
# class UserInDB(UserBase):
#     hashed_password:str
#
# #加密函数书写
# def fake_password_hasher(raw_password:str):
#     return "supersecret"+raw_password
# def fake_save_user(user_in:UserIn):
#     hashed_password = fake_password_hasher(user_in.password)
#     user_in_db=UserInDB(**user_in.dict(),hashed_password=hashed_password)
#     print(user_in_db)
#     print("保存成功！")
#     return user_in_db
#
# @app.post("/user/",response_model=UserOut)
# async def create_user(user_in:UserIn):
#     user_save = fake_save_user(user_in)
#     return user_save
from typing import Union,List
"""union或者anyOf"""
# class BaseItem(BaseModel):
#     description:str
#     type:str
# class CarItem(BaseItem):
#     type = "car"
# class PlaneItem(BaseItem):
#     type = "plane"
#     size:int
# items = {
#     "item1": {"description": "All my friends drive a low rider", "type": "car"},
#     "item2": {
#         "description": "Music is my aeroplane, it's my aeroplane",
#         "type": "plane",
#         "size": 5,
#     },
# }
# @app.get("/items/{item_id}",response_model=Union[PlaneItem,CarItem])
# async def read_item(item_id:str):
#     return items[item_id]

# class Item(BaseModel):
#     name:str
#     description:str
#
# items = [
#     {"name": "Foo", "description": "There comes my hero"},
#     {"name": "Red", "description": "It's my aeroplane"},
# ]
# @app.get("/items/",response_model=List[Item])
# async def read_items():
#     return items
# from typing import Dict
# @app.get("/keyword-weights",response_model=Dict[str,float])
# async def read_keyword_weights():
#     return {"foo":2.3,"bar":3.4}
#
"""响应状态码"""
# @app.get("/items/",status_code=200)
# async def create_item(name:str):
#     return {"name":name}

# @app.get("/items",status_code=status.HTTP_201_CREATED)
# async def create_items(name:str):
#     return {"name":name}

@app.post("/login/")
async def login(username:str = Form(...),password:str=Form(...)):
    return {"username":username}
#
# @app.post('/files')
# async def create_file(file:bytes = File(...)):
#     print(file,114)
#     return {'file_size':len(file)}
#
# @app.post("/uploadfile/")
# async def create_upload_file(file:UploadFile = File(...)):
#     print(file,119)
#     return {"filename":file.filename}

#多文件上传

# from fastapi.responses import HTMLResponse
# @app.post("/files/")
# async def create_files(files: List[bytes] = File(...)):
#     return {"file_sizes": [len(file) for file in files]}
#
#
# @app.post("/uploadfiles/")
# async def create_upload_files(files: List[UploadFile] = File(...)):
#     return {"filenames": [file.filename for file in files]}
#
#
# @app.get("/")
# async def main():
#     content = """
# <body>
# <form action="/files/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# </body>
#     """
#     return HTMLResponse(content=content)


"""同时使用file和form"""
# @app.post("/files")
# async def create_file(files:bytes=File(...),fileb :UploadFile=File(...),token:str = Form(...)):
#     return {
#         "file_size":len(files),
#         "token":token,
#         "file_content_type":fileb.content_type
#     }


"""错误处理"""

# items = {"foo": "The Foo Wrestlers"}
# @app.get("/items/{item_id}")
# async def read_item(item_id:str):
#     if item_id not in items:
#         #headers添加自定义请求头
#         raise HTTPException(status_code=404,detail="item not found",headers={"X-Error": "There goes my error"})
#     return {"item":items[item_id]}
"""安装自定义异常处理器"""

from fastapi.responses import JSONResponse,PlainTextResponse
from fastapi import Request,HTTPException
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
"""
class UnicornException(Exception):
    def __init__(self,name:str):
        self.name=name

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request:Request,exc:UnicornException):
    return JSONResponse(status_code=418,content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."})
@app.get("/unicorns/{name}")
async def read_uvicorn(name:str):
    if name == "haha":
        #会被unicorn_exception_handler函数捕获
        raise UnicornException(name=name)
    return {"unicorn_name":name}
    
"""



"""覆盖默认异常处理器"""




"""

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request,exc):
    '''
    :param request:
    :param exc:      HTTPException对象
    :return:
    '''
    # print(exc,type(exc),210)
    return PlainTextResponse(str(exc.detail),status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request,exc):
    '''

    :param request:
    :param exc:      RequestValidationError对象
    :return:
    '''
    # print(exc,type(exc),221)
    return PlainTextResponse(str(exc),status_code=400)


@app.get("/items/{item_id}")
async def read_item(item_id:int):  #如果参数类型传递错误，走RequestValidationError
    if item_id == 3:    #如果主动报错，走HTTPException
        raise HTTPException(status_code=418,detail="不是3")
    return {'item_id':item_id}
"""

"""
from fastapi.encoders import jsonable_encoder
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request:Request,exc:RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail":exc.errors(),"body":exc.body})
    )

class Item(BaseModel):
    title:str
    size:int
@app.post("/items/")
async def create_item(item:Item):
    return item
"""

"""复用FastAPI异常处理器"""
"""
from fastapi.exception_handlers import (http_exception_handler,request_validation_exception_handler)
@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(reqest,exc):
    print(f"天哪，一个HTTP错误！:{repr(exc)}")
    return await http_exception_handler(reqest,exc)
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request,exc):
    print(f"天哪,客户端发送了无效的数据！:{exc}")
    return await request_validation_exception_handler(request,exc)
@app.get("/items/{item_id}")
async def create_item(item_id:int):
    if item_id == 3:
        raise HTTPException(detail="不能等于3",status_code=418)
    return {"item_id":item_id}

"""

"""
from typing import Set
class Item(BaseModel):
    name:str
    description:Optional[str] = None
    price:float
    tax:Optional[float] = None
    tags:Set[str] = None

@app.post("/items/",response_model=Item,status_code=status.HTTP_201_CREATED)
async def create_item(item:Item):
    return item


"""


from typing import Set
class Item(BaseModel):
    name:str
    description:Optional[str] = None
    price:float
    tax:Optional[float] = None
    tags:Set[str] = None

"""
#tags在swagger文档中对接口进行分类
@app.post("/items/",response_model=Item,tags=["items"])
async def create_item(item:Item):
    return item
@app.get("/items/",tags=["items"])
async def read_items():
    return [{"name":"foo","price":42}]

@app.get("/users/",tags=["users"])
async def read_users():
    return [{"username":"johndoe"}]

"""
"""
#在swagger文档当中对接口进行定义  summary:在接口后面进行定义  description:在接口内部进行定义
@app.post("/items/",response_model=Item,summary="创建一个项目",description="创建一包含名字、描述、价格、税收以及标签的项目")
async def create_item(item:Item):
    return item
"""

"""
@app.post("/items/",summary="创建一个项目",response_model=Item)
async def create_item(item:Item):
    #在接口内部显示，相当于description
    '''
    SV读后感不是的不是那块

    aeds线才意识到刚开始
    安保SV超级爱上大V
    df不补偿款精粹商店
    失败播放进度表

    '''
    return item


"""

"""响应描述"""
"""
@app.post("/items/",response_model=Item,summary="一个新项目",response_description="创建一个新项目")
async def create_item(item:Item):
    '''
     Create an item with all the information:

     - **name**: each item must have a name
     - **description**: a long description
     - **price**: required
     - **tax**: if the item doesn't have tax, you can omit this
     - **tags**: a set of unique tag strings for this item
     '''
    return item

"""


"""
from fastapi.encoders import jsonable_encoder
#jsonable_encoder
fake_db={}
@app.put("/items/{id}")
def update_item(id:int,item:Item):

    json_compatible_item_data = jsonable_encoder(item)#将item对象转为字典
    print(json_compatible_item_data,type(json_compatible_item_data))
    fake_db[id] = json_compatible_item_data

    return item

"""

"""请求体--更新数据"""
"""
items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

from fastapi.encoders import jsonable_encoder
@app.get("/items/{item_id}",response_model=Item)
async def read_item(item_id:str):
    return items[item_id]

@app.put("/items/{item_id}",response_model=Item)
async def update_item(item_id:str,item:Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded
"""
"""用PATCH进行部分更新"""

from fastapi.encoders import jsonable_encoder
items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}
@app.get("/items/{item_id}",response_model=Item)
async def read_item(item_id:str):
    return items[item_id]


@app.patch("/items/{item_id}",response_model=Item)
async def update_item(item_id:str,item:Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item

"""依赖函数Deeped() ：子依赖项和单个依赖项都可以"""

from typing import Optional

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons

"""路径操作装饰器依赖项"""

async def verify_token(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header(...)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]


"""安全性"""
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


import uvicorn
if __name__ == '__main__':
    uvicorn.run("fastapi_learning2:app")
