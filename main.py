import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtWidgets import QLCDNumber, QLabel, QVBoxLayout, QListWidget, QLineEdit
from docx import Document
from openpyxl import Workbook


class Search(QWidget):
    def __init__(self):
        # вызываем конструктор родительского класса
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # устанавливаем размеры окна
        # устанавливаем название окна
        self.setGeometry(490, 415, 490, 415)
        self.setWindowTitle('Менеджер файлов')
        
        # создаем кнопку "Поиск" (устанавливаем размеры кнопки, устанавливаем положение кнопки, подключаем обработчик события для кнопки "Поиск" и т.д.)
        self.btn = QPushButton('Поиск', self)
        self.btn.resize(95, 50)
        self.btn.move(5, 5)
        self.btn.clicked.connect(self.butn_search)
        self.btn.layout = QVBoxLayout()
        self.btn.layout.addWidget(self.btn)
        # создаем переменную new_window и присваиваем ей значение None
        self.new_window = None

        # создаем кнопку "Создать" (устанавливаем размеры кнопки, устанавливаем положение кнопки, подключаем обработчик события для кнопки "Создать" и т.д.)
        self.btn1 = QPushButton('Создать', self)
        self.btn1.resize(95, 50)
        self.btn1.move(100, 5)
        self.btn1.clicked.connect(self.butn_sozdat)
        self.btn1.layout = QVBoxLayout()
        self.btn1.layout.addWidget(self.btn1)
        # создаем переменную new_window1 и присваиваем ей значение None
        self.new_window1 = None

        # создаем кнопку "Удалить" (устанавливаем размеры кнопки, устанавливаем положение кнопки, подключаем обработчик события для кнопки "Удалить" и т.д.)
        self.btn2 = QPushButton('Удалить', self)
        self.btn2.resize(95, 50)
        self.btn2.move(195, 5)
        self.btn2.clicked.connect(self.butn_delete)
        self.btn2.layout = QVBoxLayout()
        self.btn2.layout.addWidget(self.btn2)
        # создаем переменную new_window2 и присваиваем ей значение None
        self.new_window2 = None

        # создаем кнопку "Переименовать" (устанавливаем размеры кнопки, устанавливаем положение кнопки, подключаем обработчик события для кнопки "Переименовать" и т.д.)
        self.btn3 = QPushButton('Переименовать', self)
        self.btn3.resize(95, 50)
        self.btn3.move(290, 5)
        self.btn3.clicked.connect(self.butn_rename)
        self.btn3.layout = QVBoxLayout()
        self.btn3.layout.addWidget(self.btn3)
        # создаем переменную new_window3 и присваиваем ей значение None
        self.new_window3 = None

        # создаем кнопку "Редактировать содержимое" (устанавливаем размеры кнопки, устанавливаем положение кнопки, подключаем обработчик события для кнопки "Редактировать содержимое" и т.д.)
        self.btn4 = QPushButton('Редактировать', self)
        self.btn4.resize(100, 50)
        self.btn4.move(385, 5)
        self.btn4.clicked.connect(self.butn_edit)
        self.btn4.layout = QVBoxLayout()
        self.btn4.layout.addWidget(self.btn4)
        # создаем переменную new_window4 и присваиваем ей значение None
        self.new_window4 = None

        # создаем список LCD (устанавливаем размеры списка, устанавливаем положение списка, вызываем метод serch_search)
        self.LCD = QListWidget(self)
        self.LCD.resize(479, 350)
        self.LCD.move(5, 60)
        self.serch_search()

    # метод, выполняющий поиск (директория в которой будет выполняться поиск, цикл для обхода всех файлов в директории, цикл для обхода каждого файла, добавление файла в список)
    def serch_search(self):
        directory = './folder'
        for root, dirs, files in os.walk(directory):
            for file in files:
                self.LCD.addItem(os.path.join(root, file))

    # метод, вызывающий окно поиска (проверка на существование окна, создание нового окна, отображение окна)
    def butn_search(self):
        if not self.new_window:
            self.new_window = Research()
            self.new_window.show()
    
    # метод, вызывающий окно создания (проверка на существование окна, создание нового окна, отображение окна)
    def butn_sozdat(self):
        if not self.new_window1:
            self.new_window1 = Sozdanie()
            self.new_window1.show()
    
    # метод, вызывающий окно удаления (проверка на существование окна, создание нового окна, отображение окна)
    def butn_delete(self):
        if not self.new_window2:
            self.new_window2 = Delete()
            self.new_window2.show()

    # метод, вызывающий окно переименования (проверка на существование окна, создание нового окна, отображение окна)
    def butn_rename(self):
        if not self.new_window3:
            self.new_window3 = Rename()
            self.new_window3.show()
    
    # метод, вызывающий окно редактирования (проверка на существование окна, создание нового окна, отображение окна)
    def butn_edit(self):
        if not self.new_window4:
            self.new_window4 = Edit()
            self.new_window4.show()


