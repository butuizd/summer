import sys
#from register import register
from PyQt5.QtWidgets import QApplication
import json
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from tip import tip
from client import client
from time import sleep
from PyQt5.QtCore import *

'''
================================
        登录界面
================================
'''
class login(object):
    def __init__(self):
        self.w = QtWidgets.QWidget()
        self.setupUi(self.w)
        self.w.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 220, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.register)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 50, 81, 18))
        self.label.setObjectName("label")
        # self.checkBox = QtWidgets.QCheckBox(Form)
        # self.checkBox.setGeometry(QtCore.QRect(80, 160, 181, 22))
        # self.checkBox.setObjectName("checkBox")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(210, 50, 113, 25))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 120, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 120, 81, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 220, 112, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.login)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "summer V1.0 ※登录界面"))
        self.pushButton.setText(_translate("Form", "注册"))
        self.label.setText(_translate("Form", "用户名"))
        #self.checkBox.setText(_translate("Form", "记住用户名和密码"))
        self.label_2.setText(_translate("Form", "密码"))
        self.pushButton_2.setText(_translate("Form", "确定"))

    def login(self):
        person={'username':self.lineEdit.text(),'password':self.lineEdit_2.text()}
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        global temp
        try:
            r=requests.post("http://yourdomin/functions/login",data=person, timeout = 2)
            res=json.loads(r.text)
            print(res)
            if res['result']=='success':
                print(111)
                temp = tip("登陆成功")
                global main
                main = mainwindow(res['username'])
                self.w.close()
            elif res['result']=="password is wrong":
                temp = tip("密码错误")
                pass
            else:
                temp = tip("用户不存在")
        except:
            temp = tip("连接服务器超时")

    def register(self):
        global r
        r = register()


'''
================================
        注册界面
================================
'''
class register(object):
    def __init__(self):
        self.w = QtWidgets.QWidget()
        self.setupUi(self.w)
        self.w.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 300)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(210, 50, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 50, 81, 18))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 120, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 120, 81, 18))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 220, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.register)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def register(self):
        global temp
        try:
            infor = {'username': self.lineEdit.text(), 'password': self.lineEdit_2.text(), 'nickname': "none"}
            r = requests.post("http://yourdomin/functions/register", data=infor, timeout=1)
            res = json.loads(r.text)
            if res['result'] == 'register succeed':
                temp = tip("注册成功")
                self.w.close()
            elif res['result'] == "user has existed":
                temp = tip("用户已经存在")
            else:
                temp = tip("注册失败")
        except:
            temp = tip("连接服务器超时")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "summer V1.0 ※注册界面"))
        self.label.setText(_translate("Form", "用户名"))
        self.label_2.setText(_translate("Form", "密码"))
        self.pushButton.setText(_translate("Form", "注册"))


'''
================================
        主页面
================================
'''
end_code = "*(Jsjdh&HHI$J123q@"
friend_code = "*&781)%asld;1APD*y["
isonline_code = "0(3&jfY7%R[q12P"

