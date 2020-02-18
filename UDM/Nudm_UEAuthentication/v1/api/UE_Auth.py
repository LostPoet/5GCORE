# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import operator
from flask import request, g
import requests
import json
from flask_restful import Resource,reqparse

from sqlalchemy import Column, String, create_engine,LargeBinary
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# 原代码从tables中读取表结构
# from .. import tables
# 自定的users类型，仅满足此api，后续可能需要修改
from .. import users

parser = reqparse.RequestParser()
parser.add_argument('imsi')
parser.add_argument('key')
parser.add_argument('opc')

CurrentPath = "~/5GCORE/UDM/Nudm_UEAuthentication/v1/api/UE_Auth.py"

class UEAUTH(Resource):
    def __init__(self):
    	pass 
    def post(self):
        args = parser.parse_args()
        print(CurrentPath+":29   [UDM][INFO]   "+"receive AUSF get mysql infos with imsi("+args['imsi']+")")
        print(CurrentPath+":30   [UDM][INFO]   "+"create engine to connect mysql")
        # 数据库信息
        engine = create_engine('mysql+pymysql://root:@localhost:3306/oai_db')
        DBSession = sessionmaker(bind=engine)
        # 创建session对象:
        session = DBSession()
        # users = session.query(tables.Users).filter(tables.Users.imsi==args['imsi']).one()
        user = session.query(users.Users).filter(users.Users.imsi==args['imsi']).one()
        print(CurrentPath+":36   [UDM][INFO]   "+"infos about imsi("+args['imsi']+") in mysql as following")
        print("\n\n|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print("|                                                                       mysql user infos where imsi = "+args['imsi']+"                                                                 |")
        print("|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print("|        imsi        |         msisdn       |         imei        | mmeidentity_idmmeidentity |                      key                    |                     OPc                 |")
        print("|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")        
        print("|   "+user.imsi+"  |       "+user.msisdn+"    |    "+user.imei+"   |                 "+str(user.mmeidentity_idmmeidentity)+"         |        "+"0x8baf473f2f8fd09487cccbd7097c6862"+"   |    "+"0xe734f8734007d6c5ce7a0508809e7e9c"+"   |")       
        print("|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n\n") 
        data = {'imsi':user.imsi,'msisdn':user.msisdn,'key':'8baf473f2f8fd09487cccbd7097c6862','opc':'e734f8734007d6c5ce7a0508809e7e9c'}        
        return (json.dumps(data))
