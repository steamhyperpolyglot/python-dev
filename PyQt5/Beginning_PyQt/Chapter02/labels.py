# labels.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import *   # for QApplication, QWidget, QLabel
from PyQt5.QtGui import *       # for QPixmap

class HelloWorldWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle('QLabel Example')
        self.displayLabels()
        
        self.show()
    
    def displayLabels(self):
        """
        Display text and images using QLabels.
        Check to see if image files exist, if not throw an exception.
        """
        text = QLabel(self)
        text.setText("Hello")
        text.move(105, 15)

        image = "Chapter02\images\world.png"
        try:
            with open(image):
                world_image = QLabel(self)
                pixmap = QPixmap(image)
                world_image.setPixmap(pixmap)
                world_image.move(25, 40)
        except FileNotFoundError:
            print("Image not found.")


# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HelloWorldWindow()
    sys.exit(app.exec_())