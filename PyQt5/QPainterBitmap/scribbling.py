import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setGeometry(300, 30, 400, 300)
        self.setWindowTitle('Scribbling Example')
        self.setMouseTracking(True)

        self.pos = None
        self.last_x, self.last_y = None, None
    
    def paintEvent(self, event):
        if self.last_x and self.last_y:
            painter = QPainter(self)
            painter.drawLine(self.last_x, self.last_y, self.pos.x(), self.pos.y())
            painter.end()
            self.update()
    
    def mouseMoveEvent(self, event):

        self.pos = event.pos()
        
        if self.last_x is None:
            self.last_x = self.pos.x()
            self.last_y = self.pos.x()
            return

        # Update the origin for next time.
        self.last_x = self.pos.x()
        self.last_y = self.pos.x()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
