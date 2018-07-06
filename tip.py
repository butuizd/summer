# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tip.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class tip(object):
    def __init__(self,message):
        self.w = QtWidgets.QWidget()
        self.setupUi(self.w,message)
        self.w.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.w.show()
    def setupUi(self, Form,message):
        Form.setObjectName("提醒")
        Form.resize(377, 249)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 150, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.test)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 60, 250, 51))
        self.label.setText(message)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def test(self):
        self.w.close()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "确定"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    #w1 = QtWidgets.QWidget()
    main = tip()
    #main.setupUi(w1)
    #w1.show()
    sys.exit(app.exec_())