class mainwindow(object):
    def __init__(self,username):
        self.username = username
        self.messages = []
        self.online = False
        self.w = QtWidgets.QWidget()
        self.setupUi(self.w)
        self.w.show()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(869, 624)
        #添加好友按钮
        self.add = QtWidgets.QPushButton(Form)
        self.add.setGeometry(QtCore.QRect(270, 50, 91, 41))
        self.add.setObjectName("add")
        self.add.clicked.connect(self.add_friend)

        #发起聊天按钮
        self.chat = QtWidgets.QPushButton(Form)
        self.chat.setGeometry(QtCore.QRect(240, 180, 112, 34))
        self.chat.setObjectName("chat")
        self.chat.clicked.connect(self.select_friend)
        #发送按钮
        self.send = QtWidgets.QPushButton(Form)
        self.send.setGeometry(QtCore.QRect(700, 510, 112, 34))
        self.send.setObjectName("send")
        self.send.clicked.connect(self.send_msg)
        #退出聊天按钮
        self.exit = QtWidgets.QPushButton(Form)
        self.exit.setGeometry(QtCore.QRect(380, 510, 112, 34))
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(self.exit_chat)
        #删除好友按钮
        self.delete = QtWidgets.QPushButton(Form)
        self.delete.setGeometry(QtCore.QRect(240, 250, 112, 34))
        self.delete.setObjectName("delete")
        self.delete.clicked.connect(self.del_friend)
        #self.delete.clicked.connect(self.del)
        #添加好友输入框
        self.new_friend = QtWidgets.QLineEdit(Form)
        self.new_friend.setGeometry(QtCore.QRect(50, 50, 211, 41))
        self.new_friend.setObjectName("new_friend")
        #消息框
        self.conversation = QtWidgets.QTextBrowser(Form)
        self.conversation.setGeometry(QtCore.QRect(380, 130, 431, 241))
        self.conversation.setPlaceholderText("")
        self.conversation.setObjectName("conversation")
        self.conversation.textChanged.connect(self.move_end)
        #输入框
        self.msg_input = QtWidgets.QTextEdit(Form)
        self.msg_input.setGeometry(QtCore.QRect(380, 390, 431, 111))
        self.msg_input.setObjectName("msg_input")


        #好友列表
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(50, 170, 161, 41))
        self.comboBox.setObjectName("comboBox")
        self.load_friends()

        #"好友列表"
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(450, 90, 81, 18))
        self.label.setObjectName("label")
        #"聊天对象"
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 81, 18))
        self.label_2.setObjectName("label_2")
        #聊天对象名字
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(550, 90, 81, 18))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    #将消息框移动到最下面
    def move_end(self):
        self.conversation.moveCursor(QtGui.QTextCursor.End)
    def test(self):
        print("test")
        self.tip = tip("test")

    #加载好友
    def load_friends(self):
        '''
        while true比较暴力 有改进空间
        '''
        print('load_friends')
        self.comboBox.addItem("我的好友")
        try:
            res = requests.post("http://yourdomin/functions/ask_friends",data = {"username":self.username})
            res = json.loads(res.text)
            for i in res["detail"]:
                self.comboBox.addItem(i)
        except:
            print("服务器连接失败 请重新打开")
            sleep(1)
            self.tip = tip("服务器连接失败 请重新打开")
            pass

    #选择好友聊天
    def select_friend(self):
        if self.online ==True:
            print("当前正在聊天")
            self.tip = tip("当前正在聊天")
        elif (self.comboBox.currentIndex()!=0):
            self.friend = self.comboBox.currentText()
            print("select_friend: "+ self.friend)
            self.user =client(self.username)
            if self.user.state==True:
                self.label_3.setText(self.friend)
                self.online = True
                self.thread = Mythread()
                self.thread._signal.connect(response)
                self.thread.start()
            else:
                print("连接服务器失败")
                self.tip = tip("连接聊天服务器失败")


    #退出聊天
    def exit_chat(self):
        if self.online == True:
            print('exit_chat')
            self.online = False
            self.thread._signal.emit([end_code])
            self.label_3.setText("")
            self.conversation.setText("")
            self.messages = []
        else:
            print("不在线")

    #发送
    def send_msg(self):
        if self.online==True:
            print("send_msg")
            msg = self.msg_input.toPlainText()
            self.msg_input.setText("")
            if msg!="":
                self.user.send(self.friend, msg)
                self.messages = self.messages+['            '+msg]
                self.conversation.setText('\n'.join(self.messages))
            else:
                print("消息为空")
        else:
            print("不在线")
            self.tip = tip("未选择好友聊天")

    #添加好友
    def add_friend(self):
        print("add_friend")
        new = self.new_friend.text()
        self.new_friend.setText("")
        if new!='':
            res = requests.post("http://yourdomin/functions/add_friend", data={"user1": self.username,"user2": new})
            res = json.loads(res.text)
            if res['result']=='add succeed':
                #改进考虑消息弹出框
                print("添加成功")
                self.tip = tip("添加成功")
                self.comboBox.addItem(new)
            elif res['result'] == 'has existed':
                print("已经存在此好友")
                self.tip = tip("已经存在此好友")
            else:
                print("用户不存在")
                self.tip = tip("用户不存在")
        else:
            print("空的")

    #删除好友
    def del_friend(self):
        print("def_friend")
        if self.comboBox.currentIndex()!=0:
            to_del = self.comboBox.currentText()
            res = requests.post("http://yourdomin/functions/del_friend", data={"user1": self.username,"user2": to_del})
            res = json.loads(res.text)
            if res['result']=='delete succeed':
                #改进考虑消息弹出框
                print("删除成功")
                self.tip = tip("删除成功")
                self.comboBox.removeItem(self.comboBox.currentIndex())
            else:
                print("删除失败")
                self.tip = tip("删除失败")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "summer V1.0 ※用户名："+self.username))
        self.add.setText(_translate("Form", "添加好友"))
        self.send.setText(_translate("Form", "发送"))
        self.exit.setText(_translate("Form", "结束聊天"))
        self.label.setText(_translate("Form", "聊天对象： "))
        self.label_2.setText(_translate("Form", "好友列表"))
        self.chat.setText(_translate("Form", "发起聊天"))
        self.delete.setText(_translate("Form", "删除好友"))

class Mythread(QtCore.QThread):
    _signal = pyqtSignal(list)

    def __init__(self):
        super(Mythread, self).__init__()

    def run(self):
        global main
        while True:
            sleep(0.3)
            res = main.user.recv()
            print(res)
            try:
                if res['result']=='user has been online':
                    self._signal.emit([isonline_code])
                elif res['from'] != main.user.username:
                    if res['from']==main.friend:
                        res = res['message']
                        self._signal.emit([res])
                    else:
                        self._signal.emit([friend_code,res['from']])

            except:
                pass

def response(msg):
    global main
    if msg[0] == end_code:
        print("线程结束")
        return
    elif msg[0] == friend_code:
        main.tip = tip(msg[1]+" 正在找你聊天")
    elif msg[0] == isonline_code:
        global temp
        temp = tip("用户已在线")
        main.w.close()
    else:
        main.messages = main.messages + [msg[0]]
        main.conversation.setText('\n'.join(main.messages))


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = login()
    sys.exit(app.exec_())
