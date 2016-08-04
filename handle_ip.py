#coding:utf-8

#利用IPy模块来处理ip
from IPy import IP
ip = IP('10.1.4.128/25')
print ip.len()
for x in ip:
    print (x)