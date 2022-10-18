import psutil
from subprocess import PIPE
'''
    获得当前系统的进程信息，可以让运维人员得知应用 程序的运行状态，
    包括进程的启动时间、查看或设置 CPU亲和度、内存使用率、IO信息、socket连接、
    线程数等，这些信息可以呈现出指定进程是否存活、资 源利用情况，
    为开发人员的代码优化、问题定位提供 很好的数据参考。
'''

def ps_info():
    print(psutil.pids())#列出所有进程PID
    print(psutil.Process(1112))#实例化一个Process对象，参数为一进程 PID
    p = psutil.Process(1112)
    print(p.name())#进程名
    print(p.exe())#进程bin路径
    print(p.cwd())#进程工作目录绝对路径
    print(p.status())#进程状态
    print(p.create_time())#进程创建时间，时间戳格式
    # print(p.uids())#进程uid信息, linux系统会显示
    # print(p.gids())#进程gid信息，linux系统会显示
    print(p.cpu_times())#进程CPU时间信息，包括user、system两个CPU时间
    print(p.cpu_affinity())#get进程CPU亲和度，如要设置进程CPU亲和度，将 CPU号作为参数即可
    print(p.memory_percent())#进程内存利用率
    print(p.memory_info())#进程内存rss、vms信息
    print(p.io_counters())#进程IO信息，包括读写IO数及字节数
    print(p.connections())  # 返回打开进程socket的namedutples列表，包括 fs、family、laddr等信息
    print(p.num_threads())

def popen_test():
#     psutil提供的popen类的作用是获取用户启动的应用程 序进程信息，以便跟踪程序进程的运行状态。
# 通过psutil的Popen方法启动的应用程序，可以跟踪该程序运行的所有相关信息
    p = psutil.Popen(["python","-c","print('Hello')"],stdout=PIPE)
    print(p.name())
    print(p.username())
    print(p.communicate())
    print(p.cpu_times())#得到进程运行的CPU时间

if __name__ == '__main__':

    # ps_info()
    popen_test()