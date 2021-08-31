#!/usr/bin/env python
# coding=utf-8
"""
@Date: 2020-07-29 19:47:35
@LastEditTime: 2020-07-30 14:53:14
@LastEditors: Please set LastEditors
@FilePath: /demo/demo/app.py
"""

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from demo.views.demo_view import demo_router

TORTOISE_ORM = {
    "connections": {"default": "mysql://root:rubik123@127.0.0.1:3306/demo"},
    "apps": {"models": {"models": ["demo.models.demo"], "default_connection": "default"}},
}


def create_app():
    app = FastAPI()
    register_tortoise(app, config=TORTOISE_ORM, generate_schemas=True)

    app.include_router(demo_router)

    return app
