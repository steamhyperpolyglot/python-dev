from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from pyqtgraph import plot
from pyqtgraph.widgets import PlotWidget
import pyqtgraph as pg
import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Load the UI page
        uic.loadUi('mainwindow.ui', self)

        self.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], \
            [30, 32, 34, 32, 33, 31, 29, 32, 35, 45])
    
    def plot(self, hour, temperature):
        self.graphWidget.plot(hour, temperature)

def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()