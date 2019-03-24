# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, create_engine, Integer, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import re
import random
import os

def read_word(list_path,text):
    with open(list_path,'r',encoding = 'UTF-8-sig') as f:
        a = f.read()
        list1 = re.split(r';',str(a))
        del list1[-1]
        list_word = []
        for z in list1:
            h = re.split(r':',z)
            list_word.append(h)
    for z in list_word:
        word = Word(ont = z[0],mean = z[1],textname = text)
        session.add(word)

#将txt数据转移到数据库中
def removedata():
    list_path = os.path.join(os.getcwd(),'origin')
    filename = os.listdir(list_path)
    #去掉不是txt的文件
    for z in filename:
        if not re.search(r".txt",z):
            filename.remove(z)
    #
    for i in filename:
        end_path = os.path.join(list_path,i)
        read_word(end_path,i)
    session.commit()    

Base = declarative_base()
class Word(Base):
    #表名
    __tablename__ = 'word'

    #表的结构
    id = Column(Integer,primary_key=True)
    ont = Column(String(20)) #英文
    mean = Column(String(20))  #中文
    englishmean = Column(String(50),default = None) #英文解释
    wrong_number = Column(Integer,default = 0) #总错误次数
    temp_wrongnumber = Column(Integer,default = 0) #本次错误次数
    sentence1 = Column(String(50),default = None) #储存例句1
    sentence2 = Column(String(50),default = None) #储存例句2
    textname = Column(String(10)) #储存该单词所在组
#创建数据库连接
engine = create_engine('sqlite:///foo.db',echo=True)

#创建数据库
metadata = MetaData(engine)

DBSession = sessionmaker(bind=engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

session = DBSession() #数据库会话

removedata()
print(session.query(Word).count())
session.close    

'''
new_word = Word(ont='human',mean='人',wrong_number=0,temp_wrongnumber=0)
session.add(new_word)
session.commit()
session.close()

session = DBSession()
name = session.query(Word).all()

for i in range(0,len(name)):
    print(name[i].ont,name[i].mean,name[i].sentence)
'''