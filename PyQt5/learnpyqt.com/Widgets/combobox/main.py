from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Only needed for access to command line arguments
import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])
        widget.setEditable(True)

        # The default signal from currentIndexChanged sends the index
        widget.currentIndexChanged.connect(self.index_changed)

        # The same signal can send a text string
        widget.currentIndexChanged[str].connect(self.text_changed)

        self.setCentralWidget(widget)
    

    def index_changed(self, i):
        print(i)
    
    def text_changed(self, s):
        print(s)

# We need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for the app.
# If we know we won't use command line arguments, QApplication([])
# works too.
app = QApplication(sys.argv)

window = MainWindow()
window.show()

# Start the event loop.
app.exec_()