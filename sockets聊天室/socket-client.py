import socket

# 设定服务器地址
serverAddr = ('127.0.0.1', 1226)

# 创建 socket 连接
c = socket.socket(type=socket.SOCK_DGRAM)

# 开始向服务器地址发送数据
while True: 
    message = input('发送消息：')
    c.sendto(message.encode(), serverAddr)
    if message == 'exit':
        break
    # 接收服务器回复
    data, serverAddr = c.recvfrom(1024)
    print(f'{serverAddr[0]}:{serverAddr[1]} > {data.decode()}')
    
c.close()