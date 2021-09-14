# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Yakup Bilen\PycharmProjects\database\widgets\uies\admin_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.reader import Ui_Reader
from widgets.writer import Ui_Writer
import widgets.login
from widgets.password import Ui_Password
from widgets.admin import Ui_Admin



class Ui_AdminMain(QtWidgets.QMainWindow):
    def __init__(self,id):
        self.id = id
        super(Ui_AdminMain, self).__init__()
        self.ui = Ui_AdminMainWindow()
        self.ui.setupUi(self,self.id)



class Ui_AdminMainWindow(object):
    def setupUi(self, AdminMainWindow,id):
        AdminMainWindow.setObjectName("AdminMainWindow")
        AdminMainWindow.resize(400, 450)
        self.centralwidget = QtWidgets.QWidget(AdminMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.btnLogout_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogout_2.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnLogout_2.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons8-logout-rounded-left-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLogout_2.setIcon(icon)
        self.btnLogout_2.setObjectName("btnLogout_2")
        self.horizontalLayout_4.addWidget(self.btnLogout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_4.setStretch(0, 7)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.btnReadMenu = QtWidgets.QPushButton(self.centralwidget)
        self.btnReadMenu.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnReadMenu.setFont(font)
        self.btnReadMenu.setObjectName("btnReadMenu")
        self.horizontalLayout_5.addWidget(self.btnReadMenu)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.btnWriteMenu = QtWidgets.QPushButton(self.centralwidget)
        self.btnWriteMenu.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnWriteMenu.setFont(font)
        self.btnWriteMenu.setObjectName("btnWriteMenu")
        self.horizontalLayout_6.addWidget(self.btnWriteMenu)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.btnAdminMenu = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdminMenu.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnAdminMenu.setFont(font)
        self.btnAdminMenu.setObjectName("btnAdminMenu")
        self.horizontalLayout_8.addWidget(self.btnAdminMenu)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.btnPassword = QtWidgets.QPushButton(self.centralwidget)
        self.btnPassword.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnPassword.setFont(font)
        self.btnPassword.setObjectName("btnPassword")
        self.horizontalLayout_7.addWidget(self.btnPassword)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem11)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.setStretch(5, 2)
        self.verticalLayout_2.setStretch(6, 3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        AdminMainWindow.setCentralWidget(self.centralwidget)
        self.id = id
        # Windows
        self.read = Ui_Reader(self.id)
        self.passwordDialog = Ui_Password(self.id)
        self.loginWindow = widgets.login.Ui_Login()
        self.write = Ui_Writer(self.id)
        self.admin = Ui_Admin(self.id)

        # Buttons
        self.btnLogout_2.clicked.connect(self.logout)
        self.btnPassword.clicked.connect(self.password)
        self.btnReadMenu.clicked.connect(self.readMenu)
        self.btnWriteMenu.clicked.connect(self.writeMenu)
        self.btnAdminMenu.clicked.connect(self.adminMenu)

        self.retranslateUi(AdminMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminMainWindow)

    def adminMenu(self):
        self.admin.exec_()

    def writeMenu(self):
        self.write.exec_()

    def readMenu(self):
        self.read.exec_()

    def password(self):
        self.passwordDialog.exec_()

    def logout(self):
        self.centralwidget.window().close()
        self.loginWindow.show()

    def retranslateUi(self, AdminMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminMainWindow.setWindowTitle(_translate("AdminMainWindow", "MainWindow"))
        self.btnLogout_2.setText(_translate("AdminMainWindow", "Logout"))
        self.btnReadMenu.setText(_translate("AdminMainWindow", "Read Mode"))
        self.btnWriteMenu.setText(_translate("AdminMainWindow", "Write Mode"))
        self.btnAdminMenu.setText(_translate("AdminMainWindow", "Admin Mode"))
        self.btnPassword.setText(_translate("AdminMainWindow", "Change Password"))
import icons_rc