class Research(QWidget):
    # класс для окна поиска
    def __init__(self):
        # метод инициализации класса
        # вызов метода инициализации родительского класса
        super().__init__()
        
        # установка заголовка окна
        # установка размеров окна
        self.setWindowTitle('Поиск')
        self.setGeometry(400, 415, 400, 415)

        # создание поля ввода (установка размеров поля ввода, установка позиции поля ввода)
        self.LCD1 = QLineEdit(self)
        self.LCD1.resize(300, 20)
        self.LCD1.move(5, 20)

        # создание кнопки "Поиск" (установка размеров кнопки "Поиск", установка позиции кнопки "Поиск", подключение метода к кнопке "Поиск")
        self.btn5 = QPushButton('Поиск', self)
        self.btn5.resize(85, 22)
        self.btn5.move(310, 19)
        self.btn5.clicked.connect(self.update_file_list)
    
    # метод для обновления списка файлов (директория в которой будет выполняться поиск, очистка поля ввода, добавление файла в список)
    def update_file_list(self):
        directory = './folder'
        self.LCD1.clear()
        for root, dirs, files in os.walk(directory):
            for file in files:
                self.LCD1.addItem(os.path.join(root, file))


# класс для окна создания файла
class Sozdanie(QWidget):
    def __init__(self):
        # метод инициализации класса
        # вызов метода инициализации родительского класса
        super().__init__()
        
        # установка заголовка окна
         # установка размеров окна
        self.setWindowTitle('Создать файл')
        self.setGeometry(400, 415, 400, 415)

        # создание поля ввода
        # установка размеров поля ввода
        # установка позиции поля ввода
        self.LCD2 = QLineEdit(self)
        self.LCD2.resize(300, 20)
        self.LCD2.move(5, 20)

        # создание кнопки "Создать" (установка размеров кнопки "Создать", установка позиции кнопки "Создать", подключение метода к кнопке "Создать")
        self.btn5 = QPushButton('Создать', self)
        self.btn5.resize(85, 22)
        self.btn5.move(310, 19)
        self.btn5.clicked.connect(self.texty)

        # создание списка файлов (установка размеров списка файлов, установка позиции списка файлов, вызов метода для обновления списка файлов)
        self.LCD = QListWidget(self)
        self.LCD.resize(390, 350)
        self.LCD.move(5, 60)
        self.serch_search()

    # метод для обновления списка файлов (директория в которой будет выполняться поиск, добавление файла в список)
    def serch_search(self):
        directory = './folder/'
        for root, dirs, files in os.walk(directory):
            for file in files:
                self.LCD.addItem(os.path.join(root, file))

    # метод для создания файла ()
    def texty(self):
        # получение текста из поля ввода
        text = self.LCD2.text()
        # проверка на тип файла и закрытие
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

    # метод для создания .docx файла (формирование пути к файлу, создание документа .docx, сохранение документа по указанному пути)
    def create_docx_file(self, name):
        puti = './folder/' + name
        document = Document()
        document.save(puti)
    
    # метод для создания .xlsx файла (формирование пути к файлу, создание книги .xlsx, сохранение книги по указанному пути)
    def create_xlsx_file(self, name):
        puti = './folder/' + name
        workbook = Workbook()
        workbook.save(puti)
    
    # метод для создания .txt файла (формирование пути к файлу, открытие файла для записи, закрытие файла)
    def create_txt_file(self, name):
        puti = './folder/' + name
        with open(puti, 'w') as file:
            file.close()
    
    # метод для обновления списка файлов (директория в которой будет выполняться поиск, очистка поля ввода, добавление файла в список)
    def update_file_list(self):
        directory = './folder/'
        self.LCD2.clear()
        for root, dirs, files in os.walk(directory):
            for file in files: 
                self.LCD2.addItem(os.path.join(root, file))


