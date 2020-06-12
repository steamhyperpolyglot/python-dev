# menu_framework.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import *

class BasicMenu(QMainWindow):
	
	def __init__(self):
		super().__init__()
		
		self.initializeUI()
	
	def initializeUI(self):
		"""
		Initialize the window and display its contents to the screen
		"""
		self.setGeometry(100, 100, 350, 350)
		self.setWindowTitle('Basic Menu Example')
		self.createMenu()
		
		self.show()
	
	def createMenu(self):
		"""
		Create skeleton application with a menubar
		"""
		# Create actions for file menu
		exit_act = QAction('Exit', self)
		exit_act.setShortcut('Ctrl+Q')
		exit_act.triggered.connect(self.close)
		
		# Create menubar
		menu_bar = self.menuBar()
		menu_bar.setNativeMenuBar(False)
		
		# Create file menu and add actions
		file_menu = menu_bar.addMenu('File')
		file_menu.addAction(exit_act)

	
# Run program
if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = BasicMenu()
	sys.exit(app.exec_())
