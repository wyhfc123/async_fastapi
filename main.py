import asyncio
# async def main():
#     print("hello")
#     await asyncio.sleep(1)
#     print("world")
# print(asyncio.run(main()))
import concurrent.futures

import sys
import time
# async def say_after(delay,what):
#     await asyncio.sleep(delay)
#     print(what)
#
# async def main():
#     print(f"started at {time.strftime('%X')}")
#
#     await say_after(1,"hello")
#     await say_after(2,"world")
#     print(f"end at {time.strftime('%X')}")


# asyncio.run(main())
#asyncio.create_task() 函数用来并发运行作为 asyncio 任务 的多个协程。
# import time
#
#
# async def say_after(delay,what):
#     await asyncio.sleep(delay)
#     print(what)
# async def main():
#     task1 = asyncio.create_task(say_after(1,"hello"))
#     task2 = asyncio.create_task(say_after(2,"world"))
#     print(f"started at {time.strftime('%X')}")
#
#     await task1
#     await task2
#     print(f"end at {time.strftime('%X')}")
#
#
# asyncio.run(main())
# async def nested():
#     return 42
#
# async def factorial(name,number):
#     f=1
#     for i in range(2,number+1):
#         print(f"Task {name}: Compute factorial({i})...")
#         await asyncio.sleep(1)
#         f*=i
#     print(f"Task {name}: factorial({number}) = {f}")


# async def main():
    # nested()
    # print(await nested())
    # task = asyncio.create_task(nested())
    # await task
    # await function_that_returns_a_future_object()
    # await asyncio.gather(factorial("A",2),factorial("B",3),factorial("C",4))

# asyncio.run(main())
#
# print(sys.platform)


# async def func1():
#     print(1)
#     await asyncio.sleep(1)
#     print(2)
# async def func2():
#     print(3)
#     await asyncio.sleep(1)
#     print(4)
# asyncio.run(func1())
# asyncio.run(func2())



#greenlet 实现协程
# from greenlet import greenlet
# def func1():
#     print(1)
#     gr2.switch()
#     print(2)
#     gr2.switch()
# def func2():
#     print(3)
#     gr1.switch()
#     print(4)
# gr1 = greenlet(func1)
# gr2 = greenlet(func2)
# gr1.switch()

#yield关键字实现协程

# def func1():
#     yield 1
#     yield from func2()
#     yield 2
# def func2():
#     yield 3
#     yield 4
# f1 =func1()
# for item in f1:
#     print(item)

#asyncio实现协程
# @asyncio.coroutine
# def func1():
#     print(1)
#     yield from asyncio.sleep(2)
#     print(2)
# @asyncio.coroutine
# def func2():
#     print(3)
#     yield from asyncio.sleep(2)
#     print(4)
# task = [
#     asyncio.ensure_future(func1()),
#     asyncio.ensure_future(func2())
# ]
# loop =asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(task))


#async & await 关键字
# async def func1():
#     print(1)
#     await asyncio.sleep(2)
#     print(2)
# async def func2():
#     print(3)
#     await asyncio.sleep(2)
#     print(4)
# task = [
#     asyncio.ensure_future(func1()),
#     asyncio.ensure_future(func2())
# ]

# 等于asyncio.run(task)
# loop =asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(task))



#await 必须是可调用对象：协程对象，future对象 Task对象


#ensure_future()函数作用和create_task()函数作用相同

# async def func1():
#     print(3)
#     await asyncio.sleep(1)
#     print(4)
#     return "结束"
#
#
# async def func():
#     print(1)
#     await asyncio.sleep(1)
#     print(2)
#     return "结束"
# async def main():
#     print("main开始")
#     task1 = asyncio.create_task(func())
#     task2 = asyncio.create_task(func1())
#     print("main结束")
#     await task1
#     await task2
# asyncio.run(main())


# async def func1():
#     print(3)
#     await asyncio.sleep(1)
#     print(4)
#     return "结束"
#
#
# async def func():
#     print(1)
#     await asyncio.sleep(1)
#     print(2)
#     return "结束"
# async def main():
#     print("main开始")
#     task_list = [
#                 asyncio.create_task(func()),
#                 asyncio.create_task(func1())
#     ]
#     print("main结束")
#     #syncio.wait() 等待任务列表完成任务
#     done,pedding=await asyncio.wait(task_list,timeout=1)
#     # print(done,pedding)
# asyncio.run(main())


