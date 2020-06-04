"""

ZetCode PyQt5 tutorial

In this example, we draw text in Russian Cylliric.

Author: Jan Bodnar
Website: zetcode.com

"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class Example(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.text = "Лев Николаевич Толстой\nАнна Каренина"
		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('Drawing Text')
		self.show()
    
	def paintEvent(self, event):
		qp = QPainter()
		qp.begin(self)
		self.drawText(event, qp)
		qp.end()
    
	def drawText(self, event, qp):
		qp.setPen(QColor(168, 34, 3))
		qp.setFont(QFont('Daytona', 14))
		qp.drawText(event.rect(), Qt.AlignCenter, self.text)

def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()

