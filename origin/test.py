import os
import re

filename = os.listdir()
print(filename)
for z in filename:
    if not re.search(r".txt",z):
        filename.remove(z)
print(filename) 
filepath = os.getcwd()
print(filepath)
txt_list = []
for z in filename:
    txt_list.append((os.path.join(filepath,z)))

print(txt_list)
input("")