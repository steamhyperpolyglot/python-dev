"""

I have combined the code example from learnpyqt.com as well as
from zetcode.com/gui/pyqt5/painting.

"""
import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setGeometry(300, 30, 400, 300)
		self.setWindowTitle('Draw Something Example')
		self.label = QLabel(self)
		self.label.resize(500, 40)
		self.setMouseTracking(True)
		self.pos = None
		self.last_x, self.last_y = None, None

		self.show()
	
	def paintEvent(self, e):
		if self.last_x and self.last_y:
			q = QPainter(self)
			q.drawLine(self.last_x, self.last_y, self.pos.x(), self.pos.y())
			q.end()
			self.update()

	def mouseMoveEvent(self, event):
		if self.last_x is None:
			self.last_x = event.x()
			self.last_y = event.y()
			return

		self.pos = event.pos()

		self.last_x = event.x()
		self.last_y = event.y()

		self.label.setText('Coordinates: (%d, %d)' % (event.x(), event.y()))
	
	def mouseReleaseEvent(self, e):
		self.last_x = None
		self.last_y = None

	def drawSomething(self, qp):
		qp.drawLine(10, 10, 300, 200)

	def drawSquare(self, qp):
		pen = QPen()
		pen.setWidth(40)
		pen.setColor(QColor('red'))
		qp.setPen(pen)
		qp.drawPoint(200, 150)
	
	def drawRandomDots(self, qp):
		from random import randint, choice
		colors = ['#FFD141', '#376F9F', '#0D1F2D', '#E9EBEF', '#EB5160']

		pen = QPen()
		pen.setWidth(3)
		qp.setPen(pen)

		for n in range(10000):
			pen.setColor(QColor(choice(colors)))
			qp.setPen(pen)
			qp.drawPoint(
				200 + randint(-100, 100), 	# x
				150 + randint(-100, 100)	# y
			)
	
	def drawSingleRect(self, qp):
		from random import randint
		pen = QPen()
		pen.setWidth(3)
		pen.setColor(QColor("#EB5160"))
		qp.setPen(pen)
		qp.drawRect(50, 50, 100, 100)
		qp.drawRect(60, 60, 150, 100)
		qp.drawRect(70, 70, 100, 150)
		qp.drawRect(80, 70, 150, 100)
		qp.drawRect(90, 90, 100, 150)

	def drawMultiRects(self, qp):
		from random import randint
		pen = QPen()
		pen.setWidth(3)
		pen.setColor(QColor("#376F9F"))
		qp.setPen(pen)

		brush = QBrush()
		brush.setColor(QColor("#FFD141"))
		brush.setStyle(Qt.Dense1Pattern)
		qp.setBrush(brush)

		qp.drawRects(
			QRect(50, 50, 100, 100),
			QRect(60, 60, 150, 100),
			QRect(70, 70, 100, 150),
			QRect(80, 80, 150, 100),
			QRect(90, 90, 100, 150),
		)
	
	def drawRoundedRects(self, qp):
		from random import randint
		pen = QPen()
		pen.setWidth(3)
		pen.setColor(QColor("#376F9F"))
		qp.setPen(pen)
		qp.drawRoundedRect(40, 40, 100, 100, 10, 10)
		qp.drawRoundedRect(80, 80, 100, 100, 10, 50)
		qp.drawRoundedRect(120, 120, 100, 100, 50, 10)
		qp.drawRoundedRect(160, 160, 100, 100, 50, 50)
	
	def drawEllipse(self, qp):
		from random import randint
		pen = QPen()
		pen.setWidth(3)
		pen.setColor(QColor(204, 0, 0))
		qp.setPen(pen)

		# qp.drawEllipse(10, 10, 100, 100)
		# qp.drawEllipse(10, 10, 150, 200)
		# qp.drawEllipse(10, 10, 200, 300)

		# we can use the QPoint
		qp.drawEllipse(QPoint(100, 100), 10, 10)
		qp.drawEllipse(QPoint(100, 100), 15, 20)
		qp.drawEllipse(QPoint(100, 100), 20, 30)
		qp.drawEllipse(QPoint(100, 100), 25, 40)
		qp.drawEllipse(QPoint(100, 100), 30, 50)
		qp.drawEllipse(QPoint(100, 100), 35, 60)

	def drawText(self, qp):
		from random import randint
		
		pen = QPen()
		pen.setWidth(1)
		pen.setColor(QColor('green'))
		qp.setPen(pen)

		font = QFont()
		font.setFamily("Expressway Rg")
		font.setBold(True)
		font.setPointSize(40)
		qp.setFont(font)

		qp.drawText(100, 100, "Hello, world!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
