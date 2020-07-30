"""
@Author: your name
@Date: 2020-07-30 11:18:41
@LastEditTime: 2020-07-30 15:12:44
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /demo/demo/models/demo.py
"""


from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model


class Demo(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()

    def __str__(self):
        return self.name


Demo_Pydantic = pydantic_model_creator(Demo)
