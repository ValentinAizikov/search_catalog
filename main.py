
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel


class Search(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(500, 500, 500, 500)


# directory = './folder'
# for root, dirs, files in os.walk(directory):
#    for file in files:
#        # Печать пути к файлу
#        print(os.path.join(root, file))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Search()
    ex.show()
    sys.exit(app.exec_())

