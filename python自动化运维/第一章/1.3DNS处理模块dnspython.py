'''
dnspython（http://www.dnspython.org/）是Python实现 的一个DNS工具包，它支持几乎所有的记录类型，可 以用于查询、传输并动态更新ZONE信息，同时支持 TSIG（事务签名）验证消息和EDNS0（扩展 DNS）。在系统管理方面，我们可以利用其查询功能 来实现DNS服务监控以及解析结果的校验，可以代替 nslookup及dig等工具，轻松做到与现有平台的整合，
'''

import dns
from dns import resolver
def A_info():
    domain = "www.sohu.com"
    A = resolver.resolve(qname=domain,rdtype='A')
    # print(A.response.answer)
    for i in A.response.answer:#通过response.answer方法获取查询回 应信息
        # print(i.items)
        for j in i.items:
            if isinstance(j, dns.rdtypes.IN.A.A):  ##如果是A记录类型，则输出地址
                print('A记录: %s' % j.address)
            if isinstance(j, dns.rdtypes.ANY.CNAME.CNAME):  ##如果是CNAME记录，则直接输出
                print('CNAME: %s' % j)
def MX_info():
    domain = "163.com"
    mx = resolver.resolve(domain,'MX')
    print(mx.response.answer)
    for i in mx.response.answer:
        print(i)
def ns_info():
    domain = 'baidu.com'
    ns = resolver.resolve(domain,'NS')
    for i in ns.response.answer:
        print(i)
def cname_info():
    domain = 'baidu.com'
    ns = resolver.resolve(domain,'CNAME')
    for i in ns.response.answer:
        print(i)
if __name__ == '__main__':
    # MX_info()
    # ns_info()
    # cname_info()
    A_info()
