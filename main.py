from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import sys
import fonts

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.StudentsList = {
            '123' : 'Влад',
            '2' : 'Миша'
        }
        self.setupUi()
    
    def setupUi(self):
        self.setWindowTitle("Hello")
        self.move(0, 0)
        self.resize(1920, 1080)
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
        except:
            self.Label.setText(fonts.Fonts.ConsoleFont('Не введен номер студента'))
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())