# color_event.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class SendSignal(QObject):
    """
    Define a signal change_style that takes no arguments.
    """
    change_style = pyqtSignal()


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Create Custom Signals')

        self.setupLabel()

        self.show()

    def setupLabel(self):
        """
        Create label and connect custom signal to slot.
        """
        self.index = 0  # index of items in list
        self.direction = ""

        self.colors_list = ["red", "orange", "yellow", "green", "blue", "purple"]

        self.label = QLabel()
        self.label.setStyleSheet("background-color: {}".format(self.colors_list[self.index]))
        self.setCentralWidget(self.label)

        # create instance of SendSignal class, and
        # connect change_style signal to a slot.
        self.sig = SendSignal()
        self.sig.change_style.connect(self.changeBackground)
    
    def keyPressEvent(self, event):
        """
        Reimplement how the key press event in handled.
        """
        if event.key() == Qt.Key_Up:
            self.direction = "up"
            self.sig.change_style.emit()
        elif event.key() == Qt.Key_Down:
            self.direction = "down"
            self.sig.change_style.emit()
    
    def changeBackground(self):
        """
        Change the background of the label widget when a keyPressEvent
        signal is emitted.
        """
        if self.direction == "up" and self.index < len(self.colors_list) - 1:
            self.index = self.index + 1
            self.label.setStyleSheet("background-color: {}".format(self.colors_list[self.index]))
        elif self.direction == "down" and self.index > 0:
            self.index = self.index - 1
            self.label.setStyleSheet("background-color: {}".format(self.colors_list[self.index]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Example()
    sys.exit(app.exec_())