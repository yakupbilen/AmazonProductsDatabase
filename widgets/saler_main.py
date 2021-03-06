# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Yakup Bilen\PycharmProjects\database\widgets\uies\saler_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import widgets.login
from widgets.password import Ui_Password
from widgets.make_sale import Ui_MakeSale

class Ui_SalerMain(QtWidgets.QMainWindow):
    def __init__(self, id):
        super(Ui_SalerMain, self).__init__()
        self.id = id
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self,self.id)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow, id):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.btnSale = QtWidgets.QPushButton(self.centralwidget)
        self.btnSale.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnSale.setFont(font)
        self.btnSale.setObjectName("btnSale")
        self.horizontalLayout_5.addWidget(self.btnSale)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.btnPassword = QtWidgets.QPushButton(self.centralwidget)
        self.btnPassword.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnPassword.setFont(font)
        self.btnPassword.setObjectName("btnPassword")
        self.horizontalLayout_7.addWidget(self.btnPassword)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.setStretch(3, 2)
        self.verticalLayout_2.setStretch(4, 3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.id = id

        # Windows
        self.makeSale = Ui_MakeSale(self.id)
        self.passwordDialog = Ui_Password(self.id)
        self.loginWindow = widgets.login.Ui_Login()

        # Buttons
        self.btnLogout.clicked.connect(self.logout)
        self.btnPassword.clicked.connect(self.password)
        self.btnSale.clicked.connect(self.sale)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def sale(self):
        self.makeSale.exec_()

    def password(self):
        self.passwordDialog.exec_()

    def logout(self):
        self.centralwidget.window().close()
        self.loginWindow.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnLogout.setText(_translate("MainWindow", "Logout"))
        self.btnSale.setText(_translate("MainWindow", "Make Sale"))
        self.btnPassword.setText(_translate("MainWindow", "Change Password"))
import icons_rc