#Task对象（并发的调度当前的协程）
# asyncio.create_task([协程对象])

# async def func():
#     print(1)
#     await asyncio.sleep(1)
#     print(2)
#     return "返回值"
#
# task_list=[
#     func(),
#     func(),
# ]
# asyncio.run(asyncio.wait(task_list))

#future对象
# async def main():
#     loop = asyncio.get_running_loop()
#     fut = loop.create_future()
#     await fut
# asyncio.run(main())


# async def set_after(fut):
#     await asyncio.sleep(2)
#     fut.set_result("666")
# async def main():
#
#     #获得当前事件循环
#     loop = asyncio.get_running_loop()
#
#     #创建一个任务（Future对象），没绑定任何行为，那这个任务永远不知道什么时候结束
#     fut = loop.create_future()
#     #创建一个任务(Task对象),绑定了set_after()函数，函数内部在2s之后，会给fut赋值
#     #即手动设置future任务的最终结果，那么fut就可以结束了
#     await loop.create_task(set_after(fut))
#     #等待Future对象获取最终结果，否则一致等待下去
#     data = await fut
#     print(data)
# asyncio.run(main())

# concurrent的Future对象(使用进程池或线程池异步才使用的操作对象 )
# import time
# from concurrent.futures import Future
# from concurrent.futures.thread import ThreadPoolExecutor
# from concurrent.futures.process import ProcessPoolExecutor
# def func(value):
#     time.sleep(1)
#     print(value)
# #创建线程池
# pool = ThreadPoolExecutor(max_workers=5)
# #创建进程池
# pool = ProcessPoolExecutor(max_workers=5)
# for i in range(10):
#     fut = pool.submit(func,i)
#     print(fut)
#

# concurrent的Future对象和asyncio的Future对象合用
# def func1():
#     time.sleep(1)
#     return "68"
# async def main():
#     loop = asyncio.get_running_loop()
#
#     #第一步会先调用ThreadPoolExecutor的submit方法去线程池申请一个线程去执行func1函数，并返回一个concurrent.futures.Future对象
#     #第二步调用asyncio.wrap_future()将个concurrent.futures.Future对象包装为asyncio.Future对象
#     #因为concurrent.futures.Future对象不支持await语法，所以需要包装为asyncio.Future对象才能使用
#
#     fut = loop.run_in_executor(None,func1)
#     result = await fut
#
#     print("default thread pool",result)
#     #运行一个线程池客户端
#     # with concurrent.futures.ThreadPoolExecutor() as pool:
#     #     result =await  loop.run_in_executor(pool,func1)
#     #     print("线程池客户端",result)
#     #运行一个进程池客户端
#     # with concurrent.futures.ProcessPoolExecutor() as pool:
#     #     result =await  loop.run_in_executor(pool,func1)
#     #     print("线程池客户端",result)
#
#
# asyncio.run(main())


# asyncio+不支持异步的模块
# import requests
# async def download_image(url):
#     print("开始下载",url)
#     loop = asyncio.get_event_loop()
#     future = loop.run_in_executor(None,requests.get,url)
#     response = await future
#     print("下载完成",response.content)
#
# if __name__ == '__main__':
#     url_list=[
#         "https://gd1.alicdn.com/imgextra/i4/634870620/O1CN01c09HGu1GS0GNhGGb8_!!634870620.jpg_400x400.jpg",
#         "https://gd3.alicdn.com/imgextra/i1/634870620/O1CN013QK25e1GS0B7KTUCU_!!634870620.jpg_400x400.jpg",
#         "https://gd3.alicdn.com/imgextra/i3/2206409749051/O1CN01IUa63W2GjPUWHC8mW_!!2206409749051.jpg_400x400.jpg"
#     ]
#     tasks = [download_image(url) for url in url_list]
#     asyncio.run(asyncio.wait(tasks))
#aiohttp版本
import aiohttp
async def download_image(session,url):
    print("开始下载",url)
    async with session.get(url,verify_ssl=False) as response:
        content = await response.content.readuntil()


        print("下载完成",content)

