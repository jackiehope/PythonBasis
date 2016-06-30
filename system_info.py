#coding:utf-8

import sys
import pprint
import psutil
import datetime
from subprocess import PIPE

#pprint.pprint(dir(sys))
print sys.builtin_module_names
print sys.copyright

#获取内存信息
mem = psutil.virtual_memory()
pprint.pprint(dir(mem))
print mem
print "总内存: %f" % (mem.total / 1024.0 /1024)
print "已使用的内存: %f" % (mem.used / 1024.0 /1024)

#获取cpu信息
print psutil.cpu_times()

#获取磁盘信息
disk_info = psutil.disk_partitions()
print disk_info
disk_usage_info = psutil.disk_usage("c:\\")
print disk_usage_info
disk_io_info = psutil.disk_io_counters()
print disk_io_info

#网络信息
net_io_info = psutil.net_io_counters()
print net_io_info

print psutil.users()
print psutil.boot_time()
print datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

#进程管理
print psutil.pids()
p = psutil.Process(psutil.pids()[-1])
print p.name()
print p.status()
print p.create_time()

p = psutil.Popen(["python", "-c", "print('hello python')"], stdout=PIPE)
print p.name()
print p.username()
print p.cpu_times()