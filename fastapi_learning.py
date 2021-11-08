# -*-coding:utf-8-*-
from datetime import date
from pydantic import BaseModel

# def main(user_id:str):
#     return user_id
# class User(BaseModel):
#     id:int
#     name:str
#     joined:date
#
# # my_user:User = User(id=1,name="aa",joined="2018-07-19")
# # print(my_user)
# second_user_data={
#     "id":2,
#     "name":"Mary",
#     "joined":"2018-11-29"
# }
# my_second_user=User(**second_user_data)
# print(my_second_user)
from enum import Enum
class ModelName(str,Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def index():
    return {"message":"Hello World"}

@app.get("/item/{item_id}")   #路径中传递参数
async def read_item(item_id:int):   #定义参数类型
    return {"item_id":item_id}
@app.get("/models/{model_name}")
async def get_model(model_name:ModelName):
    # print(model_name.value)  #value值随着路径参数的值改变而改变
    if model_name == ModelName.alexnet:
        return {"model_name":model_name,"message":"DeepLearning FTW"}
    if model_name.value == "lenet":
        return {"model_name":model_name,"message":"LeCNN all the images"}
    return {"model_name":model_name,"message":"Have some residuals"}

@app.get("/files/{file_path:path}")
async def get_file(file_path:str):
    return {"file_path":file_path}


fake_items_db = [{"item_name": i}
                 for i in range(20)

                 ]

"""查询参数"""

#http://127.0.0.1:8000/items/
#http://127.0.0.1:8000/items/?&skip=0&limit=3
# @app.get("/items/")
# async def read_item(skip:int=0,limit:int = 2):
#     return fake_items_db[skip:skip+limit]
from typing import Optional


# http://127.0.0.1:8000/items/1?q=2
# @app.get("/items/{item_id}")
# async def read_items(item_id:str,q:Optional[str] = None):
#     print(q)
#     if q:
#         return {"item_id":item_id,"q":q}
#     return {"item_id":item_id}

#http://127.0.0.1:8000/items/foo?short=1
#http://127.0.0.1:8000/items/foo?short=True
@app.get("/items/{item_id}")
async def read_item(item_id:str,q:Optional[str]=None,short:bool=False):
    '''

    :param item_id:  路由参数
    :param q:        #查询字符串
    :param short:    #查询字符串
    :return:
    '''
    item = {"item_id":item_id}
    if q:
        item.update({"q":q})

    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}

        )
    return item

