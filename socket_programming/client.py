'''Client that will connect to the socket'''
import socket

s = socket.socket()
s.connect(('localhost', 9999))
name = input("Enter your name: ")
s.send(bytes(name, 'utf-8'))
# print(s.recv(1024)) # receive 1024 bytes
print(s.recv(1024).decode()) # decode the bytes to string
s.close()