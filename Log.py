# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Log.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import time
import tkinter
import mysql.connector as mc
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import *

class Ui_Log(object):

    def si(self):
        from sng import Ui_Sng
        self.Windows = QtWidgets.QMainWindow()
        self.uis = Ui_Sng()
        self.uis.setupUi(self.Windows)
        MainWindow.hide()
        self.Window.show()

    def us(self):
        us = self.lineEdit.text()
        self.ui.label.setText(us)
        MainWindow.close()




    def ope(self):
        from Dashboard import Ui_Dash
        self.us = self.lineEdit.text()
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_Dash()
        self.ui.setupUi(self.Window)
        self.Window.show()
        roo = tkinter.Tk()
        btn = Button(roo, text='Get Data', command=self.clicker)
        btn.pack(pady=10)
        btn1 = Button(roo, text='Close', command=roo.destroy)
        btn1.pack(pady=20)
        roo.mainloop()

    def clicker(self):
        us = self.lineEdit.text()
        self.ui.label.setText(us)
        MainWindow.close()

    '''def pop_Window(self, text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.critical)
        msg.setText("{}".format(text))
        msg.setInformativeText("{}".format(text))
        msg.setWindowTitle("{}".format(text))'''

    def log(self):
        '''if len(self.lineEdit_2.text()) <= 1:
            self.pop_Window('Enter a Valid Password')
        else:
            pass'''
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="H@rSHiTR24",
                database="expense"
            )
            una = self.lineEdit.text()
            pas = self.lineEdit_2.text()
            us = self.lineEdit.text()
            myc = mydb.cursor()
            sql = "select * from User Where Username = '" + una + "' and Password = '" + pas + "'"
            myc.execute(sql)
            val = myc.fetchall()

            if len(val) >= 1:
                self.ope()

                print("data found")

            else:
                print("No data found")


        except mc.Error as e:
            print("Error occured")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1186, 694)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1186, 694))
        self.label.setStyleSheet("background-color: rgb(27, 249 , 72);")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("IMG/1018911094.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(850, 130, 200, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(770, 230, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(770, 280, 311, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(770, 330, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(770, 380, 311, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(850, 450, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(27, 249, 72);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.log)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(800, 520, 100, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(910, 520, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 0, 100);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.si)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Log In"))
        self.label_3.setText(_translate("MainWindow", "Username"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Log In"))
        self.label_5.setText(_translate("MainWindow", "New User ?"))
        self.pushButton_2.setText(_translate("MainWindow", "Sign Up"))


if __name__ == "__main__":
    import sys

    app1 = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Log()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app1.exec_())


