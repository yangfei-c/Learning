'''
列表就像是一个容器一样，可以放很多种数据类型
<<<<<<< HEAD
有序可变
'''
list1 = [1,"中国","中国",True]
#追加
list1.append("追加")

#插入
list1.insert(1,"插入到1位置")

#删除
list1.remove("中国")
#如果元素不存在则报错，删之前判断一下
del list1[2:4]#切片删除

#索引删除
list1.pop(1)
#不加数字默认删除尾部,删除指定索引值，同时返回删除的值可用变量接收

#列表清空
list1.clear()

#对列表排序
list=[1,2,1,31,2,3,1]
list.sort()
#默认从小到大,字符串时安装unicode排序
list.sort(reverse=True)










=======

'''
>>>>>>> origin/master
