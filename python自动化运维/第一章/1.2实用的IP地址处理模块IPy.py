import IPy
from IPy import IP
'''
    IPy模块包含IP类，使用它可以方便处理绝大部分格 式为IPv6及IPv4的网络和地址。
'''
def ip_process():
    ip = IP('192.168.0.0/16')
    print(ip.len())#输出192.168.0.0/16网段的IP个数
    for i in ip:
        print(i)#输出192.168.0.0/16网段的所有IP清单

def ip_process1():
    # 下面介绍IP类几个常见的方法，包括反向解析名称、 IP类型、IP转换等。
    # ip = IP('192.168.59.1')
    ip = IP('123.223.52.167')
    print(ip.reverseName())#反向解析地址格式
    print(ip.iptype())#192.168.59.1为私网类型'PRIVATE'
    print(ip.int())#转换成整型格式
    print(ip.strHex())#转换成十六进制格式
    print(ip.strBin())#转换为2进制格式
    print(IP(0x8080808))#十六进制转成IP格式
def ip_process2():
    # IP方法也支持网络地址的转换，例如根据IP与掩码生产网段格式
    print(IP('192.168.1.0').make_net("255.255.255.0"))
    print(IP('192.168.1.0/255.255.255.0',make_net=True))
    print(IP('192.168.1.0-192.168.1.255',make_net=True))
#     也可以通过strNormal方法指定不同wantprefixlen参数 值以定制不同输出类型的网段。
    print(IP('192.168.1.0/24').strNormal(0))
    print(IP('192.168.1.0/24').strNormal(1))
    print(IP('192.168.1.0/24').strNormal(2))
    print(IP('192.168.1.0/24').strNormal(3))
def ip_process3():
    print(IP('10.0.0.0/24') < IP('12.0.0.0/24'))
    print('10.0.0.1' in IP('12.0.0.0/24'))
    print('10.0.0.1' in IP('10.0.0.0/24'))
    print(IP('10.0.0.0/24') in IP('10.0.0.0/16'))
# 判断两个网段是否存在重叠，采用IPy提供的overlaps
    print(IP('10.0.0.0/24') in IP('10.0.0.0/16'))
    print(IP('11.0.0.0/24') in IP('10.0.0.0/16'))
def ip_test():
    '''
    根据输入的IP或子网返回网络、掩码、广播、 反向解析、子网数、IP类型等信息。
    :return:
    '''
    ip_s = input("请输入一个ip或者一个网段信息：")#接收 用户输入，参数为IP地址或网段地址
    ips = IP(ip_s)
    if(len(ips)>1):#为一个网络信息
        # 输出网络信息
        print(ips.net())
#         输出掩码信息
        print(ips.netmask())

#         输出网络广播地址信息
        print(ips.broadcast())
        # 输出地址反向解析
        print('reverse address： %s' % ips.reverseNames()[0])
        print('subnet： %s' % len(ips)) #输出网络子网数
    else: #为单个ip地址
        print(ips.reverseNames()[0])
        # 输出IP反向解析
        print(ips.strHex())
        print(ips.strBin())
        print(ips.strDec())
if __name__ == '__main__':
    # ip_process()
    # ip_process1()
    # ip_process2()
    # ip_process3()
    ip_test()