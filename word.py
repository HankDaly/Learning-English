from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine, Integer, MetaData

#定义User对象
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