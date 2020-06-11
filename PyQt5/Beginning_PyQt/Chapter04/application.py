# application.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class GetApptForm(QWidget):
	
	def __init__(self):
		super().__init__()
		
		self.initializeUI()
	
	def initializeUI(self):
		"""
		Initialize the window and display its contents to
		the screen.
		"""
		self.setGeometry(100, 100, 300, 400)
		self.setWindowTitle('4.3 - Application Form GUI')
		self.formWidgets()
		
		self.show()
	
	def formWidgets(self):
		"""
		Create widgets that will be used in the application form.
		"""
		# Create widgets
		title = QLabel("Appointment Submission Form")
		title.setFont(QFont('Roboto', 18))
		title.setAlignment(Qt.AlignCenter)
		
		name = QLineEdit()
		name.resize(100, 100)
		address = QLineEdit()
		mobile_num = QLineEdit()
		mobile_num.setInputMask("0000 0000")
		
		age_label = QLabel("Age")
		age = QSpinBox()
		age.setRange(1, 110)
		
		height_label = QLabel("Height")
		height = QLineEdit()
		height.setPlaceholderText("cm")
		
		weight_label = QLabel("Weight")
		weight = QLineEdit()
		weight.setPlaceholderText("kg")
		
		gender = QComboBox()
		gender.addItems(["Male", "Female"])
		
		surgery = QTextEdit()
		surgery.setPlaceholderText("separate by ','")
		blood_type = QComboBox()
		blood_type.addItems(["A", "B", "AB", "O"])
		
		hours = QSpinBox()
		hours.setRange(1, 12)
		minutes = QComboBox()
		minutes.addItems([":00", ":15", ":30", ":45"])
		am_pm = QComboBox()
		am_pm.addItems(["AM", "PM"])
		
		submit_button = QPushButton("Submit Appointment")
		submit_button.clicked.connect(self.close)
		
		# Create horizontal layout and add age, height,
		# and weight to h_box
		h_box = QHBoxLayout()
		h_box.addSpacing(10)
		h_box.addWidget(age_label)
		h_box.addWidget(age)
		h_box.addWidget(height_label)
		h_box.addWidget(height)
		h_box.addWidget(weight_label)
		h_box.addWidget(weight)
		
		# Create horizontal layout and add time information
		desired_time_h_box = QHBoxLayout()
		desired_time_h_box.addSpacing(10)
		desired_time_h_box.addWidget(hours)
		desired_time_h_box.addWidget(minutes)
		desired_time_h_box.addWidget(am_pm)
		
		# Create form layout
		app_form_layout = QFormLayout()
		
		# Add all widgets to form layout
		app_form_layout.addRow(title)
		app_form_layout.addRow("Full Name", name)
		app_form_layout.addRow("Address", address)
		app_form_layout.addRow("Mobile Number", mobile_num)
		app_form_layout.addRow(h_box)
		app_form_layout.addRow("Gender", gender)
		app_form_layout.addRow("Past Surgeries ", surgery)
		app_form_layout.addRow("Blood Type", blood_type)
		app_form_layout.addRow("Desired Time", desired_time_h_box)
		app_form_layout.addRow(submit_button)
		
		self.setLayout(app_form_layout)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = GetApptForm()
	sys.exit(app.exec_())