# класс для окна создания файла
class Sozdanie(QWidget):
    def __init__(self):
        # метод инициализации класса
        # вызов метода инициализации родительского класса
        super().__init__()
        
        # установка заголовка окна
        # установка размеров окна
        self.setWindowTitle('Создать файл')
        self.setGeometry(400, 415, 400, 415)

        # создание поля ввода
        # установка размеров поля ввода
        # установка позиции поля ввода
        self.LCD2 = QLineEdit(self)
        self.LCD2.resize(300, 20)
        self.LCD2.move(5, 20)
        
        # создание кнопки "Создать" (установка размеров кнопки "Создать", установка позиции кнопки "Создать", подключение метода к кнопке "Создать")
        self.btn5 = QPushButton('Создать', self)
        self.btn5.resize(85, 22)
        self.btn5.move(310, 19)
        self.btn5.clicked.connect(self.texty)

        # создание списка файлов
        # установка размеров списка файлов
        # установка позиции списка файлов
        # вызов метода для обновления списка файлов
        self.LCD = QListWidget(self)
        self.LCD.resize(390, 350)
        self.LCD.move(5, 60)
        self.serch_search()

    # метод для обновления списка файлов директория в которой будет выполняться поиск
    def serch_search(self):
        directory = './folder/'
        for root, dirs, files in os.walk(directory):  # цикл для обхода всех файлов в директории
            for file in files:  # цикл для обхода каждого файла
                self.LCD.addItem(os.path.join(root, file))  # добавление файла в список

    def texty(self):  # метод для создания файла
        text = self.LCD2.text()  # получение текста из поля ввода
        if '.docx' in text:  # проверка на тип файла
            self.close()  # закрытие окна
            return self.create_docx_file(text)  # вызов метода для создания .docx файла
        elif '.xlsx' in text:  # проверка на тип файла
            self.close()  # закрытие окна
            return self.create_xlsx_file(text)  # вызов метода для создания .xlsx файла
        elif '.txt' in text:  # проверка на тип файла
            self.close()  # закрытие окна
            return self.create_txt_file(text)  # вызов метода для создания .txt файла
        elif '.docx' and '.xlsx' and '.txt' not in text:  # проверка на тип файла
            pass

    def create_docx_file(self, name):  # метод для создания .docx файла
        puti = './folder/' + name  # формирование пути к файлу
        document = Document()  # создание документа .docx
        document.save(puti)  # сохранение документа по указанному пути
    
    def create_xlsx_file(self, name):  # метод для создания .xlsx файла
        puti = './folder/' + name  # формирование пути к файлу
        workbook = Workbook()  # создание книги .xlsx
        workbook.save(puti)  # сохранение книги по указанному пути
    
    def create_txt_file(self, name):  # метод для создания .txt файла
        puti = './folder/' + name  # формирование пути к файлу
        with open(puti, 'w') as file:  # открытие файла для записи
            file.close()  # закрытие файла
    
    def update_file_list(self):  # метод для обновления списка файлов
        directory = './folder/'  # директория, в которой будет выполняться поиск
        self.LCD2.clear()  # очистка поля ввода
        for root, dirs, files in os.walk(directory):  # цикл для обхода всех файлов в директории
            for file in files: 
                self.LCD2.addItem(os.path.join(root, file))  # добавление файла в список


