import socket
def print_local_info():
    host_name = socket.gethostname()
    print(host_name)
    print(socket.gethostbyname(host_name))

if __name__ == '__main__':
    print_local_info()
