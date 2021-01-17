import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton
from ui_customdialog import CustomDialog

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("My App")

		button = QPushButton("Press me for a dialog!")
		button.clicked.connect(self.button_clicked)
		self.setCentralWidget(button)

	def button_clicked(self, s):
		print("click", s)

		dlg = CustomDialog(self)
		if dlg.exec_():
			print("Success!")
		else:
			print("Canceled!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
