from sqlalchemy import Column, String, create_engine, Integer, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

a = "aa"
b = "adfadfaf"
c = 12
d = 22323

print("%10s %20d"%(a,c))
print("%10s %20d"%(b,d))
