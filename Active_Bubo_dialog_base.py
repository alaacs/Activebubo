# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Active_Bubo_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ActiveBuboDialogBase(object):
    def setupUi(self, ActiveBuboDialogBase):
        ActiveBuboDialogBase.setObjectName("ActiveBuboDialogBase")
        ActiveBuboDialogBase.resize(400, 300)
        self.button_box = QtWidgets.QDialogButtonBox(ActiveBuboDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")

        self.retranslateUi(ActiveBuboDialogBase)
        self.button_box.accepted.connect(ActiveBuboDialogBase.accept)
        self.button_box.rejected.connect(ActiveBuboDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(ActiveBuboDialogBase)

    def retranslateUi(self, ActiveBuboDialogBase):
        _translate = QtCore.QCoreApplication.translate
        ActiveBuboDialogBase.setWindowTitle(_translate("ActiveBuboDialogBase", "Active Bubo"))
