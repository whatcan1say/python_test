# python 字符串
# 字符串 转义字符 字符串的内容可以包含任何字符， 英文字符，中文字符

# str2 = 'hello world ! '
# print(str2)
# str1 = "热爱我的热爱"
# print(str1)
# str3 = " i'm whatcanisay " # 当字符串中内容包含引号时 适用不同的引号将字符串括起来
# print(str3)
# str4 = '"Spring is here , let us jam!,"said woodchunk.'
# print(str4)
# str5 = '"we are scared, Let\' hide in the shade", says the bird' #使用反斜线（\）将字符串中的特殊字符转义
# print(str5)


# 字符串拼接 
# s1 = "hello," 'lee'
# print(s1)
# s2 = "Python "
# s3 = "is funny"
# print(s2 + s3)

# repr 和字符串
# s1 = "这本书的价格是："
# a = 9.8
# print(s1+str(a)) #python不允许直接拼接数值和字符串 适用str()和repr()函数
# print(s1+repr(a))
# st = "what can i say"
# print(st)
# print(repr(st))


#适用input和raw_input获取输入
# msg = input("请输入你的名字：")
# print(msg)
# print(type(msg)) #python 2 中尽量使用raw_input 等同python3 中的input函数

#长字符串
# s = ''' "let's go finishing ", said mary.'''
# print(s)
# s2 = 'the quick brown fox \ 适用转义字符对换行转义 不会中断字符串。
# jump over the lazy dog.'
# print(s2)

#原始字符串
# lujing = 'D:\\BaiduNetdiskDownload\\激活工具'
# print(lujing)
# lujing = r'D:\BaiduNetdiskDownload\激活工具' #原始字符串以r开头 不会把反斜线当成特殊字符
# print(lujing)
# s2 = r'"let\'s go"'
# print(s2) # 原始字符串内包含特殊字符也需转义
# s3 = r'good morning ' "\\"
# print(s3)

# 字节串  由多个字节组成，以字节为单位进行基本操作
# b1 = bytes() #创建空的bytes
# b2 = b''
# b3 = b'hello' # 通过b前缀指定hello是bytes类型的值
# print(b3)
# print(b3[0])
# print(b3[2:4])
# b4 = bytes('我爱python编程',encoding='utf-8')
# print(b4)
# b5 = "学习python很有趣".encode('utf-8')
# print(b5)
# st = b5.decode('utf-8')
# print(st)


#python 支持的转义字符  
# \b 退格符  \n 换行符 \r 回车符 \t 制表符 \" 双引号  \' 单引号 \\ 反斜线
# s = 'hello\nworld\nwhat\ncan\nisay'
# print(s)
# s1 = '商品名\t\t单价\t\t数量\t\t总价'
# s2 = 'what\t\t222\t\t111\t\t333'
# print(s1)
# print(s2)
# st = '"Spring is here , let us jam!,"said woodchunk.'
# print(st[2])
# print(st[-4])
# print(st[3:-4])
# print(st[3:5])
# print(st[-6:-3])
# print(st[-3:-])
# print(st[5:])
# print(st[:5])
# print('is' in st) #判断字符是否在字符串中，返回bool类型值 true or false
# print('are' in st)
# print(len(st))
# print(len("test"))
# print(max(st))
# print(min(st))
# a = 'what can i say'
# print(a.title())  每个单词的首字母大写
# print(a.lower())  整个字符串改成小写
# print(a.upper())  整个字符串改成大写


# 三目运算符
a = 5
b = 3
st = "a大于b" if a > b else "a小于b"
print(st)