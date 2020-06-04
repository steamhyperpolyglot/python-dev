from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Only needed for access to command line arguments
import sys

class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        # layout = QStackedLayout()

        # layout.addWidget(Color('red'))
        # layout.addWidget(Color('green'))
        # layout.addWidget(Color('blue'))
        # layout.addWidget(Color('yellow'))

        # layout.setCurrentIndex(3)

        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        layout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(layout)

        for n, color in enumerate(['red', 'green', 'blue', 'yellow']):
            btn = QPushButton(str(color))
            btn.pressed.connect(lambda n=n: layout.setCurrentIndex(n))
            button_layout.addWidget(btn)
            layout.addWidget(Color(color))

        widget = QWidget()
        widget.setLayout(pagelayout)
        
        self.setCentralWidget(widget)


# We need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for the app.
# If we know we won't use command line arguments, QApplication([])
# works too.
app = QApplication(sys.argv)

window = MainWindow()
window.show()

# Start the event loop.
app.exec_()