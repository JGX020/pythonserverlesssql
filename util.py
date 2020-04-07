# -*- coding: utf-8 -*-
from flask import Blueprint,request,Flask
import os
import json
import datetime
import platform
import csv
import os
import traceback
import yaml
from flask_sqlalchemy import SQLAlchemy
import uuid
import settings

data = Blueprint('register', __name__)
# wuhan2020文件夹为https://github.com/wuhan2020/wuhan2020项目文件的本地clone
# 阿里云serverless使用挂载nas远程目录来存放缓存文件；在本机调试时，缓存文件夹将存放在项目根目录


    
app = Flask(__name__)
app.config.from_object(settings)
db = SQLAlchemy(app)


"""
Tools
"""
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

@data.route('/create')
def hospital_list():
    resp = {
        'success': False,
        'data': [],
        'msg': 'create success',
    }
    db.create_all()
    return json.dumps(resp, ensure_ascii=False)
@data.route('/delete')
def hospital_delete():
    resp = {
        'success': False,
        'data': [],
        'msg': 'delete success',
    }
    db.drop_all()
    return json.dumps(resp, ensure_ascii=False)    
