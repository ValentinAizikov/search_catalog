import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QVBoxLayout, QListWidget, QLineEdit


class Search(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(490, 415, 490, 415)
        self.setWindowTitle('Менеджер файлов')

        self.btn = QPushButton('Поиск', self)
        self.btn.resize(95, 50)
        self.btn.move(5, 5)
        self.btn.clicked.connect(self.butn_search)
        self.btn.layout = QVBoxLayout()
        self.btn.layout.addWidget(self.btn)
        self.new_window = None

        self.btn1 = QPushButton('Создать', self)
        self.btn1.resize(95, 50)
        self.btn1.move(100, 5)
        self.btn1.clicked.connect(self.butn_sozdat)
        self.btn1.layout = QVBoxLayout()
        self.btn1.layout.addWidget(self.btn1)
        self.new_window1 = None

        self.btn2 = QPushButton('Удалить', self)
        self.btn2.resize(95, 50)
        self.btn2.move(195, 5)
        self.btn2.clicked.connect(self.butn_delete)
        self.btn2.layout = QVBoxLayout()
        self.btn2.layout.addWidget(self.btn2)
        self.new_window2 = None

        self.btn3 = QPushButton('Переименовать', self)
        self.btn3.resize(95, 50)
        self.btn3.move(290, 5)
        self.btn3.clicked.connect(self.butn_rename)
        self.btn3.layout = QVBoxLayout()
        self.btn3.layout.addWidget(self.btn3)
        self.new_window3 = None

        self.btn4 = QPushButton('Редактировать\nсодержимое', self)
        self.btn4.resize(100, 50)
        self.btn4.move(385, 5)
        self.btn4.clicked.connect(self.butn_edit)
        self.btn4.layout = QVBoxLayout()
        self.btn4.layout.addWidget(self.btn4)
        self.new_window4 = None

        self.LCD = QListWidget(self)
        self.LCD.resize(479, 350)
        self.LCD.move(5, 60)
        text = self.serch_search()
        self.LCD.addItem(text)
    
    def serch_search(self):
        directory = './folder'
        spis = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Печать пути к файлу
                return os.path.join(root, file)
    
    def butn_search(self):
        if not self.new_window:  # Проверяем, создано ли уже новое окно
            self.new_window = Research()  # Если нет, создаем новое окно
            self.new_window.show()  # Отображаем новое окно
    
    def butn_sozdat(self):
        if not self.new_window1:
            self.new_window1 = Sozdanie()
            self.new_window1.show()
    
    def butn_delete(self):
        if not self.new_window2:
            self.new_window2 = Delete()
            self.new_window2.show()

    def butn_rename(self):
        if not self.new_window3:
            self.new_window3 = Rename()
            self.new_window3.show()
    
    def butn_edit(self):
        if not self.new_window4:
            self.new_window4 = Edit()
            self.new_window4.show()


class Research(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Поиск')
        self.setGeometry(400, 415, 400, 415)

        self.LCD1 = QLineEdit(self)
        self.LCD1.resize(300, 20)
        self.LCD1.move(5, 20)


class Sozdanie(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Создать файл')
        self.setGeometry(400, 415, 400, 415)

        self.LCD1 = QLineEdit(self)
        self.LCD1.resize(300, 20)
        self.LCD1.move(5, 20)


class Delete(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Удалить файл')
        self.setGeometry(400, 415, 400, 415)


class Rename(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Переименовать файл')
        self.setGeometry(400, 415, 400, 415)

        self.LCD1 = QLineEdit(self)
        self.LCD1.resize(300, 20)
        self.LCD1.move(5, 20)


class Edit(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Редактировать файл')
        self.setGeometry(400, 415, 400, 415)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Search()
    ex.show()
    sys.exit(app.exec_())