'''
本节介绍python-nmap模块的两个常用类，一个为 PortScanner（）类，实现一个nmap工具的端口扫描功 能封装；另一个为PortScannerHostDict（）类，实现 存储与访问主机的扫描结果

'''

import sys
import nmap
scan_row=[]
input_data="192.168.59.1/24 80,3306"
scan_row = input_data.split(" ")
if len(scan_row)!=2:
    print("Input errors，example \"192.168.1.0/24 80，443，22\"")
    sys.exit(0)
hosts=scan_row[0] #接收用户输入的主机
port=scan_row[1]#接收用户输入的端口
try:
    nm=nmap.PortScanner()#创建端口扫描对象
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(0)
except:
    print("Unexpected error：", sys.exc_info()[0])
    sys.exit(0)

try:
# 调用扫描方法，参数指定扫描主机hosts，nmap扫描命令行参数arguments
    nm.scan(hosts=hosts,arguments=' -v -sS -p '+port)
except Exception as e:
    print(e)
for host in nm.all_hosts(): #遍历扫描主机
    print('-'*12)
    print(f"Host:{host} ({nm[host].hostname()})")
