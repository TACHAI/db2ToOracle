#!user/bin/env python3
# -*- coding: gbk -*-
import os
# 获取当前目录的位置 \\转义字符
path = os.getcwd()
filesPath = path+'\\'+'jcsj'
files = os.listdir(filesPath)
# 遍历文件夹
for file in files:
    # 判断是否是文件夹，不是文件夹才打开
    if not os.path.isdir(file):
        f = open(filesPath+'\\'+file, 'r', encoding='GBK')
        f1 = open(path+'\\'+file, 'a', encoding='GBK')
        line = f.readline()
        while line:
            print(line)
            # 将一行分成temp数组
            temp = line.split('values')
            # 定义两个变量存着个temp  第一组存字段名，第二组存数据，如果第一个包含data 或者time
            temp0arr = temp[0].split(',')
            temp1arr = temp[1].split(',')
            # to_date('2004-05-07 13:23:44','yyyy-mm-dd hh24:mi:ss')
            for i in temp0arr:
                # 记录下标
                index = len(temp1arr) - (len(temp0arr) - (temp0arr.index(i)))
                if i.find('TIME') != -1:
                    x = temp1arr[index]
                    if x.find('null') == -1:
                        temp1arr[index] = 'TIMESTAMP' + x
                        # temp1arr[i.index()] = 'to_date(\''+x+'\', \'yyyy-mm-dd hh24:mi:ss\')'
                elif i.find('DATE') != -1:
                    x = temp1arr[index]
                    if x.find('null') == -1:
                        temp1arr[index] = 'date' + x
                        # temp1arr[i.index()] = 'to_date(\'' + x + '\', \'yyyy-mm-dd\')'
            print(temp1arr)
            end = ','.join(temp0arr)+'values'+','.join(temp1arr)
            f1.write(end)
            # print(end)
            line = f.readline()
        f.close()
