# 3题
''' a = int(input("请输入第一个数：")) 
b = int(input("请输入第二个数：")) 
print("两个数整除的结果为：",a // b)  # //整除 舍弃小数部分
print("两个数整除的结果为：",a / b) '''

# 4题
''' a = int(input("请输入第一个数：")) 
b = int(input("请输入第二个数："))
print("和为：",a + b) 
print("差为：",a - b)
print("积为：",a * b) '''

''' # 5题
str1 = input("请输入一个字符串：")
str2 = input("请输入一个子串：")
print(str1.count(str2)) # count方法 统计次数
 '''
# 6题
''' num = int(input("请输入一个整数："))
print("十进制：",num)
print("八进制：",oct(num)[2:])
print("十六进制：",hex(num).upper()[2:])
print("二进制：",bin(num)[2:]) '''

# 7题 字符串切片 
str = input("请输入一个字符串：")
a = int(input("请输入要操作的位置："))
str_m = input("请输入要替换的字符：")
print("原字符串为：",str)
print("修改后的字符串为：",str[:a] + str_m + str[a+1:]) 