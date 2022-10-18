import dns
from dns import  resolver
import requests
import os
'''
    1）实现域名的解析，获取域名所有的A记录解析IP列 表；
    2）对IP列表进行HTTP级别的探测。
'''
iplist=[]#定义域名IP列表变量
appdomain="www.baidu.com"#定义业务域名

def get_iplist(appdomain):#域名解析函数，解析成功IP将被追加到 iplist

    try:
        A = resolver.resolve(appdomain,"A")
    except Exception as e:
        print("dns resolver error :"+e)
        return
    for i in A.response.answer:
        for j in i.items:
            if isinstance(j,dns.rdtypes.IN.A.A):
                iplist.append(j.address)
    return True
def checkip(ip):
    checkurl="http://"+ip+":80"
    print(checkurl)
    getcontent=""
    result = requests.get(checkurl)
    spec_text = '<img hidefocus="true" src="//www.baidu.com/img/bd_logo1.png"'

    if spec_text in result.text:
        print(ip+" [OK] ")
    else:
        print(ip+" [ERROR] ")
if __name__ == '__main__':
    if(get_iplist(appdomain) and len(iplist)>0):

        for ip in iplist:
            checkip(ip)
    else:
        print("dns resolver error")