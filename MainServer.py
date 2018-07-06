import socket
import sys
import threading
import json

# 服务端初始化
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#本地使用
#host = '127.0.0.1'
#远程使用
#host = '0.0.0.0'
port = 8000

serversocket.bind((host,port))
serversocket.listen(6)
socks = {}
usernames = []


def listen(sock,addr):
    data = {}
    is_online = True


    #加入在线用户列表
    global usernames
    global socks
    res = json.loads(sock.recv(1024).decode('utf-8'))
    try:
        username = res['username']
        if (username in usernames and socks[username]!=''):
            raise ValueError
        if username not in usernames:
            usernames = usernames + [username]
        socks[username] = sock
        data['result'] = 'join succeed'
    except ValueError:
        data['result'] = 'user has been online'
        sock.send(json.dumps(data).encode('utf-8'))
        return
    except:
        data['result'] = 'join fail'
    sock.send(json.dumps(data).encode('utf-8'))


    #处理发消息请求
    #print(username)
    #print(socks)
    while True:
        try:
            res = sock.recv(1024).decode('utf-8')
            res = json.loads(res)
            try:
                data = {
                    'result':'message',
                    'from': username,
                    'message':res['message']
                }
                print('target is : ',res['target'])
                s = socks[res['target']]
                s.send(json.dumps(data).encode('utf-8'))
                print('服务器发送成功')
            except:
                data['result'] = 'user is not online'
                print('服务器发送失败')
        except:
            data = {
                'result':'value error'
            }
            is_onlie = False
            socks[username]=""
            print("用户断开连接")
        sock.send(json.dumps(data).encode('utf-8'))
        if is_online == False:
            return
    #print(usernames)


while True:
    sock , addr = serversocket.accept()
    threading.Thread(target = listen,args=(sock,addr)).start()

