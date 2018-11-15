# -*-coding:utf-8-*-
from sys import argv  #导入参数传递系统
from os.path import exists #导入exists判断文件是否存在

script,from_file,to_file =argv #外来参数整理
print("copying from %s to %s" % (from_file,to_file)) #打印任务清单

#We could do these two on one line, how?
in_file = open(from_file) #打开要复制的文件
indata = in_file.read()#赋值给变量indata

print("The input file is %d bytes long" % len(indata)) #用len方法显示字节数
print("Does the output file exist? %r" % exists(to_file)) #检查目标文件是否存在
print("Ready, Hit RETURN to continue, CTRL-C to Abort")

input(">")
out_file = open(to_file,"w") #用写模式打开要复制到的目标
out_file.write(indata)#写入文件

print("Allright,all done.")
out_file.close() #关闭文件
in_file.close #关闭文件