# button.py
# Import necessary modules

import sys
from PyQt5.QtWidgets import *


class ButtonWindow(QWidget):
	
	def __init__(self):
		super().__init__()      # create default constructor for QWidget
		self.initializeUI()
	
	def initializeUI(self):
		"""
		Initialize the window and display its contents to the screen.
		"""
		self.setGeometry(100, 100, 200, 150)
		self.setWindowTitle('QPushButton Widget')
		self.displayButton()    # call our displayButton function
		
		self.show()
	
	def displayButton(self):
		"""
		Setup the button widget.
		"""
		name_label = QLabel(self)
		name_label.setText("Don't push the button.")
		name_label.move(60, 30)     # arrange label
		
		button = QPushButton('Push Me', self)
		button.clicked.connect(self.buttonClicked)
		button.move(80, 70)     # arrange button
	
	def buttonClicked(self):
		"""
		Print message to the terminal,
		and close the window when button is clicked.
		"""
		print("The window has been closed.")
		self.close()


# Run program
if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = ButtonWindow()
	sys.exit(app.exec_())
