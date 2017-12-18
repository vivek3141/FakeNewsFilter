import sys
from check_auto import * 
import sqlite3 as sql
import numpy
import urllib.request
from bs4 import BeautifulSoup

 
class MyForm(QtGui.QDialog):
    def __init__(self,parent=None): 
        QtGui.QWidget.__init__(self, parent) 
        self.ui = Ui_Dialog() 
        self.ui.setupUi(self) 
        #self.ui.setStyleSheet("")
        self.conn = sql.connect("website.db")
        self.cursor = self.conn.cursor()
        QtCore.QObject.connect(self.ui.pb,QtCore.SIGNAL('clicked()'),self.check)
    def check(self):
        url = self.ui.le.text()
        print(self.data(url))
    def data(self, url):

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
            self.ui.lbl.setText(s[0][0])
            if(s[0][0] == "Yes"):
                m = QtGui.QMessageBox()
                m.setText("It is most likely real")
                m.setStyleSheet('background-color: rgb(0, 255, 0); color: rgb(255, 255, 255);font: 75 18pt "Berlin Sans FB Demi";')
                m.show()
                m.exec_()
            if(s[0][0] == "No"):
                m = QtGui.QMessageBox()
                m.setText("It is most likely fake")
                m.setStyleSheet('background-color: rgb(255, 0, 0); color: rgb(255, 255, 255);font: 75 18pt "Berlin Sans FB Demi";')
                m.show()
                m.exec_()
            else:
                return self.neural(url)
    def neural(self, url):
        response = urllib.request.urlopen("https://" + str(url))
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.head.title.string)
        
    

         
if __name__=="__main__": 
    app=QtGui.QApplication(sys.argv) 
    myapp=MyForm()
    myapp.show()
    sys.exit(app.exec_()) 
