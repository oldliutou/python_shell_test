import socket

'''
    通过指定的端口和协议找到服务名
'''
def find_service_name():
    protocolname='tcp'
    for port in [80,25,110,3389,445,443,22]:
        print(f"port: {port} => servicename:{socket.getservbyport(port,protocolname)}")
    print(f"port: 53 => servicename:{socket.getservbyport(53,'udp')}")

if __name__ == '__main__':
    find_service_name()