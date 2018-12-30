# """ #python 注释！
# #这是一行简单的注释
# print("hellp world!")
# '''
#    这里面
#    的内容
#    是多行
#    注释
# '''
# """
# #三引号多行注释同样被允许！
# """

# #python 变量
# a=5
# print(a)
# #type():python 内置函数 判断变量类型
# print(type(a))
# a='whatcanisay'
# print(a)
# print(type(a)) """

#python print()函数输出变量
#print(...)详细语法适用格式
#   print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False) 
""" 
print函数多个变量输出
user_name ='whatcanisay'
user_age=20
print("姓名:", user_name,"年龄:", user_age)
print("姓名:", user_name,"年龄:", user_age,'\t',end=" ") # end默认设置换行
print("姓名:", user_name,"年龄:", user_age,'\t',end=" ") #设置end 参数 不换行 """

# #python数值类型
# #整型
# a = 56 
# print(a)
# print(type(a))
# a =9999999999999999999999999999999 #python2 中被当成long型，无影响
# print(a)
# print(type(a))
# a = None
# print(a) #python 整型支持空值


# hex_value1 = 0x13
# hex_value2 = 0XaF
# print("hex_value1的值为：",hex_value1)
# print("hex_value2的值为：",hex_value2) # python 16进制输出 0x 0X 代表十六进制数
# bin_val = 0b111
# print("bin_val的值为：",bin_val)
# bin_val = 0B111
# print("bin_val的值为：",bin_val) 
# oct_val = 0o54
# print("oct_val的值为：",oct_val) 
# oct_val = 0O17
# print("oct_val的值为：",oct_val) # python 8进制输出 0o 0o 代表二进制数


# one_million = 1_000_000
# print(one_million)

# #浮点型
# af1 =  5.123456
# print(af1)
# print(type(af1))
# f1 =520e1
# print(f1)
# print(type(f1))

# #复数
# ac1 = 3 + 0.2j
# print(ac1)
# print(type(ac1))
# ac2 = 4 -0.1j
# print(ac2)
# print(ac1 +ac2)
# import cmath
# ac3 = cmath.sqrt(-1) #cmath 内置函数 求平方根
# print(ac3)