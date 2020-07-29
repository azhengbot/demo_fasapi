#!/usr/bin/env python
# coding=utf-8
'''
@Author: xuhaoqing
@Date: 2020-07-29 19:49:20
@LastEditTime: 2020-07-29 20:12:04
@LastEditors: xuhaoqing
@FilePath: /demo/main.py
'''

from demo.app import create_app

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000

app = create_app()


