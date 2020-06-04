from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Only needed for access to command line arguments
import sys

# Subclass QMainWindow to customise your application's main window.
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        layout = QVBoxLayout()
        """ widgets = [QCheckBox, 
            QComboBox,
            QDateEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit
        ]

        for w in widgets:
            layout.addWidget(w()) """

        label1 = QLabel()
        # font = label1.font()
        # font.setPointSize(30)
        # label1.setFont(font)
        # label1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        label1.setPixmap(QPixmap('jungle.jpg'))
        label1.setScaledContents(True)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(label1)


# We need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for the app.
# If we know we won't use command line arguments, QApplication([])
# works too.
app = QApplication(sys.argv)

window = MainWindow()
window.show()

# Start the event loop.
app.exec_()
