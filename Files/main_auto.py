# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(579, 320)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 801, 541))
        self.graphicsView.setStyleSheet(_fromUtf8("background-image: url(:/Back/bluegruge.jpg);"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.le = QtGui.QLineEdit(self.centralwidget)
        self.le.setGeometry(QtCore.QRect(130, 80, 411, 27))
        self.le.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.le.setObjectName(_fromUtf8("le"))
        self.lbl_2 = QtGui.QLabel(self.centralwidget)
        self.lbl_2.setGeometry(QtCore.QRect(40, 80, 70, 21))
        self.lbl_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 12pt \"Berlin Sans FB\";"))
        self.lbl_2.setObjectName(_fromUtf8("lbl_2"))
        self.pb = QtGui.QPushButton(self.centralwidget)
        self.pb.setGeometry(QtCore.QRect(250, 150, 112, 34))
        self.pb.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pb.setObjectName(_fromUtf8("pb"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 579, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_New_Website = QtGui.QAction(MainWindow)
        self.actionAdd_New_Website.setObjectName(_fromUtf8("actionAdd_New_Website"))
        self.actionCheck = QtGui.QAction(MainWindow)
        self.actionCheck.setObjectName(_fromUtf8("actionCheck"))
        self.menuFile.addAction(self.actionAdd_New_Website)
        self.menuFile.addAction(self.actionCheck)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Fake News Filter", None))
        self.lbl_2.setText(_translate("MainWindow", "URL", None))
        self.pb.setText(_translate("MainWindow", "Submit", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionAdd_New_Website.setText(_translate("MainWindow", "Add New Website", None))
        self.actionAdd_New_Website.setShortcut(_translate("MainWindow", "Ctrl+Shift+A", None))
        self.actionCheck.setText(_translate("MainWindow", "Check", None))
        self.actionCheck.setShortcut(_translate("MainWindow", "Ctrl+Shift+C", None))

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

