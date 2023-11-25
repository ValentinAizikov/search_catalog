import json
import sys
from PyQt5.QtWidgets import QComboBox, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QTextEdit
from docx import Document
from openpyxl import Workbook
import os


def create_txt_file(file_path):
    with open(file_path, 'w') as file:
        file.write("Пример текста в файле .txt")

def create_docx_file(file_path):
    document = Document()
    document.add_paragraph("Пример текста в файле .docx")
    document.save(file_path)

def create_xlsx_file(file_path):
    workbook = Workbook()
    sheet = workbook.active
    sheet['A1'] = "Пример текста в файле .xlsx"
    workbook.save(file_path)

file_types = {
    'txt': create_txt_file,
    'docx': create_docx_file,
    'xlsx': create_xlsx_file
}

class CollectionInterface(QWidget):
    def __init__(self, collection):
        super().__init__()
        self.collection = collection
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Collection Interface')
        self.setGeometry(100, 100, 400, 300)

        self.search_input = QLineEdit()
        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.search_results)

        self.results_display = QTextEdit()

        self.element_id_input = QLineEdit()
        self.view_details_button = QPushButton('View Details')
        self.view_details_button.clicked.connect(self.view_element_details)

        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.search_input)
        hbox1.addWidget(self.search_button)
        vbox.addLayout(hbox1)
        vbox.addWidget(self.results_display)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(QLabel('Element ID:'))
        hbox2.addWidget(self.element_id_input)
        hbox2.addWidget(self.view_details_button)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

        layout = QVBoxLayout()

        label = QLabel("Выберите тип файла:")
        layout.addWidget(label)

        file_type_combo = QComboBox()
        file_type_combo.addItems(file_types.keys())
        layout.addWidget(file_type_combo)

        create_button = QPushButton("Создать файл")
        create_button.clicked.connect(lambda: self.create_file(file_type_combo.currentText()))
        layout.addWidget(create_button)

        self.setLayout(layout)
        self.setWindowTitle("File Creation Widget")

    def create_file(self, file_type):
        file_path = "example." + file_type
        file_types[file_type](file_path)

    def search_results(self):
        search_term = self.search_input.text()
        sorted_results = self.collection.search(search_term)
        self.display_results(sorted_results)

    def display_results(self, results):
        self.results_display.clear()
        for result in results:
            self.results_display.append(str(result))

    def view_element_details(self):
        element_id = self.element_id_input.text()
        self.collection.view_element_details(element_id)


class Collection:
    def load_from_file(self, file_path):
        # Загрузка коллекции элементов из файла
        with open(file_path, 'r') as file:
            # Чтение данных из файла и добавление элементов в коллекцию
            # Например, если данные в файле представлены в формате JSON
            data = json.load(file)
            self.elements = data['elements']
    
    def load_from_database(self, db_connection):
        # Загрузка коллекции элементов из базы данных
        # Например, если используется SQLite
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM elements")
        rows = cursor.fetchall()
        for row in rows:
            # Добавление элементов в коллекцию
            self.elements.append(row)

    def search(self, keywords):
        # Поиск по ключевым словам или фразам в названиях и описаниях элементов коллекции
        results = []
        for element in self.elements:
            if any(keyword in element['name'] or keyword in element['description'] for keyword in keywords):
                results.append(element)
        return results

    def filter(self, category):
        # Фильтрация результатов поиска по определенным категориям или атрибутам элементов
        filtered_results = [element for element in self.elements if element['category'] == category]
        return filtered_results

    def save_results(self, results, file_path):
        # Сохранение результатов поиска в файл
        with open(file_path, 'w') as file:
            # Запись результатов в файл, например, в формате JSON
            data = {'results': results}
            json.dump(data, file)
    
    def input_search_keywords(self):
        # Ввод ключевых слов или фраз для поиска
        keywords_input = input("Введите ключевые слова или фразы для поиска (через запятую): ")
        keywords = [keyword.strip() for keyword in keywords_input.split(',')]
        return keywords
    
    def search(self, keywords):
        # Поиск по названиям и описаниям элементов коллекции с использованием введенных ключевых слов или фраз
        results = []
        try:
            for element in self.elements:
                for keyword in keywords:
                    if keyword.lower() in element['name'].lower() or keyword.lower() in element['description'].lower():
                        results.append(element)
                        break  # Если хотя бы одно ключевое слово найдено, переходим к следующему элементу
        except AttributeError:
            return self.setText('Ничего не найдено')
    
    def display_results(self, results):
        # Отображение результатов поиска путем вывода списка элементов, соответствующих критериям поиска
        if results:
            print("Результаты поиска:")
            for index, element in enumerate(results, start=1):
                print(f"{index}. Название: {element['name']}, Описание: {element['description']}")
        else:
            print("По вашему запросу ничего не найдено.")

    def filter_results(self, results, filter_criteria):
        # Фильтрация результатов по определенным категориям или атрибутам элементов
        filtered_results = [element for element in results if element['category'] == filter_criteria]
        return filtered_results
    
    def save_results(self, results, file_name):
        # Сохранение результатов поиска в файл
        with open(file_name, 'w') as file:
            json.dump(results, file)

    def save_element(self, element, file_name):
        # Сохранение отдельного элемента коллекции в файл
        with open(file_name, 'w') as file:
            json.dump(element, file)

    def view_element_details(self, element_id):
        # Просмотр детальной информации об элементе коллекции по его идентификатору
        element = self.get_element_by_id(element_id)
        if element:
            print(element)
        else:
            print("Element not found")


directory = './folder'
for root, dirs, files in os.walk(directory):
    for file in files:
        # Печать пути к файлу
        print(os.path.join(root, file))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    collection = Collection()  # Создание экземпляра класса Collection
    ex = CollectionInterface(collection)
    ex.show()
    sys.exit(app.exec_())