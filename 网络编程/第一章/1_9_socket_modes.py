import socket
def test_socket_modes():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setblocking(1)

    s.settimeout(0.5)
    s.bind(('127.0.0.1',0))
    socket_address = s.getsockname()
    print("Trivial Server launched on socket: %s" % str(socket_address))
    while (1):
        s.listen(1)

if __name__ == '__main__':
    test_socket_modes()

    '''
        在这个攻略中，我们把1传给setblocking()方法，启用套接字的阻
        塞模式。类似地，可以把0传给这个方法，把套接字设为非阻塞模
        式。
        这个功能在后面的一些攻略中会用到，到时再详细说明其真正作用。
    '''