#coding:utf-8

#十进制到十六进制
num1 = int(raw_input("输入一个十进制数:"))
print hex(num1)

#十六进制到十进制
num2 = raw_input("输入一个十六进制数：")
print int(num2, 16)

#十进制到字符串
num3 = int(raw_input("输入一个数"))
print repr(str(num3))