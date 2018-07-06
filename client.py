import socket
import sys
import threading
from time import sleep
import json

#本地地址
#host = '127.0.0.1'
#远程地址
host = 'yourdomin'
class client():
    #连接主机并加入在线名单 并根据结果设置state的值
    def __init__(self,username):
        try:
            self.username = username
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            global host
            self.host =  host
            self.port = 8000
            self.s.connect((self.host, self.port))
            self.state = True
            #表明身份
            data = {
                'username': username
            }
            
            self.s.send(json.dumps(data).encode('utf-8'))
            res = self.s.recv(1024).decode('utf-8')
            res = json.loads(res)
            print(res)
            #print(res['result'])
            if res['result']=='join fail':
                raise ValueError
        except:
            #print('连接失败')
            self.state = False

    #发消息，返回是否发送成功的字符串信息
    def send(self,target,message):
        try:
            if message=="":
                raise ValueError
            data = {
                'target':target,
                'message':message
            }
            self.s.send(json.dumps(data).encode('utf-8'))
            #return 'succeed'
        except:
            return 'value error'

    #返回一个记录返回参数的字典
    def recv(self):
        try:
            res = self.s.recv(1024).decode('utf-8')
            res = json.loads(res)
        except:
            res = {
                'result':'error'
            }
        return res

    '''
    while True:
        sleep(0.1)
        print('\n请输入你要发送的消息')
        send = input();
        s.send(send.encode('utf-8'))
    '''


    