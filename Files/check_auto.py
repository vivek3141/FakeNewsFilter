# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(570, 347)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 0);\n"
""))
        self.le = QtGui.QLineEdit(Dialog)
        self.le.setGeometry(QtCore.QRect(120, 40, 411, 27))
        self.le.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.le.setObjectName(_fromUtf8("le"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 70, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.pb = QtGui.QPushButton(Dialog)
        self.pb.setGeometry(QtCore.QRect(230, 100, 112, 34))
        self.pb.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pb.setObjectName(_fromUtf8("pb"))
        self.lbl = QtGui.QLabel(Dialog)
        self.lbl.setGeometry(QtCore.QRect(230, 180, 211, 101))
        self.lbl.setStyleSheet(_fromUtf8("font: 75 26pt \"Berlin Sans FB Demi\";\n"
"color: rgb(255, 255, 255);"))
        self.lbl.setObjectName(_fromUtf8("lbl"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "URL", None))
        self.pb.setText(_translate("Dialog", "Submit", None))
        self.lbl.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

