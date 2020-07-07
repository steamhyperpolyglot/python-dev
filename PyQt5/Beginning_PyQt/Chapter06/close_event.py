# close_event.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Event Handling Example')
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            print("Application closed.")
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Example()
    sys.exit(app.exec_())