async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
            "https://gd1.alicdn.com/imgextra/i4/634870620/O1CN01c09HGu1GS0GNhGGb8_!!634870620.jpg_400x400.jpg",
            "https://gd3.alicdn.com/imgextra/i1/634870620/O1CN013QK25e1GS0B7KTUCU_!!634870620.jpg_400x400.jpg",
            "https://gd3.alicdn.com/imgextra/i3/2206409749051/O1CN01IUa63W2GjPUWHC8mW_!!2206409749051.jpg_400x400.jpg"
        ]
        tasks = [asyncio.create_task(download_image(session,url)) for url in url_list]
        done,pending = await asyncio.wait(tasks)
if __name__ == '__main__':


    asyncio.run(main())



#异步迭代器(实现了__aiter__()和__anext__()方法)

# class Reader(object):
#     def __init__(self):
#         self.count = 0
#     async def readline(self):
#         self.count+=1
#         if self.count == 100:
#             return None
#         return self.count
#     def __aiter__(self):
#         return self
#     async def __anext__(self):
#         val = await self.readline()
#         if not val:
#             raise StopAsyncIteration
#         return val
#
#
# async def func():
#     r = Reader()
#     #async必须在协程函数内
#     async for item in r:
#         print(item)
# asyncio.run(func())




#异步上下文管理器__aenter__()和__anext__()
# import pymysql
# class AsyncContextManager:
#     def __init__(self,conn=None,user=None,host = None,password = None,database=None):
#         self.conn = conn
#         self.user = user
#         self.password = password
#         self.host = host
#         self.database = database
#     async def do_thing(self,sql):
#         cursor = self.conn.cursor()
#         cursor.execute(sql)
#
#         return cursor.fetchone()
#
#     async def __aenter__(self):
#
#         self.conn = pymysql.connect(host= self.host,
#                                     user=self.user,
#                                     password=self.password,
#                                     database=self.database)
#
#         return self
#     async def __aexit__(self, exc_type, exc_val, exc_tb):
#         #异步关闭数据库链接
#         self.conn.close()
#         await asyncio.sleep(1)
#
# async def func():
#     async with AsyncContextManager(host="127.0.0.1", user="root", password="123456", database="bp_flask") as f:
#         result = await f.do_thing("select * from bp")
#         print(result)
# asyncio.run(func())
#上下文管理器代码
# class Resource():
#     def __enter__(self):
#         print('===connect to resource===')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#
#
#         print('===close resource connection===')
#
#     def operate(self):
#         print('===in operation===')
#
#
# with Resource() as res:
#     res.operate()


# uvloop(是asyncio事件循环的替代方案，大于asyncio的事件循环)
# import uvloop
# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
# asyncio.run(...)

# import aioredis
# #异步操作Redis(安装aioredis)
# async def excute(address,password):
#     print("开始执行",address)
#     redis = await aioredis.from_url(address,password=password)
#     # async with redis.client() as conn:
#     #     await conn.hmset("car", {"key1": 1, "key2":2, "key3": 3})
#
#     await redis.hmset("car", {"key1": 1, "key2": 3, "key3": 3})
#     #网络IO操作，去redis中获取值
#         # result = await conn.hgetall("car")
#     result = await redis.hgetall("car")
#     print(result)
# task_list=[
# excute("redis://localhost",""),
# excute("redis://localhost","")
# ]
# asyncio.run(asyncio.wait(task_list))


# #异步操作MySQL(安装aiomysql)
# import aiomysql
#
#
# async def excute(host,password):
#     #网络IO操作，连接MySQL
#     conn = await aiomysql.connect(host=host,port=3306,user="root",password=password,db="kcc")
#     cur = await conn.cursor()
#     await cur.execute("select * from bp")
#     #网络io操作，获取sql结果
#     result = await cur.fetchall()
#     print(result)
#     await cur.close()
#     conn.close()
#
# task_list=[
# excute("127.0.0.1","123456"),
# excute("127.0.0.1","123456"),
# ]
# asyncio.run(asyncio.wait(task_list))
