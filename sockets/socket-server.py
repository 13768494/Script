import socket

# 设定服务器地址
serverAddr = ('127.0.0.1', 1226)

# 创建 socket 并且绑定到服务器地址
s = socket.socket(type=socket.SOCK_DGRAM)
s.bind(serverAddr)

# 开始监听端口，接收 1024 个字节
while True:
    data, clientAddr = s.recvfrom(1024)
    print(f'{clientAddr[0]}:{clientAddr[1]} > {data.decode()}')
    if data.decode() == 'exit':
        break
    # 回复发送端
    reply = input('回复消息：')
    s.sendto(reply.encode(), clientAddr)

s.close()