# Определение класса Delete, наследующего класс QWidget
class Delete(QWidget):
    # Метод инициализации класса
    def __init__(self):
        # Вызов метода инициализации родительского класса
        super().__init__()
        
        # Установка заголовка окна
        # Установка геометрии окна
        self.setWindowTitle('Удалить файл')
        self.setGeometry(400, 415, 400, 415)

        # Создание виджета списка (Установка размеров виджета, Установка положения виджета, Вызов метода serch_search)
        self.LCD = QListWidget(self)
        self.LCD.resize(390, 380)
        self.LCD.move(5, 30)
        self.serch_search()

        # Создание виджета ввода текста (Установка размеров виджета, Установка положения виджета)
        self.LCD2 = QLineEdit(self)
        self.LCD2.resize(290, 20)
        self.LCD2.move(5, 5)

        # Создание кнопки (Установка размеров кнопки, Установка положения кнопки, Подключение обработчика события к кнопке, Создание вертикального макета, Добавление кнопки в макет)
        self.btn9 = QPushButton('Удалить', self)
        self.btn9.resize(100, 22)
        self.btn9.move(296, 4)
        self.btn9.clicked.connect(self.ydali)
        self.btn9.layout = QVBoxLayout()
        self.btn9.layout.addWidget(self.btn9)
        # Инициализация переменной new_window4
        self.new_window4 = None
    
    # Метод для поиска файлов
    def serch_search(self):
        directory = './folder/'
        # Циклы обхода файлов
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Печать пути к файлу
                # Добавление пути к файлу в список
                self.LCD.addItem(os.path.join(root, file))

    # Метод для удаления файла
    def ydali(self):
        # Получение имени файла из поля ввода
        name = self.LCD2.text()
        # Формирование пути к файлу
        directory = './folder/' + name
        # Отображение диалогового окна с вопросом о подтверждении удаления файла
        reply = QMessageBox.question(None, 'Точно?', 'Вы уверены, что хотите удалить этот файл?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            if os.path.exists(directory):
                # Если файл существует
                os.remove(directory)
                # Вызов метода обновления списка файлов
                self.update_file_list()
            else:
                pass
            # Закрыть окно
            self.close()
        else:
            # Закрыть окно
            self.close()

    # Метод для обновления списка файлов
    def update_file_list(self):
        directory = './folder/'
        # Очистка списка
        self.LCD.clear()
        # Циклы обхода файлов
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Добавление пути к файлу в список
                self.LCD.addItem(os.path.join(root, file))


class Rename(QWidget):
    def __init__(self):
        super().__init__()
        
        # Установка заголовка окна
        # Установка геометрии окна
        self.setWindowTitle('Переименовать файл')
        self.setGeometry(400, 415, 400, 415)

        # Создание экземпляров QLineEdit (Установка размеров, Перемещение)
        self.LCD3 = QLineEdit(self)
        self.LCD3.resize(300, 20)
        self.LCD3.move(5, 5)

        self.LCD4 = QLineEdit(self)
        self.LCD4.resize(300, 20)
        self.LCD4.move(5, 30)
        
        # Создание экземпляра QListWidget (Установка размеров, Перемещение, Вызов метода serch_search)
        self.LCD = QListWidget(self)
        self.LCD.resize(390, 350)
        self.LCD.move(5, 60)
        self.serch_search()

        # Создание кнопки 'Переименовать' (Установка размеров, Перемещение, Подключение обработчика событий нажатия кнопки к методу ren)
        self.btn5 = QPushButton('Переименовать', self)
        self.btn5.resize(85, 22)
        self.btn5.move(310, 19)
        self.btn5.clicked.connect(self.ren)
    
    # Определение метода serch_search ()
    def serch_search(self):
        directory = './folder/'
        # Циклы по файлам
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Добавление элемента в список
                self.LCD.addItem(os.path.join(root, file))
    
    # Определение метода ren (Установка директории, Получение текста из поля ввода LCD3-LCD4, Проверка существования файла, Переименование файла)
    def ren(self):
        directory = './folder/'
        name = self.LCD3.text()
        name1 = self.LCD4.text() 
        if os.path.exists((directory + name)):
            oldname = os.path.join(directory, name)
            newname = os.path.join(directory, name1)
            os.rename(oldname, newname)
        else:
            # Установка геометрии окна
            pass


# Создание класса Edit, наследующегося от QWidget
class Edit(QWidget):
    # Инициализация класса
    def __init__(self):
        super().__init__()
        
        # Установка заголовка окна
        self.setWindowTitle('Редактировать файл')
        # Установка размеров и положения окна
        self.setGeometry(400, 415, 400, 415)

        # Создание виджета для ввода текста
        self.LCD4 = QLineEdit(self)
        self.LCD4.resize(390, 380)
        self.LCD4.move(5, 5)

        # Создание кнопки "Сохранить"
        self.btn5 = QPushButton('Сохранить', self)
        self.btn5.resize(85, 22)
        self.btn5.move(310, 390)


# Запуск приложения
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Search()
    ex.show()
    sys.exit(app.exec_())