import socket
import sys

def reuse_socket_addr():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # Get the old state of the SO_REUSEADDR option
    old_state = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
    print("old sock state:"+ str(old_state))

    # Enable the SO_REUSEADDR option
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    new_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print("new sock state:" + str(new_state))

    local_port = 8282
    srv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # srv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    srv.bind(("",local_port))
    srv.listen()
    print("Listening on port: %s " % local_port)
    while True:
        try:
            connection,addr = srv.accept()
            print('Connected by %s:%s' % (addr[0], addr[1]))
        except KeyboardInterrupt:
            break
        except socket.error as e:
            print(e)
if __name__ == '__main__':
    reuse_socket_addr()
    '''
        你可以在一个终端窗口运行这个脚本，然后在另一个终端窗口中输入
        telnet localhost 8282，尝试连接这个服务器。关闭服务器程
        序后，还可以使用同一个端口再次连接。然而，如果你把设定
        SO_REUSEADDR的那行代码注释掉，服务器将不会再次运行脚本。
    '''