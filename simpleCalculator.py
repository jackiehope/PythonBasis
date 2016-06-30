#coding:utf-8

#简单的四则运算器

clist = ['加', '减', '乘', '除']
tlist = [ '+', '-', '*', '/']
for i in clist:
    print clist.index(i), ':' , i

choice = raw_input("你选择什么运算方式：")
f_num = raw_input("输入第一个数：")
s_num = raw_input("输入第二个数")
#获得计算表达式
calcu_str = f_num + tlist[int(choice)] + s_num
print eval(calcu_str)