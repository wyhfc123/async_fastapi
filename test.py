# -*-coding:utf-8-*-
import json

import requests
# data={
#     "name": "laxcasdcll",
#     "price": 21.333,
#     "tax":20
# }
# data=json.dumps(data)


# data = requests.post("http://127.0.0.1:8000/item/",data=data).json()
# print(data)

# data = requests.put("http://127.0.0.1:8000/put_item/2",data=data).json()
# print(data)

# data = requests.put("http://127.0.0.1:8000/put_items/1?name=lili",data=data).json()
# print(data)

# data = requests.put("http://127.0.0.1:8000/put_body_item/2?q=2222",data=data).json()
# print(data)
# user={
#     "name":"张三",
#     "age":18
# }
# data={
#     "item":{
#     "name": "laxcasdcll",
#     "price": 21.333,
#     "tax":20
#     },
#     "user":{
#     "name":"张三",
#     "age":18
# }
# }
# data = json.dumps(data)
# data = requests.put("http://127.0.0.1:8000/get_mutiple_body_item/2",data=data).json()
# print(data)


# data={
#     "item":{
#     "name": "laxcasdcll",
#     "price": 21.333,
#     "tax":20
#     },
#     "user":{
#     "name":"张三",
#     "age":18
#     },
#     "importance":1
# }
# data = json.dumps(data)
# data = requests.put("http://127.0.0.1:8000/get_mutiple_body_items/2",data=data).json()
# print(data)


# data={
#     "item":{
#     "name": "laxcasdcll",
#     "price": 21.333,
#     "tax":20
#     },
#     "user":{
#     "name":"张三",
#     "age":18
#     },
#     "importance":5
# }
# data = json.dumps(data)
# data = requests.put("http://127.0.0.1:8000/get_mutiple_query_items/2/?q=20",data=data).json()
# print(data)

# data={
#     "item":{
#         "name": "lili",
#     "price": 21.333,
#     }
# }
# data=json.dumps(data)
# data = requests.put("http://127.0.0.1:8000/get_single_body_item/3",data=data).json()
# print(data)

# data={
#     "item":{
#         "name":"Tom",
#         "price":22.1,
#         "description":"工资薪水"
#     }
# }
# data = json.dumps(data)
# data = requests.put("http://127.0.0.1:8000/get_fields_items/3",data=data).json()
# print(data)

# data={
#
#         "name":"Tom",
#         "price":22.1,
#         "description":"工资薪水",
#         "images":[{
#                 "url":"http://www.baidu.com",
#                 "name":"百度图片"
#         }]
#
# }
# data = json.dumps(data)
# data = requests.put("http://127.0.0.1:8000/nested_item/3",data=data).json()
# print(data)

# data = requests.put("http://127.0.0.1:8000/get_nested_item/3",data=data).json()
# print(data)


# data={
#
#         "name":"Tom",
#         "price":22.1,
#         "description":"工资薪水",
#         "items":[
#                 {
#                         "name":"item1",
#                         "description":"this is items",
#                         "price":33.5,
#                         "tax":"1",
#                         "tags":["Apples","origin","Banner"],
#                         "images":[
#                         {
#                                 "url":"http://www.baidu.com",
#                                 "name":"百度图片"
#                                 }
#                         ]
#
#                  }
#         ]
#
# }
# data = json.dumps(data)
# data = requests.post("http://127.0.0.1:8000/get_deep_nested_item/3",data=data).json()
# print(data)


# data=[{
#         "url":"http://www.baidu.com",
#         "name":"百度一下"
# }]
# data = json.dumps(data)
# data = requests.post("http://127.0.0.1:8000/images/multiple/",data=data).json()
# print(data)


# data={
#         1:1.1,
#         2:3.333
# }
# data = json.dumps(data)
# data = requests.post("http://127.0.0.1:8000/index_weights",data=data).json()
# print(data)


# data={
#         "name":"zhang3",
#         "price":22.1
# }
# data = json.dumps(data)
# data = requests.put("http://127.0.0.1:8000/extra_item",data=data).json()
# print(data)

# cookies = dict(ads_id='11111111')
# data = requests.get("http://127.0.0.1:8000/cookie_item",cookies=cookies).json()
# print(data)
# headers = dict(user_agent="aaaa")
#
# data = requests.get("http://127.0.0.1:8000/header_item",headers=headers).json()
# print(data)





# data = requests.get("http://127.0.0.1:8000/get_list_header_item",headers=headers).json()
# print(data)


data={
    "username":"WYH",
    "password":"123",
    "email":"w1792102245@163.com",
    "full_name":None
}

# # data = requests.post("http://127.0.0.1:8000/item/foo/name",data=json.dumps(data)).json()
# # print(data)
# data = requests.post("http://127.0.0.1:8000/user/",data=json.dumps(data)).json()
# print(data)
# from pydantic import BaseModel,EmailStr
# from typing import Optional
#
#
# class UserIn(BaseModel):
#     username:str
#     password:str
#     email:EmailStr
#     full_name:Optional[str] = None
#
# user_in = UserIn(username="john", password="secret", email="john.doe@example.com")
# print(user_in.dict())


# data={
#     "username":"zhang3",
#     "password":"123"
#
# }
#
# data = requests.post("http://127.0.0.1:8000/login/",data=data).json()
# print(data)

# import requests
# url = "http://127.0.0.1:8000/uploadfile"
# path = "C:/Users//123456/Desktop/photo-1476908965434-f988d59d7abd.jpg"
# files = {'file': open(path, 'rb')}
# r = requests.post(url, files=files)
# print(r.url,r.text)

# data={
#   "title": "towel",
#   "size": "XL"
# }
# data=requests.post("http://127.0.0.1:8000/items/",data=json.dumps(data)).json()
# print(data)

# data={
#     "name":"zhang3",
#     "price":22.1
# }
# data=requests.put("http://127.0.0.1:8000/items/1",data=json.dumps(data))
# print(data.json())


# data={
#         "name":"foo",
#     "price":22.1
# }
# data=requests.put("http://127.0.0.1:8000/items/foo",data=json.dumps(data))
# print(data.json())


# data=requests.patch("http://127.0.0.1:8000/items/foo",data=json.dumps(data))
# print(data.json())
# nums=input("请输入整数a:").split(" ")
# a = int(nums[0])
# b = int(nums[1])
# if a<-10**6:
#     raise ValueError("超出数值范围")
# if b>10**6:
#     raise ValueError("超出数值范围")
# print("{:,d}".format(a+b))









