'''This module we will implement socket programming in Python'''
import socket

s = socket.socket()
print('socket created')
s.bind(('localhost', 9999))

s.listen(3) # how many connections can be queued
print('waiting for connections...')

while True:
    c, addr = s.accept()  # accept the connection
    name = c.recv(1024).decode()  # receive the name from the client
    print(f'connected with {addr} as {name}')
    c.send(bytes('welcome to the server', 'utf-8')) # send a welcome message, uses bytes to encode the string
#    c.close()  # close the connection