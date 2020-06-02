"""

ZetCode PyQt5 tutorial

This program draws a Beizer curve with
QPainterPath.

Author: Jan Bodnar
Website: zetcode.com

"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Example(QWidget):

	def __init__(self):
		super().__init__()

		self.initUI()
	
	def initUI(self):
		self.setGeometry(300, 30, 380, 250)
		self.setWindowTitle('Bézier curve')
		self.show()

	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		qp.setRenderHint(QPainter.Antialiasing)
		self.drawBeizerCurve(qp)
		qp.end()
	
	def drawBeizerCurve(self, qp):
		path = QPainterPath()
		path.moveTo(30, 30)
		path.cubicTo(30, 30, 200, 350, 350, 30)

		qp.drawPath(path)


def main():

	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
