# 3.3.2 实践：实现TCP探测目标服务路由轨迹
import os,sys,time,subprocess
import warnings,logging
warnings.filterwarnings("ignore",category=DeprecationWarning)  #屏蔽scapy无用告警信息
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)#屏蔽模块IPv6多余告警
from scapy.all import traceroute

domains='www.baidu.com'
target = domains.split(" ")
dport=[80]
if len(target)>=1 and target[0]!="":
    res,unans = traceroute(target,dport,retry=-2) #启 动路由跟踪
    res.graph(target="> test.svg") #生成svg矢量图
    subprocess.Popen("/usr/bin/convert test.svg test.png", shell = True)  # svg转png格式
    time.sleep(1)
else:
    print( "IP/domain number of errors，exit")