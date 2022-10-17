import socket
SEND_BUF_SIZE=4096
RECV_BUF_SIZE=4096
def modify_buff_size():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # Get the size of the socket's send buffer
    bufsize = sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
    print("Buffer size [Before]:%d" % bufsize)

    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)

    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_SNDBUF,
        SEND_BUF_SIZE)
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_RCVBUF,
        RECV_BUF_SIZE)

    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Buffer size [After]:%d" % bufsize)

if __name__ == '__main__':
    modify_buff_size()
    '''
        在套接字对象上可调用方法getsockopt()和setsockopt()分别获
        取和修改套接字对象的属性。setsockopt()方法接收三个参数：
        level、optname和value。其中，optname是选项名，value是该
        选项的值。第一个参数所用的符号常量（SO_*等）可在socket模块
        中查看。
    '''

