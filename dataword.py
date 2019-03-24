from sqlalchemy import Column, String, create_engine, Integer, MetaData, and_, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import random


#创建对象的基类
Base = declarative_base()
#创建对象
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
engine = create_engine('sqlite:///foo.db',echo=False)

#创建数据库
metadata = MetaData(engine)

DBSession = sessionmaker(bind=engine)

#背中文
def get_chinese(session,text):
    q = False
    txt_name = None
    print('现在有这么多单词表哦! ',text)

    while(txt_name not in text):
        txt_name = str(input("今天想要背哪个呢?_?"))
    list1 = session.query(Word).filter(Word.textname == txt_name).all()

    while q != True:
        if len(list1) == 0:
            break
        a = random.choice(list1)
        print(a.ont,":\n")
        print('英文解释: ',a.englishmean,"\n")
        print('例句一: ',a.sentence1,"\n")
        print('例句二:',a.sentence2,"\n")
        print('请写出   '+a.ont+'   的中文意思')
        chinese_mean = input('在此处写入')
        if chinese_mean == a.mean:
            list1.remove(a)
            print('正确')
        else:
            print('错误')
            print(a.mean)
            a.wrong_number += 1
            a.temp_wrongnumber += 1
        q = input('输入任意键继续，输入True退出')
        if q == 'True':
            session.commit()
            q = True

#背英文
def get_english(session,text):
    q = False
    txt_name = None
    print('现在有这么多单词表哦! ',text)

    while(txt_name not in text):
        txt_name = str(input("今天想要背哪个呢?_?"))
    list1 = session.query(Word).filter(Word.textname == txt_name).all()

    while q != True:
        if len(list1) == 0:
            break
        a = random.choice(list1)
        print('请写出   '+a.mean+'   的英文')
        english_ont = input('在此处写入')
        if english_ont == a.ont:
            list1.remove(a)
            print('正确')
            print(a.ont)
            print(a.mean,"\n")
            print('英文解释: ',a.englishmean,"\n")
            print('例句一: ',a.sentence1,"\n")
            print('例句二:',a.sentence2,"\n")
 
        else:
            print('错误')
            print(a.ont)
            print(a.mean,"\n")
            print('英文解释: ',a.englishmean,"\n")
            print('例句一: ',a.sentence1,"\n")
            print('例句二:',a.sentence2,"\n")
            a.wrong_number += 1
            a.temp_wrongnumber += 1
        q = input('输入任意键继续，输入True退出')
        if q == 'True':
            session.commit()
            q = True

#看统计
def get_statistics(session,text):
    q = False
    txt_name = None
    print('现在有这么多单词表哦! ',text)

    while(txt_name not in text):
        txt_name = str(input("想要看哪个单词表的统计呢?_?"))
    list1 = session.query(Word).filter(Word.textname == txt_name).all()

    while q != True:
        list1 = sorted(list1,key = lambda x: x.temp_wrongnumber,reverse = True)
        for i in list1:
            print("%10s %10s %10s %10s" %(i.ont,i.mean,'本次错误次数:'+str(i.temp_wrongnumber),'历代错误次数:'+str(i.wrong_number)))
        q = input('输入任意键继续，输入True退出')
        if q == 'True':
            q = True

#添加例句
def add_sentence(session,text):
    q = False
    txt_name = None
    print('现在有这么多单词表哦! ',text)

    while(txt_name not in text):
        txt_name = str(input("想要给哪个单词表添加例句呢?_?"))
    list1 = session.query(Word).filter(and_(
        Word.textname == txt_name,
        or_(Word.englishmean == None,Word.sentence1 == None,Word.sentence2 == None)
        )).all()

    for i in list1:
        print(i.ont," ",i.mean)
        i.englishmean = input('输入单词的英文意思')
        i.sentence1 = input('例句一')
        i.sentence2 = input('例句二')
        q = input('输入任意键继续，输入True退出')
        if q == 'True':
            break
    print("都添加完啦")
    session.commit()


def main():
    print('(* v *)单词测试升级版开始啦~~')
    session = DBSession() #数据库会话
    query = session.query(Word).all()
    text = []
    text_name = None
    for i in query:
        if(i.textname not in text):
            text.append(i.textname)
    flag1 = False
    #
    while flag1 == False:
        flag2 = False
        while flag2 == False:
            g = str(input('a.添加单词.\nb.给英文猜中文.\nc.给中文猜英文.\nd.统计错误.\ne.添加例句\nf.退出'))
            if g in ['a','b','c','d','e','f']:
                flag2 = True
            else:
                print('请重新输入哦')
    #
        if g == 'a' :
            ont = input('输入要添加的英文')
            mean = input('输入单词的中文')
            englishmean = input('输入单词的英文意思')
            sentence1 = input('例句一')
            sentence2 = input('例句二')
            textname = input('想存到哪儿呢?')
            word = Word(ont = ont,mean = mean,englishmean = englishmean,sentence1 = sentence1,sentence2 = sentence2,textname = textname)
            session.add(word)
            session.commit()

        elif g == 'b' :
            get_chinese(session,text)
        elif g == 'c' :
            get_english(session,text)
        elif g == 'd' :
            get_statistics(session,text)
        elif g == 'e' :
            add_sentence(session,text)
        elif g == 'f' :
            #将临时的错误统计都置零
            list1 = session.query(Word).all()
            for i in list1:
                i.temp_wrongnumber = 0
            session.commit()
            #关闭会话
            session.close
            flag1 = True

if __name__ == "__main__":
    main()