#多个路径和查询参数
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id:int,item_id:str,q:Optional[str] = None,short:bool = False
):
    item = {"item_id":item_id,"owner_id":user_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
#必须查询参数（不声明默认值即可）
@app.get("/itemed/{item_id}")
async def read_user_items(
        item_id:str,needy:str
):
    item = {"item_id":item_id,"needy":needy}
    return item


@app.get("/itemsed/{item_id}")
async def read_user_itemed(
        item_id:str,needy:str,skip:int = 0,limit:Optional[int]= None
):
    item={"item_id":item_id,"needy":needy,"skip":skip,"limit":limit}
    return item

"""请求体"""
from pydantic import BaseModel
class Item(BaseModel):
    name:str
    description:Optional[str]=None
    price:float
    tax:Optional[float] = None


# @app.post("/item/")
# async def create_item(item:Item):
#     return item

#使用模型
@app.post("/item/")
async def create_item(item:Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax":price_with_tax})
    return item_dict

#请求体加路径参数
@app.put("/put_item/{item_id}")
async def create_put_item(item_id:int,item:Item):
    item_dict = item.dict()
    item_dict.update({"item_id":item_id})
    if item.tax:
        item_dict.update({"total_price":item.tax+item.price+item_id})
    return item_dict

#请求体加路径参数+查询参数

@app.put("/put_items/{item_id}")
async def create_put_items(item:Item,item_id:int,name:str,q:Optional[str]=None):
    item_dict = item.dict()
    item_dict.update({"item_id":item_id,"name":name})
    if q:
        item_dict.update({"q":q})
    return item_dict


#查询参数和字符串校验
@app.get("/get_items/")
async def create_get_items(q:Optional[str] = None):
    results={"items":[{"item_id": "Foo"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results

#额外的校验
from fastapi import Query,Path,Body
@app.get("/get_item")
async def get_read_items(q:Optional[str]=Query(None,max_length=3)):#设置q最大值不超过50位
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/get_item_query")
async def get_read_query_items(q:Optional[str]=Query(None,max_length=5,min_length=2)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#添加正则表达式
@app.get("/get_item_regix")
async def get_read_item_regix(q:Optional[str]=Query(None,min_length=2,max_length=5,regex="^a(.*?)s$")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
#默认值
@app.get("/deault_item")
async def get_read_default_item(q:Optional[str]=Query("lili",max_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
#声明为必须参数
@app.get("/get_require_item")
async def get_read_require_item(q:Optional[str]=Query(...,max_length=5)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
from typing import List


#查询参数列表/多个值
#http://127.0.0.1:8000/get_multiple?q=1&q=2&q=3
@app.get("/get_multiple")
async def get_multiple_item(q:Optional[List[str]]=Query(None)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#具有默认值的查询列表/多个值
#http://127.0.0.1:8000/get_default_mutiple
@app.get("/get_default_mutiple")
async def get_deault_multiple(q:Optional[List[str]]=Query(["Foo","Bar"])):
    query_item = {"q":q}
    return query_item

#也可以使用list代替List
# @app.get("/get_default_mutiple")
# async def get_deault_multiple(q:list=Query(["Foo","Bar"])):
#     query_item = {"q":q}
#     return query_item

#声明更多元数据
@app.get("/get_meta_item")
#title和description给自己描述的
async def get_meta_read_item(q:Optional[str]=Query(None,title="Query string",description="查询字符串且长度小于3",max_length=3)):
    if q:
        return {"q":q}
    return {}
#别名参数
@app.get("/get_alias_item")
#http://127.0.0.1:8000/get_alias_item?item-query=10
#alias使用过后原名称不在生效
async def get_alias_item(q:Optional[str]=Query(None,alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#弃用参数
@app.get("/get_deprecated_item")
async def get_deprecated_item(q:Optional[str]=Query(None,title="查询字符串",description="用该字符串查询数据库",min_length=2,max_length=5,deprecated=True)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#路径参数和数值校验
#路径参数必须是必须的，即使使用None还是必须的
@app.get("/get_path_items/{items_id}")
async def get_path_items(items_id:int = Path(...,title="The ID of the item to get"),
                         q:Optional[str]=Query(None,alias="item-query")):
    result = {"item_id":items_id}
    if q:
        result.update({"q":q})
    return result

# @app.get("/get_sort_items/{item_id}")
# async def get_sort_items(
#     q: str, item_id: int = Path(..., title="The ID of the item to get")
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

@app.get("/get_sort_items/{item_id}")
#第一个参数*代表后续参数以关键字参数(键值对)传递
async def get_sort_items(*,item_id:int =Path(...,title="avschjsdvjhsdfvhj"),q:str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

"""
#数值校验
gt：大于（greater than）
ge：大于等于（greater than or equal）
lt：小于（less than）
le：小于等于（less than or equal）
"""

# @app.get("/get_ge_item/{item_id}")
# async def get_ge_item(
#         *,item_id:int=Path(...,title="teamID",ge=1),q:str):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results
#
"""
请求体 - 多个参数
"""
@app.put("/put_body_item/{item_id}")
async def put_body_item(
        *,
        item_id:int=Path(...,title="获得item_id",ge=0,le=1000),    #路径参数
        q:Optional[str] = None,                                   #查询参数
        item:Optional[Item] = None                                #请求体参数

):
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    if item:
        results.update({"item":item})
    return results



class User(BaseModel):
    name:str
    full_name:Optional[str]=None
    age:int
"""多个请求体参数"""
# @app.put("/get_mutiple_body_item/{item_id}")
# async def get_mutiple_body_item(
#         *,
#         item_id:int = Path(...,title="item id"),   #路径参数
#         item:Item,                                  #请求体1
#         user:User,                                  #请求体2
# ):
#     results={"item_id":item_id,"item":item,"user":user}
#     return results

#将参数作为body参数进行传递

@app.put("/get_mutiple_body_items/{item_id}")
async def get_mutiple_body_items(
        *,
        item_id:int=Path(...,title="item id"),
        item:Item,
        user:User,
        importance:int=Body(...)
):
    results ={"item_id":item_id,"user":user,"item":item,"importance":importance}
    return results
"""多个请求体参数和查询参数"""
@app.put("/get_mutiple_query_items/{item_id}")
async def get_mutiple_query_items(*,
                                  item_id:int=Path(...,title="team id"),
                                  item:Item,
                                  user:User,
                                  importance:int = Body(...),
                                  q:Optional[str] = Query(None,title="查询参数",description="查询数据库",deprecated=True)
                                  ):
    results ={"item_id":item_id,"item":item,"user":user,"importance":importance}
    if q:
        results.update({"q":q})
    return results

"""嵌入单个请求体参数"""
@app.put("/get_single_body_item/{item_id}")
async def get_single_body_item(
        *,
        item_id:int,
        item:Item = Body(...,embed=True)
):
    results={"item_id":item_id,"item":item}
    return results


"""请求体字段"""
from pydantic import Field
#Field:对属性进行描述
class NewItem(BaseModel):
    name:str
    description:Optional[str] = Field(
        None,title="这是一个项目的描述",max_length=300
    )
    price:float = Field(...,gt=0,description="price必须大于0")
@app.put("/get_fields_items/{item_id}")
async def get_fields_items(
        item_id:int,
        item:NewItem = Body(...,embed=True),
):
    results = {"item_id":item_id,"item":item}
    return results

from typing import List,Set,Dict
"""请求体（嵌套模型）"""
class CommonItem(BaseModel):
    name:str
    description:Optional[str] = None
    price:float
    tax:Optional[float] = None
    # tags:list=[]
    # tags:List[str] = []
    tags:Set[str] = set()
@app.put("/nested_item/{item_id}")
async def nested_item(
        item_id:int,
        item:CommonItem
):
    results={"item_id":item_id,"item":item}
    return results


from pydantic import HttpUrl
"""嵌套模型"""

class Image(BaseModel):
    # url:str
    url:HttpUrl   #检查是否是有效的字符串
    name:str
class NestedItem(BaseModel):
    name:str
    description:Optional[str]= None
    price:float
    tax:Optional[str] = None
    tags:Set[str]=[]
    # images:Optional[Image] = None
    images:Optional[List[Image]]=None
@app.put("/get_nested_item/{item_id}")
async def get_nested_item(item_id:int,item:NestedItem):
    results = {"item_id":item_id,"item":item}
    return results


"""深度嵌套模型"""

class DeepImage(BaseModel):
    url:HttpUrl
    name:str
class DeepNestedItem(BaseModel):
    name:str
    description:Optional[str] = None
    price:float
    tax:Optional[str] = None
    tags:Set[str] = set()
    images:Optional[List[DeepImage]] = None
class Offer(BaseModel):
    name:str
    description:Optional[str] = None
    price: float
    items:List[DeepNestedItem]

@app.post("/get_deep_nested_item/{item_id}")
async def get_deep_nested_item(item_id:str,offer:Offer):
    results={"item_id":item_id,"offer":offer}
    return results

"""纯列表请求体"""
class PureImage(BaseModel):
    url:HttpUrl
    name:str
@app.post("/images/multiple/")
async def create_images_multiple(image:List[PureImage]):
    return image
"""任意dict构成的请求体"""
@app.post("/index_weights")
async def create_index_weights(weights:Dict[int,float]):  #接收任意键为int，值为float的数据
    return weights

"""
    模式的额外信息
    Pydantic schema_extra
"""

class ExtraItem(BaseModel):
    name:str
    description:Optional[str] = None
    price:float
    tax:Optional[float] = None
    class Config:
        schema_extra={
            "example":{
                "name":"Foo",
                "description":"A very nice item",
                "price":35.4,
                "tax":3.2
            }
        }
@app.put("/extra_item")
async def update_item(item:ExtraItem):
    return {"item":item}


"""Field的附加参数"""
# example:除了Field之外还可以在Query,Body,Path当中使用
class ExtraFieldItem(BaseModel):
    name:str = Field(...,example="Foo")
    description : Optional[str] = Field(None,example="描述信息")
    price:float = Field(...,example="价格，20.4")
    tax:Optional[float] = Field(...,example=3.2)
@app.put("/extra_field_item")
async def extra_field_item(item:ExtraFieldItem):
    return {"item":item}


"""
    额外数据类型:UUID、datetime、date、frozenset、bytes、Decimal

"""

"""Cookie参数"""
from fastapi import Cookie,Header
@app.get("/cookie_item")
async def cookie_item(ads_id:Optional[str]=Cookie(20)):
    return {"ads_id":ads_id}

"""headers参数"""
@app.get("/header_item")
async def header_item(user_agent:Optional[str]=Header(None)):
    print(user_agent)
    return {"User-Agent":user_agent}

"""重复的 headers"""
@app.get("/get_list_header_item")
async def get_list_header_item(x_token: Optional[List[str]] = Header(None)):
    print(x_token)
    return {"X-Token values": x_token}



@app.get("/items_ll/")
async def items_ll(
    strange_header: Optional[str] = Header(None, convert_underscores=False)
):
    return {"strange_header": strange_header}


from pydantic import EmailStr
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None
# Don't do this in production!
@app.post("/user/", response_model=UserIn)
async def create_user(user: UserIn):
    return user


#添加输出模型
class UserIn(BaseModel):
    username:str
    password:str
    email:EmailStr
    full_name:Optional[str] = None
class UserOut(BaseModel):
    username:str
    email:EmailStr
    full_name:Optional[str] = None
@app.post("/out_user/",response_model=UserOut)
async def create_out_user(
        user:UserIn
):
    return user


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get("/exclude_user/{item_id}",response_model=Item,response_model_exclude_unset=True)
async def exclude_user(
        item_id:str
):
    return items[item_id]


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}
@app.get("/item/{item_id}/name",response_model=Item,response_model_include={"name","description"})
async def read_item_name(item_id:str):
    return items[item_id]

import uvicorn
if __name__ == '__main__':
    uvicorn.run("fastapi_learning:app")




