# coding=UTF-8
import socket
language = {'what is your name':'I am Tom','how old areyou':'25','bye':'bye!'}

HOST="127.0.0.1"
PORT=6666
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT)) #绑定主机和端口号
s.listen(1) #开始侦听
print("Listing as port 6666")
conn,addr = s.accept() #响应客户端的一个请求，接受一个连接。
print("Connect by:",addr)
while True:
    data = conn.recv(1024)
    data = data.decode()
    if not data:
        break
    print("Received message:",data)
    conn.sendall(language.get(data,"Nothing").encode())
conn.close()
s.close()