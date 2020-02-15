import datetime as dt

# Define a class named Member for making member objects.
class Member:
	""" Create a member object """
	free_days = 90
	
	""" Create a member from uname and fname """
	def __init__(self, uname, fname):
		self.username = uname
		self.fullname = fname
		
		# Default date_joined to today's date
		self.date_joined = dt.date.today()
		# Set an expiration date
		self.free_expires = dt.date.today() + dt.timedelta(days=Member.free_days)
		# Set is active to True initially
		self.is_active = True
	
	# Define methods as functions, use self for "this" object
	def show_datejoined(self):
		return f"{self.fullname} joined on {self.date_joined:%d/%m/%y}"
	
	# Method to activate (True) or deactivate (False) account.
	def activate( self, yesno ):
		""" True for active, False to make inactive """
		self.is_active = yesno
	
	@classmethod
	def setfreedays(cls, days):
		cls.free_days = days
	
	@staticmethod
	def currenttime():
		now = dt.datetime.now()
		return f"{now:%I:%M %p}"


Member.setfreedays(30)
new_guy = Member('Rambo', 'Rocco Moe')

print(new_guy.is_active)

new_guy.activate(False)

print(new_guy.is_active)

print(new_guy.free_expires)

print(Member.currenttime())
