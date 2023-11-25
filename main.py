
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QTextEdit


def serch_search():
    directory = './folder'
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Печать пути к файлу
            return os.path.join(root, file)


class Search(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Search')

        self.btn = QPushButton('Поиск', self)
        self.btn.resize(100, 50)
        self.btn.move(5, 5)

        self.btn1 = QPushButton('Создать', self)
        self.btn1.resize(100, 50)
        self.btn1.move(105, 5)

        self.btn2 = QPushButton('a', self)
        self.btn2.resize(100, 50)
        self.btn2.move(205, 5)

        self.btn3 = QPushButton('y', self)
        self.btn3.resize(100, 50)
        self.btn3.move(305, 5)

        self.btn4 = QPushButton('ы', self)
        self.btn4.resize(100, 50)
        self.btn4.move(405, 5)

        self.LCD = QTextEdit(self)
        self.LCD.resize(490, 350)
        self.LCD.move(5, 60)
        text = serch_search()
        self.LCD.setPlainText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Search()
    ex.show()
    sys.exit(app.exec_())

