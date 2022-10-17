import socket
from binascii import hexlify
def convert_ip4_address():
    for ip in ['127.0.0.1','192.168.1.1']:
        packed_ip_addr = socket.inet_aton(ip)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print(f"ip address:{ip} => packed:{hexlify(packed_ip_addr)} => unpacked:{unpacked_ip_addr}")
if __name__ == '__main__':
    convert_ip4_address()
    '''
        在这个攻略中，使用for-in语句把两个字符串形式的IP地址转换成
        打包后的32位二进制格式，而且还调用了binascii模块中的
        hexlify函数，以十六进制形式表示二进制数据。
    '''