# checkboxes.py
# Import necessary modules

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class CheckBoxWindow(QWidget):
	
	def __init__(self):
		super().__init__()
		self.initializeUI()
	
	def initializeUI(self):
		"""
		Initialize the window and display its contents to the screen.
		"""
		self.setGeometry(100, 100, 250, 250)
		self.setWindowTitle('QCheckBox Widget')
		self.displayCheckBoxes()
		
		self.show()
	
	def displayCheckBoxes(self):
		"""
		Setup the checkboxes and other widgets
		"""
		header_label = QLabel(self)
		header_label.setText("Which shifts can you work? (Please check all that apply)")
		header_label.setWordWrap(True)
		header_label.move(10, 10)
		header_label.resize(230, 60)
		
		# Set up checkboxes
		morning_cb = QCheckBox("Morning [8AM - 2PM]", self)     # text, parent
		morning_cb.move(20, 80)
		morning_cb.stateChanged.connect(self.printToTerminal)
		
		after_cb = QCheckBox("Afternoon [1PM - 8PM]", self)     # text, parent
		after_cb.move(20, 100)
		after_cb.stateChanged.connect(self.printToTerminal)
		
		night_cb = QCheckBox("Night [7PM - 3AM]", self)     # text, parent
		night_cb.move(20, 120)
		night_cb.stateChanged.connect(self.printToTerminal)
	
	def printToTerminal(self, state):   # pass state of checkbox
		"""
		Simple function to show how to determine the state of the checkbox.
		Prints the text label of the checkbox by determining which widget
		is sending the signal.
		"""
		sender = self.sender()
		if state == Qt.Checked:
			print("{} Selected.".format(sender.text()))
		else:
			print("{} Deselected.".format(sender.text()))


# Run program
if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = CheckBoxWindow()
	sys.exit(app.exec_())
