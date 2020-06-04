import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5 import uic

from MainWindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
