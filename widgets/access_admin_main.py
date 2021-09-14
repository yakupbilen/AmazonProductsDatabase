# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Yakup Bilen\PycharmProjects\database\widgets\uies\access_admin_main.ui'
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
from widgets.access_admin import Ui_AccessAdmin

class Ui_AccessAdminMain(QtWidgets.QMainWindow):
    def __init__(self, id):
        self.id = id
        super(Ui_AccessAdminMain, self).__init__()
        self.ui = Ui_AccessAdminMainWindow()
        self.ui.setupUi(self,self.id)


class Ui_AccessAdminMainWindow(object):
    def setupUi(self, AccessAdminMainWindow, id):
        AccessAdminMainWindow.setObjectName("AccessAdminMainWindow")
        AccessAdminMainWindow.resize(400, 600)
        self.centralwidget = QtWidgets.QWidget(AccessAdminMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.btnLogout = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogout.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnLogout.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons8-logout-rounded-left-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLogout.setIcon(icon)
        self.btnLogout.setObjectName("btnLogout")
        self.horizontalLayout_4.addWidget(self.btnLogout)
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.btnAccessAdminMenu = QtWidgets.QPushButton(self.centralwidget)
        self.btnAccessAdminMenu.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnAccessAdminMenu.setFont(font)
        self.btnAccessAdminMenu.setObjectName("btnAccessAdminMenu")
        self.horizontalLayout.addWidget(self.btnAccessAdminMenu)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.btnPassword = QtWidgets.QPushButton(self.centralwidget)
        self.btnPassword.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnPassword.setFont(font)
        self.btnPassword.setObjectName("btnPassword")
        self.horizontalLayout_7.addWidget(self.btnPassword)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem13)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.setStretch(6, 2)
        self.verticalLayout_2.setStretch(7, 3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        AccessAdminMainWindow.setCentralWidget(self.centralwidget)

        self.id = id
        # Windows
        self.read = Ui_Reader(self.id)
        self.passwordDialog = Ui_Password(self.id)
        self.loginWindow = widgets.login.Ui_Login()
        self.write = Ui_Writer(self.id)
        self.admin = Ui_Admin(self.id)
        self.accessAdmin = Ui_AccessAdmin(self.id)

        # Buttons
        self.btnLogout.clicked.connect(self.logout)
        self.btnPassword.clicked.connect(self.password)
        self.btnReadMenu.clicked.connect(self.readMenu)
        self.btnWriteMenu.clicked.connect(self.writeMenu)
        self.btnAdminMenu.clicked.connect(self.adminMenu)
        self.btnAccessAdminMenu.clicked.connect(self.accessAdminMenu)

        self.retranslateUi(AccessAdminMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AccessAdminMainWindow)

    def accessAdminMenu(self):
        self.accessAdmin.exec_()

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

    def retranslateUi(self, AccessAdminMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AccessAdminMainWindow.setWindowTitle(_translate("AccessAdminMainWindow", "MainWindow"))
        self.btnLogout.setText(_translate("AccessAdminMainWindow", "Logout"))
        self.btnReadMenu.setText(_translate("AccessAdminMainWindow", "Read Mode"))
        self.btnWriteMenu.setText(_translate("AccessAdminMainWindow", "Write Mode"))
        self.btnAdminMenu.setText(_translate("AccessAdminMainWindow", "Admin Mode"))
        self.btnAccessAdminMenu.setText(_translate("AccessAdminMainWindow", "Access Admin Mode"))
        self.btnPassword.setText(_translate("AccessAdminMainWindow", "Change Password"))
import icons_rc