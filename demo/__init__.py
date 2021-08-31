#!/usr/bin/env python
# coding=utf-8
"""
@Date: 2020-07-29 19:50:48
@LastEditTime: 2020-07-29 20:09:43
@LastEditors: xuhaoqing
@FilePath: /demo/demo/__init__.py
"""

from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()

    def __str__(self):
        return self.name
