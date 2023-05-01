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

        try:
            url = 'https://ipelab.ru/serv/atten.php'
            payload = {'py_get_comm' : 1,}
            
            x = requests.get(url, params=payload)
            #print(x.text)
            response = json.loads(x.text)

            self.StudentsList = {}

            for i in range(0, len(response)):
                #print(response[i]['studak'], response[i]['name'])
                self.StudentsList.update({response[i]['studak'] : response[i]['name']})

            print('Список студентов получен')
        except:
            print('Ошибка получения списка студентов')
            
        self.setupUi()
    

    def setupUi(self):
        self.setWindowTitle("Attendance")
        self.move(0, 0)
        self.resize(500, 200)
        self.LeftBar = QPushButton()
        self.LeftBar.resize(100, 100)
        self.LeftBar.move(100, 100)

        self.Label = QLabel(self)
        self.Label.resize(500, 100)
        self.Label.move(0, 25)
        
        self.lineEditStudak = QLineEdit(self)
        self.lineEditStudak.resize(500, 50)
        self.lineEditStudak.setFont(QtGui.QFont("Times", 25, QtGui.QFont.Bold))
        self.lineEditStudak.setPlaceholderText("Номер студенческого")
        self.lineEditStudak.textEdited.connect(self.my_func)

        self.lineEditLessonNumber = QLineEdit(self)
        self.lineEditLessonNumber.resize(500, 50)
        self.lineEditLessonNumber.move(0, 100)
        self.lineEditLessonNumber.setFont(QtGui.QFont("Times", 25, QtGui.QFont.Bold))
        self.lineEditLessonNumber.setPlaceholderText("Номер пары")



    def my_func(self, text):
        try:
            self.Label.setText(fonts.Fonts.ConsoleFont(self.StudentsList[text]))
            self.lineEditStudak.clear()

            if (self.lineEditLessonNumber.text() == ''):
                lesson_number = get_current_time()
            else:
                lesson_number = self.lineEditLessonNumber.text()
            
            print('Номер пары:', lesson_number)

            url = 'https://ipelab.ru/serv/atten.php'
            datetime.today().strftime('%Y-%m-%d')
            payload =   {
                            'py_post_comm'  : 1,
                            'student'       : text,
                            'cur_date'      : datetime.today().strftime('%Y-%m-%d'),
                            'cur_lesson'    : lesson_number
                        }
            
            x = requests.post(url, data=payload)
            print(self.StudentsList[text], x.text)

        except:
            self.Label.setText(fonts.Fonts.ConsoleFont('Не введен номер студента'))
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
