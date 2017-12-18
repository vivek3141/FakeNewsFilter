import sys
sys.path.append("./Files")
from PyQt4 import QtCore, QtGui, uic 
import numpy as np
import sqlite3 as sql
import urllib
from bs4 import BeautifulSoup
 
from main_auto import * 
import check_mod  
class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): 
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self) 
        QtCore.QObject.connect(self.actionCheck,QtCore.SIGNAL('triggered()'),self.check)                    
        self.conn = sql.connect("website.db")
        self.cursor = self.conn.cursor()
        QtCore.QObject.connect(self.pb,QtCore.SIGNAL('clicked()'),self.check)
    def check(self):
        url = self.le.text()


        print(self.data(url))
    def data(self, url):
        
        try:
            url = str(url)
        except ValueError:
            QtGui.QMessageBox.information(self,  "An Error occurred:",  "Please enter a valid url")
            return False
        url = url.strip()
        if(url.find("http://www.") == 0):
            url = url.replace("http://www.", "")
        elif(url.find("https://www.") == 0):
            url = url.replace("https://www.", "")
        elif(url.find("www.") == 0):
            url = url.replace("www.", "")
        elif(url.find("http://") == 0):
            url = url.replace("http://", "")
        elif(url.find("https://") == 0):
            url = url.replace("https://", "")
        if(url.find("/") != -1):
            url = url.replace(url[url.find("/"):], "")
        try:
            a = urllib.request.urlopen("http://"+url)
        except:
            QtGui.QMessageBox.information(self,  "An Error occurred:",  "Please enter a valid url")
            return False
        print(url)
        self.cursor.execute("select Opt from Website where Web = '" + url + "'")
        s = self.cursor.fetchall()
        if(len(s) != 0):
            if(s[0][0] == "Yes"):
                m = QtGui.QMessageBox()
                m.setText("It is most likely real")
                m.setStyleSheet('background-color: rgb(0, 255, 0); color: rgb(255, 255, 255);font: 75 18pt "Berlin Sans FB Demi";')
                m.show()
                m.exec_()
                return True
            elif(s[0][0] == "No"):
                m = QtGui.QMessageBox()
                m.setText("It is most likely fake")
                m.setStyleSheet('background-color: rgb(255, 0, 0); color: rgb(255, 255, 255);font: 75 18pt "Berlin Sans FB Demi";')
                m.show()
                m.exec_()
                return False
        else:
            print("hi")
            return self.neural(url)
    def datat(self, url):

        try:
            url = str(url)
        except ValueError:
            return False
        url = url.strip()
        if(url.find("http://www.") == 0):
            url = url.replace("http://www.", "")
        elif(url.find("https://www.") == 0):
            url = url.replace("https://www.", "")
        elif(url.find("www.") == 0):
            url = url.replace("www.", "")
        elif(url.find("http://") == 0):
            url = url.replace("http://", "")
        elif(url.find("https://") == 0):
            url = url.replace("https://", "")
        if(url.find("/") != -1):
            url = url.replace(url[url.find("/"):], "")
        print(url)
        self.cursor.execute("select Opt from Website where Web = '" + url + "'")
        s = self.cursor.fetchall()
        if(len(s) != 0):
            if(s[0][0] == "Yes"):
                return True
                lblr.setText("")
            elif(s[0][0] == "No"):
                print("bad")
                return False
                lblr.setText("")
        else:
            print("hi")

    def Check(self):
        try:
            c = check_mod.MyForm()
            c.show()
            c.exec_()
        except:
            m = QtGui.QMessageBox()
            m.setText("Not quite sure")
            m.setStyleSheet('background-color: rgb(255, 255, 0); color: rgb(255, 255, 255);font: 75 18pt "Berlin Sans FB Demi";')
            m.show()
            m.exec_()
            return False
    def neural(self, url):
        try:
            response = urllib.request.urlopen("https://" + str(url))

            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            z = 0
            print(soup.find_all('a'))
            for link in soup.find_all('a'):
                u = link.get('href')
                print(u)
                a = self.datat(u)
                
                if(a):
                    z = z + 1
                elif(a == False):
                    z = z -1
                elif(a == None):
                    z = z
            print(z)
        except:
            m = QtGui.QMessageBox()
            m.setText("Not quite sure")
            m.setStyleSheet('background-color: rgb(255, 255, 0); color: rgb(255, 255, 255);font: 75 18pt "Berlin Sans FB Demi";')
            m.show()
            m.exec_()
            return False
            
        
        if(z>0):
            m = QtGui.QMessageBox()
            m.setText("It is most likely real")
            m.setStyleSheet('background-color: rgb(0, 255, 0); color: rgb(255, 255, 255);font: 75 18pt "Berlin Sans FB Demi";')
            m.show()
            m.exec_()
        elif(z<0):
            m = QtGui.QMessageBox()
            m.setText("It is most likely fake")
            m.setStyleSheet('background-color: rgb(255, 0, 0); color: rgb(255, 255, 255);font: 75 18pt "Berlin Sans FB Demi";')
            m.show()
            m.exec_()
        else:
            m = QtGui.QMessageBox()
            m.setText("Not quite sure")
            m.setStyleSheet('background-color: rgb(255, 255, 0); color: rgb(255, 255, 255);font: 75 18pt "Berlin Sans FB Demi";')
            m.show()
            m.exec_()

        
            
            
        """
        
        X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
        y = np.array([[0,1,1,0]]).T
        syn0 = 2*np.random.random((3,4)) - 1
        syn1 = 2*np.random.random((4,1)) - 1
        for j in xrange(60000):
            l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
            l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
            l2_delta = (y - l2)*(l2*(1-l2))
            l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1))
            syn1 += l1.T.dot(l2_delta)
            syn0 += X.T.dot(l1_delta)
        """

         
 
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_() 
