from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import sys
import fonts
import requests
import urllib
from urllib.request import urlopen
from urllib.request import Request
import json
from datetime import datetime


def get_current_time():
    ct = datetime.now()

    currentTimeInMinutes = ct.minute + ct.hour * 60

    if currentTimeInMinutes in range(0, 635):
        return 1
    elif currentTimeInMinutes in range(635, 755):
        return 2
    elif currentTimeInMinutes in range(755, 855):
        return 3
    elif currentTimeInMinutes in range(855, 975):
        return 4
    elif currentTimeInMinutes in range(975, 1075):
        return 5
    elif currentTimeInMinutes in range(1075, 1175):
        return 6


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.StudentsList = {
            '123' : 'Влад',
            '0009044070' : 'Миша',
            '0009227889' : 'Петя',
            '0014774697' : 'Влад',
            '0014247922' : 'Леша',
            '0011669327' : 'Коля'
        }
        self.setupUi()
    
    def setupUi(self):
        self.setWindowTitle("Hello")
        self.move(0, 0)
        self.resize(500, 200)
        self.LeftBar = QPushButton()
        self.LeftBar.resize(100, 100)
        self.LeftBar.move(100, 100)
        self.Label = QLabel(self)
        self.Label.resize(500, 100)
        self.Label.move(0, 100)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.resize(1000, 100)
        self.lineEdit.setFont(QtGui.QFont("Times", 25, QtGui.QFont.Bold))
        self.lineEdit.textEdited.connect(self.my_func)

    def my_func(self, text):
        try:
            self.Label.setText(fonts.Fonts.ConsoleFont(self.StudentsList[text]))
            self.lineEdit.clear()

            url = 'https://ipelab.ru/serv/atten.php'
            datetime.today().strftime('%Y-%m-%d')
            payload =   {
                            'py_comm'       : 1,
                            'student'       : text,
                            'cur_date'      : datetime.today().strftime('%Y-%m-%d'),
                            'cur_lesson'    : get_current_time()
                        }
            
            x = requests.post(url, data=json.dumps(payload))
            print(x.text)

        except:
            self.Label.setText(fonts.Fonts.ConsoleFont('Не введен номер студента'))
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
