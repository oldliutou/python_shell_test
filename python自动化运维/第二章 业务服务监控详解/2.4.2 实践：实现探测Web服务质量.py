import pycurl
import time
import sys
import os

URL = "http://www.baidu.com"
c = pycurl.Curl()
c.setopt(pycurl.URL,URL) #
# c.setopt(pycurl.CONNECT_TIME,5)
c.setopt(pycurl.TIMEOUT,5)
c.setopt(pycurl.NOPROGRESS,1)
c.setopt(pycurl.FORBID_REUSE,1)
c.setopt(pycurl.MAXREDIRS,1)
c.setopt(pycurl.DNS_CACHE_TIMEOUT,30) #设置保存DNS信息的时间 为30s

#创建一个文件对象，以”wb”方式打开，用来存储返回的http头部及页面内容
indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt",'wb')
c.setopt(pycurl.WRITEHEADER, indexfile) #将返回的HTTP HEADER定向到indexfile文件对象
c.setopt(pycurl.WRITEDATA,indexfile)#将返回的HTML内容定向到 indexfile文件对象
try:
    c.perform()
except Exception as e:
    print("connection error: %s" %e)
    indexfile.close()
    c.close()
    sys.exit()
NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
# CONNECT_TIME = c.getinfo(c.CONNECTION_TIME)
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)

STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
HTTP_CODE = c.getinfo(c.HTTP_CODE)
SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
SPEED_DOWNLOAD=c.getinfo(c.SPEED_DOWNLOAD)
print( "HTTP状态码：%s" %HTTP_CODE)
print ("DNS解析时间：%.2f ms" %(NAMELOOKUP_TIME*1000))
# print ("建立连接时间：%.2f ms" %(CONNECT_TIME*1000))
print ("准备传输时间：%.2f ms" %(PRETRANSFER_TIME*1000))
print ("传输开始时间：%.2f ms" %(STARTTRANSFER_TIME*1000))
print ("传输结束总时间：%.2f ms" %(TOTAL_TIME*1000))

print ("下载数据包大小：%d bytes/s" %(SIZE_DOWNLOAD))
print ("HTTP头部大小：%d byte" %(HEADER_SIZE))
print ("平均下载速度：%d bytes/s" %(SPEED_DOWNLOAD))