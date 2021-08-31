"""
@Date: 2020-07-30 11:29:05
@LastEditTime: 2020-07-30 15:14:25
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /demo/demo/views/demo_view.py
"""

from fastapi import APIRouter

from demo.models.demo import Demo, Demo_Pydantic

demo_router = APIRouter()


@demo_router.get("/hs")
async def check_hs():
    return {"msg": "ok"}


@demo_router.get("/demo/{id}")
async def get_demo(id: int):
    return await Demo_Pydantic.from_queryset_single(Demo.get(id=id))
