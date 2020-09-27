import os
def file_size(path):
    os.chdir(path)
    all_file = os.listdir('.')
    for each in all_file:
        print('%s [%d Bytes]' %(each,os.path.getsize(each)))

path=input("请输入路径：")
file_size(path)
