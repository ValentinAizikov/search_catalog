import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtWidgets import QLCDNumber, QLabel, QVBoxLayout, QListWidget, QLineEdit
from docx import Document
from openpyxl import Workbook


class Search(QWidget):  # создаем класс Search
    def __init__(self):  # создаем метод init
        super().__init__()  # вызываем конструктор родительского класса
        self.initUI()  # вызываем метод initUI
    
    def initUI(self):  # создаем метод initUI
        self.setGeometry(490, 415, 490, 415)  # устанавливаем размеры окна
        self.setWindowTitle('Менеджер файлов')  # устанавливаем название окна

        self.btn = QPushButton('Поиск', self)  # создаем кнопку "Поиск"
        self.btn.resize(95, 50)  # устанавливаем размеры кнопки
        self.btn.move(5, 5)  # устанавливаем положение кнопки
        self.btn.clicked.connect(self.butn_search)  # подключаем обработчик события для кнопки "Поиск"
        self.btn.layout = QVBoxLayout()  # создаем вертикальный контейнер
        self.btn.layout.addWidget(self.btn)  # добавляем кнопку в контейнер
        self.new_window = None  # создаем переменную new_window и присваиваем ей значение None

        self.btn1 = QPushButton('Создать', self)  # создаем кнопку "Создать"
        self.btn1.resize(95, 50)  # устанавливаем размеры кнопки
        self.btn1.move(100, 5)  # устанавливаем положение кнопки
        self.btn1.clicked.connect(self.butn_sozdat)  # подключаем обработчик события для кнопки "Создать"
        self.btn1.layout = QVBoxLayout()  # создаем вертикальный контейнер
        self.btn1.layout.addWidget(self.btn1)  # добавляем кнопку в контейнер
        self.new_window1 = None  # создаем переменную new_window1 и присваиваем ей значение None

        self.btn2 = QPushButton('Удалить', self)  # создаем кнопку "Удалить"
        self.btn2.resize(95, 50)  # устанавливаем размеры кнопки
        self.btn2.move(195, 5)  # устанавливаем положение кнопки
        self.btn2.clicked.connect(self.butn_delete)  # подключаем обработчик события для кнопки "Удалить"
        self.btn2.layout = QVBoxLayout()  # создаем вертикальный контейнер
        self.btn2.layout.addWidget(self.btn2)  # добавляем кнопку в контейнер
        self.new_window2 = None  # создаем переменную new_window2 и присваиваем ей значение None

        self.btn3 = QPushButton('Переименовать', self)  # создаем кнопку "Переименовать"
        self.btn3.resize(95, 50)  # устанавливаем размеры кнопки
        self.btn3.move(290, 5)  # устанавливаем положение кнопки
        self.btn3.clicked.connect(self.butn_rename)  # подключаем обработчик события для кнопки "Переименовать"
        self.btn3.layout = QVBoxLayout()  # создаем вертикальный контейнер
        self.btn3.layout.addWidget(self.btn3)  # добавляем кнопку в контейнер
        self.new_window3 = None  # создаем переменную new_window3 и присваиваем ей значение None

        self.btn4 = QPushButton('Редактировать', self)  # создаем кнопку "Редактировать содержимое"
        self.btn4.resize(100, 50)  # устанавливаем размеры кнопки
        self.btn4.move(385, 5)  # устанавливаем положение кнопки
        self.btn4.clicked.connect(self.butn_edit)  # подключаем обработчик события для кнопки "Редактировать содержимое"
        self.btn4.layout = QVBoxLayout()  # создаем вертикальный контейнер
        self.btn4.layout.addWidget(self.btn4)  # добавляем кнопку в контейнер
        self.new_window4 = None  # создаем переменную new_window4 и присваиваем ей значение None

        self.LCD = QListWidget(self)  # создаем список LCD
        self.LCD.resize(479, 350)  # устанавливаем размеры списка
        self.LCD.move(5, 60)  # устанавливаем положение списка
        self.serch_search()  # вызываем метод serch_search

    def serch_search(self): # метод, выполняющий поиск
        directory = './folder' # директория, в которой будет выполняться поиск
        for root, dirs, files in os.walk(directory): # цикл для обхода всех файлов в директории
            for file in files: # цикл для обхода каждого файла
                self.LCD.addItem(os.path.join(root, file)) # добавление файла в список

    def butn_search(self): # метод, вызывающий окно поиска
        if not self.new_window: # проверка на существование окна
            self.new_window = Research() # создание нового окна
            self.new_window.show() # отображение окна
    
    def butn_sozdat(self): # метод, вызывающий окно создания
        if not self.new_window1: # проверка на существование окна
            self.new_window1 = Sozdanie() # создание нового окна
            self.new_window1.show() # отображение окна
    
    def butn_delete(self): # метод, вызывающий окно удаления
        if not self.new_window2: # проверка на существование окна
            self.new_window2 = Delete() # создание нового окна
            self.new_window2.show() # отображение окна

    def butn_rename(self): # метод, вызывающий окно переименования
        if not self.new_window3: # проверка на существование окна
            self.new_window3 = Rename() # создание нового окна
            self.new_window3.show() # отображение окна
    
    def butn_edit(self): # метод, вызывающий окно редактирования
        if not self.new_window4: # проверка на существование окна
            self.new_window4 = Edit() # создание нового окна
            self.new_window4.show() # отображение окна


