import socket

def test_socket_timeout():
    # 第一个参数是地址族，第二个参数是套接字类型。
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print(f"默认的超时时间为：{s.gettimeout()}")
    s.settimeout(100)
    print(f'修改后的超时时间为：{s.gettimeout()}')
if __name__ == '__main__':
    test_socket_timeout()
    '''
        在这段代码片段中，首先创建了一个套接字对象。套接字构造方法的
        第一个参数是地址族，第二个参数是套接字类型。然后，调用
        gettimeout()方法获取套接字超时时间，再调用settimeout()方
        法修改超时时间。传给settimeout()方法的参数可以是秒数（非负
        浮点数）也可以是None。这个方法在处理阻塞式套接字操作时使用。
        如果把超时时间设为None，则禁用了套接字操作的超时检测。
    '''

