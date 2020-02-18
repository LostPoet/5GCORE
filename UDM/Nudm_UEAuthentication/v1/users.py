from sqlalchemy import VARBINARY, VARCHAR
from sqlalchemy.sql.schema import Column
from sqlalchemy.types import String

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
import mysql.connector

# 初始化数据库连接:
# 这里一定要用pymysql连接数据库，mysqlconnector取VARBINARY数据时会进行decode导致报错
engine = create_engine('mysql+pymysql://root:@localhost:3306/oai_db',)

Base = declarative_base()

# 定义User对象:
class Users(Base):
    # 表的名字:
    __tablename__ = 'users'

    # 表的结构:
    #id = Column(String(20), primary_key=True)
    #name = Column(String(20))
    #sqn = Column(BigInteger(20))
    OPc =  Column(VARBINARY(16))
    imei = Column(VARCHAR(15))
    imsi = Column(String(15),primary_key = True)
    mmeidentity_idmmeidentity = Column(VARCHAR(15))
    msisdn = Column(VARCHAR(15))

if __name__ == '__main__':

     # 建表
     def create():
          Base.metadata.create_all(engine)

     create()

     # 创建DBSession类型:
     DBSession = sessionmaker(bind=engine)
     # 创建session对象:
     session = DBSession()

     # 插入新Users对象
     def add():
          # 创建新Users对象:
          new_user = Users(imsi='208930000000002',imei='351751102746693',OPc=bytes.fromhex('e734f8734007d6c5ce7a0508809e7e9c'),msisdn='msisdn789012345',mmeidentity_idmmeidentity='012345678912345')
          # 添加到session:
          session.add(new_user)
          # 提交即保存到数据库:
          session.commit()

     # 查询插入的对象，测试用
     def query():
          user = session.query(Users).filter(Users.imsi=='208930000000002').one()
          print('type:',type(user))
          print('imei:',type(user.imei))
          print('OPc:',type(user.OPc))
          opc = bytes().fromhex('e734f8734007d6c5ce7a0508809e7e9c')
          print((opc))
          if user.OPc == opc:
               print('hhhhhh')
          else:
               print('eeeeee')

     add()
     query()

     # 关闭session:
     session.close()
