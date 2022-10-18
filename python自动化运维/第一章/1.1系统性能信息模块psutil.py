import datetime

import psutil
'''
    采集系统的基本性能信息包括CPU、内存、磁盘、网 络等，可以完整描述当前系统的运行状态及质量。 psutil模块已经封装了这些方法，用户可以根据自身 的应用场景，调用相应的方法来满足需求，非常简单 实用。
'''
def mem_info():
    # Linux系统的内存利用率信息涉及total（内存总数）、 used（已使用的内存数）、free（空闲内存数）、 buffers（缓冲使用数）、cache（缓存使用数）、 swap（交换分区使用数）等，分别使用 psutil.virtual_memory（）与psutil.swap_memory（）
    # 方法获取这些信息
    mem = psutil.virtual_memory() #使用psutil.virtual_memory方 法获取内存完整信息
    print(mem)
    print("内存总量为：%s" %(mem.total))
    print("内存可用为：%s" %mem.available)
    print("空闲内存为：%s" %mem.free)
    swap_mem = psutil.swap_memory()
    print(swap_mem)


def cpu_info():
    # Linux操作系统的CPU利用率有以下几个部分： ·User Time，执行用户进程的时间百分比； ·System Time，执行内核进程和中断的时间百分比； ·Wait IO，由于IO等待而使CPU处于idle（空闲）状态 的时间百分比； ·Idle，CPU处于idle状态的时间百分比。

    #使用cpu_times方法获取CPU完整信息，需要显示所 有逻辑CPU信息，>#指定方法变量percpu=True即可，如psutil.cpu_times（percpu=True）
    cup_info = psutil.cpu_times(percpu=False)
    print(cup_info)
    print(cup_info.user)#获取单项数据信息，如用户user的CPU时 间比
    print(psutil.cpu_count()) #获取CPU的逻辑个数，默认logical=True4
    print(psutil.cpu_count(logical=False))#获取CPU的物理个数

def io_info():
    #磁盘IO信息包括read_count（读IO数）、 write_count（写IO数）、read_bytes（IO读字节数）、 write_bytes（IO写字节数）、read_time（磁盘读时 间）、write_time（磁盘写时间）等。这些IO信息可 以使用psutil.disk_io_counters（）获取
    print(psutil.disk_partitions())#使用psutil.disk_partitions方法 获取磁盘完整信息
    print(psutil.disk_usage("C:\\"))  #使用psutil.disk_usage方法获取分区（参 数）的使用情况
    print(psutil.disk_io_counters())#使用psutil.disk_io_counters获 取硬盘总的IO个数、读写信息
    print(psutil.disk_io_counters(True))  #“perdisk=True”参数获 取单个分区IO个数、 #读写信息
def net_info():
#         系统的网络信息与磁盘IO类似，涉及几个关键点，包 括bytes_sent（发送字节数）、 bytes_recv=28220119（接收字节数）、 packets_sent=200978（发送数据包数）、 packets_recv=212672（接收数据包数）等
    print(psutil.net_io_counters())#使用psutil.net_io_counters获取 网络总的IO信息，默认  pernic=False
    print(psutil.net_io_counters(True)) #pernic=True输出每个网络 接口的IO信息
def other_info():
#     psutil模块还支持获取用户登录、开机时间等信息
    print(psutil.users())#使用psutil.users方法返回当前登录系统的用户信 息
    print(psutil.boot_time())#使用psutil.boot_time方法获取开机时间 ，以 Linux时间戳格式返回
    print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__':
    # cpu_info()
    # mem_info()
    #  io_info()
    # net_info()
    other_info()