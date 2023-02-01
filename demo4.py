## 变量的定义和使用

# 一、定义变量
name = "马冬梅" #"马冬梅"字符串赋值给了变量name

# 变量有三个属性：标识、类型、值。
# 1、标识：表示对象所存储的内存地址，使用内置函数id(obj)获取
print("变量name的标识是",id(name),sep='')
# 2、类型：表示对象的数据类型，使用内置函数type(obj)获取
print("变量name的类型是",type(name),sep='')
# 3、值：表示对象所存储的具体数据内容，使用print(obj)可以直接打印输出
print("变量name的值是",name,sep='')

# print打印完后，默认会换行。
# 如果希望字符串和变量在同一行打印，则需要在中间加逗号，这样会把换行变成空格。
# 如果不想要空格，可以在再后面加上sep='' 
# sep='xxx'其含义是：在print中，用逗号分隔的不同元素之间，在打印时用xxx分隔。
# sep=''表示中间什么都没有，从而得以去掉了空格。

# 二、当再次赋值同一个变量后，变量名会指向新的空间
name = "马什么梅"
print("变量name的标识是",id(name),sep='')