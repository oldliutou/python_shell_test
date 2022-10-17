import socket
import sys
import argparse

def main():
    # setup argument parsing
    parser = argparse.ArgumentParser(description="Socket Error Examples")
    parser.add_argument('--host',action="store",dest="host",required=False)
    parser.add_argument('--port',action="store",dest="port",required=False)
    parser.add_argument('--file',action="store",dest="file",required=False)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file
    # First try-except block -- create socket
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error as e:
        print(f"Error creating socket:{e}")
        sys.exit(1)
    # Second try-except block -- connect to given host/port
    try:
        s.connect((host,port))
    except socket.gaierror as e:
        print("Address-related error connecting to server: %s" % e)
        sys.exit(1)
    # Third try-except block -- sending data
    try:
        s.sendall(("GET %s HTTP/1.0\r\n\r\n" %filename))
    except socket.error as e:
        print("Error sending data:"+e)
        sys.exit(1)
    while 1:
    # Fourth tr-except block -- waiting to receive data from     remote    host
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print("Error receiving data:"+e)
            sys.exit(1)
            if not len(buf):
                break
                # write the received data
            sys.stdout.write(buf)
if __name__ == '__main__':
    main()
    '''
        这个攻略用到了三个命令行参数：主机名、端口号和文件名。
        如果提供的主机不存在，这个脚本会输出如下错误
        如果某个端口上没有服务，你却尝试连接到这个端口，则这个脚本会抛出连接超时异常，如下所示：
        
        
    '''