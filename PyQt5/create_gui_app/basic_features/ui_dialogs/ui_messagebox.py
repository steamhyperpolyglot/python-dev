import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, \
    QMainWindow, QPushButton

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("My App")

		button = QPushButton("Press me for a dialog!")
		button.clicked.connect(self.button_clicked)
		self.setCentralWidget(button)

	def button_clicked(self, s):
		print("click", s)
		dlg = QMessageBox(self)
		dlg.setWindowTitle("I have a question!")
		dlg.setText("This is a simple dialog")
		dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		dlg.setIcon(QMessageBox.Question)
		button = dlg.exec_()

		if button == QMessageBox.Yes:
			print("Yes!")
		else:
			print("No!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
