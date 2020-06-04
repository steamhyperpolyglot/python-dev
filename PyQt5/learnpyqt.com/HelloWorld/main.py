import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, \
	QToolBar, QAction, QStatusBar, QCheckBox
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
	
	def contextMenuEvent(self, event):
		print("Context menu event!")
		super(MainWindow, self).contextMenuEvent(event)
	
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		
		self.setWindowTitle("My Awesome App")
		
		label = QLabel("This is a PyQt5 window!")
		
		label.setAlignment(Qt.AlignCenter)
		
		self.setCentralWidget(label)
		
		toolbar = QToolBar("My Main Toolbar")
		self.addToolBar(toolbar)
		
		button_action = QAction(QIcon("bug.png"), "Your button", self)
		button_action.setStatusTip("This is your button")
		button_action.triggered.connect(self.onMyToolBarButtonClick)
		button_action.setCheckable(True)
		toolbar.addAction(button_action)

		toolbar.addSeparator()

		button_action2 = QAction(QIcon("bug.png"), "Your button 2", self)
		button_action2.setStatusTip("This is your button2")
		button_action2.triggered.connect(self.onMyToolBarButtonClick)
		button_action2.setCheckable(True)
		toolbar.addAction(button_action2)

		toolbar.addWidget(QLabel("Hello"))
		toolbar.addWidget(QCheckBox())

		self.setStatusBar(QStatusBar(self))
	
	def onMyToolBarButtonClick( self, s ):
		print("click", s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()