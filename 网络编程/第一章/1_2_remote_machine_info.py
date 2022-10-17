import socket

def get_remote_info():
    remote_host = "www.python.org"
    try:
        print(f"ip 地址为：{socket.gethostbyname(remote_host)}")
    except socket.error as err_msg:
        print(remote_host,err_msg)
if __name__ == '__main__':
    get_remote_info()
    '''
        这个攻略把gethostbyname()方法包装在用户定义的
        get_remote_machine_info()函数中，还引入了异常处理的概
        念。如上述代码所示，我们把主要的函数调用放在try-except块
        中，这就意味着，如果执行函数gethostbyname()的过程中发生了
        错误，这个错误将由try-except块处理。
    '''