class Research(QWidget): # класс для окна поиска
    def __init__(self): # метод инициализации класса
        super().__init__() # вызов метода инициализации родительского класса
        
        self.setWindowTitle('Поиск') # установка заголовка окна
        self.setGeometry(400, 415, 400, 415) # установка размеров окна

        self.LCD1 = QLineEdit(self) # создание поля ввода
        self.LCD1.resize(300, 20) # установка размеров поля ввода
        self.LCD1.move(5, 20) # установка позиции поля ввода

        self.btn5 = QPushButton('Поиск', self) # создание кнопки "Поиск"
        self.btn5.resize(85, 22) # установка размеров кнопки "Поиск"
        self.btn5.move(310, 19) # установка позиции кнопки "Поиск"
        self.btn5.clicked.connect(self.update_file_list) # подключение метода к кнопке "Поиск"
    
    def update_file_list(self): # метод для обновления списка файлов
        directory = './folder' # директория, в которой будет выполняться поиск
        self.LCD1.clear() # очистка поля ввода
        for root, dirs, files in os.walk(directory): # цикл для обхода всех файлов в директории
            for file in files: # цикл для обхода каждого файла
                self.LCD1.addItem(os.path.join(root, file)) # добавление файла в список


class Sozdanie(QWidget): # класс для окна создания файла
    def __init__(self): # метод инициализации класса
        super().__init__() # вызов метода инициализации родительского класса
        
        self.setWindowTitle('Создать файл') # установка заголовка окна
        self.setGeometry(400, 415, 400, 415) # установка размеров окна

        self.LCD2 = QLineEdit(self) # создание поля ввода
        self.LCD2.resize(300, 20) # установка размеров поля ввода
        self.LCD2.move(5, 20) # установка позиции поля ввода

        self.btn5 = QPushButton('Создать', self) # создание кнопки "Создать"
        self.btn5.resize(85, 22) # установка размеров кнопки "Создать"
        self.btn5.move(310, 19) # установка позиции кнопки "Создать"
        self.btn5.clicked.connect(self.texty) # подключение метода к кнопке "Создать"

        self.LCD = QListWidget(self) # создание списка файлов
        self.LCD.resize(390, 350) # установка размеров списка файлов
        self.LCD.move(5, 60) # установка позиции списка файлов
        self.serch_search() # вызов метода для обновления списка файлов

    def serch_search(self): # метод для обновления списка файлов
        directory = './folder' # директория, в которой будет выполняться поиск
        for root, dirs, files in os.walk(directory): # цикл для обхода всех файлов в директории
            for file in files: # цикл для обхода каждого файла
                self.LCD.addItem(os.path.join(root, file)) # добавление файла в список

    def texty(self): # метод для создания файла
        text = self.LCD2.text() # получение текста из поля ввода
        if '.docx' in text: # проверка на тип файла
            self.close() # закрытие окна
            return self.create_docx_file(text) # вызов метода для создания .docx файла
        elif '.xlsx' in text: # проверка на тип файла
            self.close() # закрытие окна
            return self.create_xlsx_file(text) # вызов метода для создания .xlsx файла
        elif '.txt' in text: # проверка на тип файла
            self.close() # закрытие окна
            return self.create_txt_file(text) # вызов метода для создания .txt файла
        elif '.docx' and '.xlsx' and '.txt' not in text: # проверка на тип файла
            pass

    def create_docx_file(self, name): # метод для создания .docx файла
        puti = './folder/' + name # формирование пути к файлу
        document = Document() # создание документа .docx
        document.save(puti) # сохранение документа по указанному пути
    
    def create_xlsx_file(self, name): # метод для создания .xlsx файла
        puti = './folder/' + name # формирование пути к файлу
        workbook = Workbook() # создание книги .xlsx
        workbook.save(puti) # сохранение книги по указанному пути
    
    def create_txt_file(self, name): # метод для создания .txt файла
        puti = './folder/' + name # формирование пути к файлу
        with open(puti, 'w') as file: # открытие файла для записи
            file.close() # закрытие файла
    
    def update_file_list(self): # метод для обновления списка файлов
        directory = './folder' # директория, в которой будет выполняться поиск
        self.LCD2.clear() # очистка поля ввода
        for root, dirs, files in os.walk(directory): # цикл для обхода всех файлов в директории
            for file in files: 
                self.LCD2.addItem(os.path.join(root, file))  # добавление файла в список


