import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.label = QLabel()
        canvas = QPixmap(400, 300)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()
    
    def draw_something(self):
        painter = QPainter(self.label.pixmap())
        painter.drawLine(10, 10, 300, 300)
        painter.end()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
