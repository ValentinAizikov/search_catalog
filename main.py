import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QVBoxLayout, QListWidget, QLineEdit
from docx import Document
from openpyxl import Workbook


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
        self.serch_search()
    
    def serch_search(self):
        directory = './folder'
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Печать пути к файлу
                self.LCD.addItem(os.path.join(root, file))
    
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

        self.btn5 = QPushButton('Поиск', self)
        self.btn5.resize(85, 22)
        self.btn5.move(310, 19)


class Sozdanie(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Создать файл')
        self.setGeometry(400, 415, 400, 415)

        self.LCD2 = QLineEdit(self)
        self.LCD2.resize(300, 20)
        self.LCD2.move(5, 20)

        self.btn5 = QPushButton('Создать', self)
        self.btn5.resize(85, 22)
        self.btn5.move(310, 19)
        self.btn5.clicked.connect(self.texty)

        self.LCD = QListWidget(self)
        self.LCD.resize(390, 350)
        self.LCD.move(5, 60)
        self.serch_search()

    def serch_search(self):
        directory = './folder'
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Печать пути к файлу
                self.LCD.addItem(os.path.join(root, file))

    def texty(self):
        text = self.LCD2.text()
        if '.docx' in text:
            self.close()
            return self.create_docx_file(text)
        elif '.xlsx' in text:
            self.close()
            return self.create_xlsx_file(text)
        elif '.txt' in text:
            self.close()
            return self.create_txt_file(text)
        elif '.docx' and '.xlsx' and '.txt' not in text:
            pass

    def create_docx_file(self, name):
        puti = './folder/' + name
        document = Document()
        document.save(puti)
    
    def create_xlsx_file(self, name):
        puti = './folder/' + name
        workbook = Workbook()
        workbook.save(puti)
    
    def create_txt_file(self, name):
        puti = './folder/' + name
        with open(puti, 'w') as file:
            file.close()
    
    def update_file_list(self):
        directory = './folder'
        self.LCD2.clear()
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Печать пути к файлу
                self.LCD2.addItem(os.path.join(root, file))


class Delete(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Удалить файл')
        self.setGeometry(400, 415, 400, 415)

        self.LCD = QListWidget(self)
        self.LCD.resize(390, 380)
        self.LCD.move(5, 30)
        self.serch_search()

        self.btn9 = QPushButton('Удалить', self)
        self.btn9.resize(100, 20)
        self.btn9.move(296, 5)
        self.btn9.clicked.connect(self.ydali)
        self.btn9.layout = QVBoxLayout()
        self.btn9.layout.addWidget(self.btn9)
        self.new_window4 = None
    
    def serch_search(self):
        directory = './folder'
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Печать пути к файлу
                self.LCD.addItem(os.path.join(root, file))

    def ydali(self):
        if not self.new_window4:
            self.new_window4 = Delete_Win()
            self.new_window4.show()
        self.update_file_list()
    
    def update_file_list(self):
        directory = './folder'
        self.LCD.clear()
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Печать пути к файлу
                self.LCD.addItem(os.path.join(root, file))


class Rename(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Переименовать файл')
        self.setGeometry(400, 415, 400, 415)

        self.LCD3 = QLineEdit(self)
        self.LCD3.resize(300, 20)
        self.LCD3.move(5, 20)

        self.btn5 = QPushButton('Переименовать', self)
        self.btn5.resize(85, 22)
        self.btn5.move(310, 19)


class Edit(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Редактировать файл')
        self.setGeometry(400, 415, 400, 415)

        self.LCD4 = QLineEdit(self)
        self.LCD4.resize(390, 380)
        self.LCD4.move(5, 5)

        self.btn5 = QPushButton('Сохранить', self)
        self.btn5.resize(85, 22)
        self.btn5.move(310, 390)


class Delete_Win(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Точно?')
        self.setGeometry(270, 70, 270, 70)

        self.label = QLabel('Вы уверены, что хотите удалить этот файл?', self)
        self.label.move(20, 20)

        self.btn6 = QPushButton('Нет', self)
        self.btn6.resize(65, 22)
        self.btn6.move(60, 40)
        self.btn6.clicked.connect(self.kek)
        self.btn6.layout = QVBoxLayout()
        self.btn6.layout.addWidget(self.btn6)
        self.new_window = None

        self.btn7 = QPushButton('Да', self)
        self.btn7.resize(65, 22)
        self.btn7.move(140, 40)
        self.btn7.clicked.connect(self.lol)
        self.btn7.layout = QVBoxLayout()
        self.btn7.layout.addWidget(self.btn7)
        self.new_window = None

    def lol(self):
        return True
    
    def kek(self):
        self.close()
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Search()
    ex.show()
    sys.exit(app.exec_())