class Sozdanie(QWidget):  # класс для окна создания файла
    def __init__(self):  # метод инициализации класса
        super().__init__()  # вызов метода инициализации родительского класса
        
        self.setWindowTitle('Создать файл')  # установка заголовка окна
        self.setGeometry(400, 415, 400, 415)  # установка размеров окна

        self.LCD2 = QLineEdit(self)  # создание поля ввода
        self.LCD2.resize(300, 20)  # установка размеров поля ввода
        self.LCD2.move(5, 20)  # установка позиции поля ввода

        self.btn5 = QPushButton('Создать', self)  # создание кнопки "Создать"
        self.btn5.resize(85, 22)  # установка размеров кнопки "Создать"
        self.btn5.move(310, 19)  # установка позиции кнопки "Создать"
        self.btn5.clicked.connect(self.texty)  # подключение метода к кнопке "Создать"

        self.LCD = QListWidget(self)  # создание списка файлов
        self.LCD.resize(390, 350)  # установка размеров списка файлов
        self.LCD.move(5, 60)  # установка позиции списка файлов
        self.serch_search()  # вызов метода для обновления списка файлов

    def serch_search(self):  # метод для обновления списка файлов
        directory = './folder'  # директория, в которой будет выполняться поиск
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
        directory = './folder'  # директория, в которой будет выполняться поиск
        self.LCD2.clear()  # очистка поля ввода
        for root, dirs, files in os.walk(directory):  # цикл для обхода всех файлов в директории
            for file in files: 
                self.LCD2.addItem(os.path.join(root, file))  # добавление файла в список


