import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.button_is_checked = True
        
        self.setWindowTitle("My App")
        
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        # button.clicked.connect(self.the_button_was_clicked)
        # button.clicked.connect(self.the_button_was_toggled)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)
        
        self.setFixedSize(QSize(300, 180))
        
        # Set the central widget of the Window
        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        # isChecked() returns the check state of the button.
        self.button_is_checked = self.button.isChecked()

        print(self.button_is_checked)
    
    def the_button_was_clicked(self):
        print("Clicked!")
    
    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        
        print(self.button_is_checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
