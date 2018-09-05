'''
Created on 2018年7月25日

@author: yangyi
'''
#coding=utf-8
import argparse,socket
from datetime import datetime
MAX_bytes=65535
def server(port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1',port))
    print('listen at {}'.format(sock.getsockname()))
    while True:
        data,address=sock.recvfrom(MAX_bytes)
        text=data.decode('ascil')
        print('The client at {} says {!r}'.format(address,text))
        text='Your data was {} bytes long'.format(len(data))
        data=text.encode('ascil')
        sock.send(data,address)
def client(port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
if __name__ == '__main__':
    server('12')