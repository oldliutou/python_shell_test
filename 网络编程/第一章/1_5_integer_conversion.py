import socket

def convert_integer():
     data = 1234
     # 32-bit
     print( "Original: %s => Long host byte order: %s, Network byte order: %s" %(data, socket.ntohl(data), socket.htonl(data)))
     # 16-bit
     print("Original: %s => Short host byte order: %s, Network byte order: %s"     %(data, socket.ntohs(data), socket.htons(data)))
if __name__ == '__main__':
    convert_integer()

    '''
        在这个攻略中，我们以整数为例，演示了如何把它转换成网络字节序
        和主机字节序。socket库中的类函数ntohl()把网络字节序转换成
        了长整形主机字节序。函数名中的n表示网络；h表示主机；l表示长
        整形；s表示短整形，即16位。
    '''