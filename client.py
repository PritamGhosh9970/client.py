import socket

c = socket.socket()

c.connect(('localhost', 9999))

name = input("Enter your name: ")
c.send(bytes(name, 'utf-8'))

print(c.recv(1024).decode())

respo = c.recv(1024).decode()
print(respo)
res = input("\t Yes/No:\t")
c.send(bytes(res,'utf-8'))
respo = c.recv(1024).decode()
print('Message:\t\t', respo)
while respo != '\0':
        c.send(bytes(input("Enter Respond:\t "), 'utf-8'))
        print('Message:\t\t', c.recv(1024).decode())



