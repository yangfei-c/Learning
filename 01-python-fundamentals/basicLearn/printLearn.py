import os
'''
遍历输出指定路径下指定后缀名的文件或文件夹名
'''
for item in os.listdir("/"):
    if item.endswith('venv'):
        print(item)