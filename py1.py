# coding:utf-8
# Author：si1ent
# 2018-11-2
# 第一步，首先定义一个urltoip的函数主要作用是用于域名正向解析到IP地址
# 第二步，打开我们自己保存的域名地址，并新建一个保存解析后存放IP地址的txt文档中，之后再调用这个函数即可实现函数的作用并成功解析域名并保存IP地址到txt中。
# 第三部，读取、新建的文件需要"关闭"连接。
# 重要部分：1、函数的建立，2、for循环读取URL，3、gethostbyname函数获取IP地址，4、urllist读取，新建iplist以及函数调用。
import socket
def urltoip():
   for oneurl in urllist.readlines():       # readlines()py中文件读取函数
       url = str(oneurl.strip())[7:]        # 7是切片只获取uri不包含http协议部分，因为我们正常进行ping时也是只包含uri。
       print url
       try:
           ip = socket.gethostbyname(url)    # 函数用域名或主机名获取IP地址
           print ip
           iplist.writelines(str(ip)+"\n")
       except:
           print "The URL to IP ERROR "

try:
    urllist = open("url.txt", "r")
    iplist = open("ip.txt", "w")
    urltoip()
    urllist.close()
    iplist.close()
    print "Successed!"
except:
    print "ERROR!"