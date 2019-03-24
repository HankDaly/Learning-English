'''给自己做个能背单词的系统'''
#功能一，有记录错误次数的功能
#功能二，有抽背的功能
#功能三，可以按意思抽，可以按单词抽
import re
import random
import os
class Word():
    '''定义单词类'''
    def __init__(self,ont,mean):
        #单词的属性有英文（ont）意思（中文）和总错误次数还有临时错误次数
        self.ont = ont
        self.mean = mean
        self.wrong_number = 0
        self.te_wrong_number = 0

class Word_list():
    '''定义词库，所有的词都放在这'''
    def __init__(self):
        #一开是空列表，需要后续添加
        self.list = []

    #定义一个添加单词的方法
    def add_word(self,word):
        if word not in self.list:
            self.list.append(word)
            print('添加成功')
        else:
            print('单词重复了')
    #定义一个方法，按字母序排列
    def sort_list(self):
        self.list = sorted(self.list,key = lambda x : x.ont)
    #定义一个方法，能按照总错误次数排序
    def wrong_list(self):
        f = self.list[:]
        f2 = sorted(f,key = lambda x : x.wrong_number,reverse = True)
        for z in f2:
            print(str(z.ont)+str(z.mean)+str(z.wrong_number))

    #定义一个方法，随机抽取单词，根据英文得到中文
    def get_chinese(self):
        q = False
        list1 = self.list[:]
        while q != True:
            if len(list1) == 1:
                    list1 = self.list[:]
            a = random.choice(list1)

            print('请写出   '+a.ont+'   的中文意思')
            chinese_mean = input('在此处写入')
            if chinese_mean == a.mean:
                list1.remove(a)
                print('正确')
            else:
                print('错误')
                print(a.mean)
                a.wrong_number += 1
            q = input('输入任意键继续，输入True退出')
            if q == 'True':
                q = True


    #定义一个方法，随机抽取单词，根据中文得到英文
    def get_english(self):
        q = False
        list1 = self.list[:]
        while q != True:
            if len(list1) == 1:
                list1 = self.list[:]
            a = random.choice(list1)
            
            print("请写出   "+a.mean+'   的英文')
            english_mean = input('在此处写入')
            if english_mean == a.ont:
                list1.remove(a)
                print('正确')
            else:
                print('错误')
                print(a.ont)
                a.wrong_number += 1
            q = input('输入任意键继续，输入True退出')
            if q == 'True':
                q = True
    #定义一个方法，能够读取上一次保存的词组列表
    def read_word(self):
        with open(list_path,'r',encoding = 'UTF-8-sig') as f:
            a = f.read()
            list1 = re.split(r';',str(a))
            del list1[-1]
            list_word = []
            for z in list1:
                h = re.split(r':',z)
                list_word.append(h)
        for z in list_word:
            word1 = Word(z[0],z[1])
            self.list.append(word1)
    #定义一个方法，能够写入到文件
    def write_word(self):
        q = str()
        for z in self.list:
            j = str(z.ont+':'+z.mean+';')
            q += j
        with open(list_path,'w',encoding = 'UTF-8-sig') as f:
            f.write(q)

#主程序
print('单词测试开始')
q = False
#处理单词表
filename = os.listdir()
for z in filename:
    if not re.search(r".txt",z):
        filename.remove(z)
print("目前有下列单词表")
print(filename)
txt_name = None
while(txt_name not in filename):
    txt_name = str(input("请输入要选择的单词表"))
filepath = os.getcwd()
list_path = os.path.join(filepath,txt_name)
#读入
word_list = Word_list()
word_list.read_word()


while q == False:
    z = False
    while z == False:
        g = str(input('a.添加单词.\nb.给英文猜中文.\nc.给中文猜英文.\nd.统计错误.\ne.退出'))
        if g in ['a','b','c','d','e']:
            z = True
        else:
            print('请重新输入')

    if g == 'a' :
        ont = input('输入要添加的英文')
        mean = input('输入单词的中文')
        word = Word(ont,mean)
        word_list.add_word(word)
    elif g == 'b' :
        word_list.get_chinese()
    elif g == 'c' :
        word_list.get_english()
    elif g == 'd' :
        word_list.wrong_list()
    elif g == 'e' : #按字母序排列后保存并退出
        word_list.sort_list()
        word_list.write_word()
        q = True

    