# Определение класса Delete, наследующего класс QWidget
class Delete(QWidget):
    # Метод инициализации класса
    def __init__(self):
        super().__init__()  # Вызов метода инициализации родительского класса
        
        self.setWindowTitle('Удалить файл')  # Установка заголовка окна
        self.setGeometry(400, 415, 400, 415)  # Установка геометрии окна

        self.LCD = QListWidget(self)  # Создание виджета списка
        self.LCD.resize(390, 380)  # Установка размеров виджета
        self.LCD.move(5, 30)  # Установка положения виджета
        self.serch_search()  # Вызов метода serch_search

        self.LCD2 = QLineEdit(self)  # Создание виджета ввода текста
        self.LCD2.resize(290, 20)  # Установка размеров виджета
        self.LCD2.move(5, 5)  # Установка положения виджета

        self.btn9 = QPushButton('Удалить', self)  # Создание кнопки
        self.btn9.resize(100, 22)  # Установка размеров кнопки
        self.btn9.move(296, 4)  # Установка положения кнопки
        self.btn9.clicked.connect(self.ydali)  # Подключение обработчика события к кнопке
        self.btn9.layout = QVBoxLayout()  # Создание вертикального макета
        self.btn9.layout.addWidget(self.btn9)  # Добавление кнопки в макет
        self.new_window4 = None  # Инициализация переменной new_window4
    
    # Метод для поиска файлов
    def serch_search(self):
        directory = './folder'  # Установка директории
        for root, dirs, files in os.walk(directory):  # Цикл обхода файловой структуры
            for file in files:  # Цикл обхода файлов
                # Печать пути к файлу
                self.LCD.addItem(os.path.join(root, file))  # Добавление пути к файлу в список

    # Метод для удаления файла
    def ydali(self):
        name = self.LCD2.text()  # Получение имени файла из поля ввода
        directory = './folder/' + name  # Формирование пути к файлу
        reply = QMessageBox.question(None, 'Точно?', 'Вы уверены, что хотите удалить этот файл?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  # Отображение диалогового окна с вопросом о подтверждении удаления файла
        if reply == QMessageBox.Yes:  # Если получен положительный ответ
            if os.path.exists(directory):  # Если файл существует
                os.remove(directory)  # Удаление файла
                self.update_file_list()  # Вызов метода обновления списка файлов
            else:
                pass  # Ничего не делать
            self.close()  # Закрыть окно
        else:
            self.close()  # Закрыть окно

    # Метод для обновления списка файлов
    def update_file_list(self):
        directory = './folder'  # Установка директории
        self.LCD.clear()  # Очистка списка
        for root, dirs, files in os.walk(directory):  # Цикл обхода файловой структуры
            for file in files:  # Цикл обхода файлов
                # Печать пути к файлу
                self.LCD.addItem(os.path.join(root, file))  # Добавление пути к файлу в список


class Rename(QWidget):
    def __init__(self):  # Определение метода init
        super().__init__()  # Вызов метода init родительского класса
        
        self.setWindowTitle('Переименовать файл')  # Установка заголовка окна
        self.setGeometry(400, 415, 400, 415)  # Установка геометрии окна

        self.LCD3 = QLineEdit(self)  # Создание экземпляра QLineEdit
        self.LCD3.resize(300, 20)  # Установка размеров
        self.LCD3.move(5, 5)  # Перемещение

        self.LCD4 = QLineEdit(self)  # Создание экземпляра QLineEdit
        self.LCD4.resize(300, 20)  # Установка размеров
        self.LCD4.move(5, 30)  # Перемещение

        self.LCD = QListWidget(self)  # Создание экземпляра QListWidget
        self.LCD.resize(390, 350)  # Установка размеров
        self.LCD.move(5, 60)  # Перемещение
        self.serch_search()  # Вызов метода serch_search

        self.btn5 = QPushButton('Переименовать', self)  # Создание кнопки 'Переименовать'
        self.btn5.resize(85, 22)  # Установка размеров
        self.btn5.move(310, 19)  # Перемещение
        self.btn5.clicked.connect(self.ren)  # Подключение обработчика событий нажатия кнопки к методу ren
    
    def serch_search(self):  # Определение метода serch_search
        directory = './folder'  # Установка директории
        for root, dirs, files in os.walk(directory):  # Цикл по файлам в директории
            for file in files:  # Цикл по файлам
                # Печать пути к файлу
                self.LCD.addItem(os.path.join(root, file))  # Добавление элемента в список
    
    def ren(self):  # Определение метода ren
        directory = './folder/'  # Установка директории
        name = self.LCD3.text()  # Получение текста из поля ввода LCD3
        name1 = self.LCD4.text()  # Получение текста из поля ввода LCD4
        if os.path.exists((directory + name)):  # Проверка существования файла
            oldname = os.path.join(directory, name)  # Старое имя файла
            newname = os.path.join(directory, name1)  # Новое имя файла
            os.rename(oldname, newname)  # Переименование файла
        else:
            pass  # Пропуск выполнения кода


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