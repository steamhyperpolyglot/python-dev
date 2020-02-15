import datetime as dt


# Define a class named Member for making member objects.
class Member:
	""" Create a member object """
	free_days = 365
	
	""" Create a member from uname and fname """
	
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname
		
		# Default date_joined to today's date
		self.date_joined = dt.date.today()
		# Set an expiration date
		self.expiry_date = dt.date.today() + dt.timedelta(days=Member.free_days)
		# Default secret code is nothing
		self.secret_code = ''
	
	# Method in the base class
	def get_status(self):
		return f"{self.firstname} is a Member"
	
	# Method in the base class
	def showexpiry(self):
		return f"{self.firstname} {self.lastname} expires on {self.expiry_date}"

	
# Subclass for Admins.
class Admin(Member):
	# Admin accounts don't expire for 100 years.
	expiry_days = 365.2422 * 100
	
	# Subclass parameters
	def __init__(self, firstname, lastname, secret_code):
		super().__init__(firstname, lastname)
		# Assigning the remaining parameter to this object
		self.secret_code = secret_code
	
	def get_status(self):
		return f"{self.firstname} is an Admin"


# Subclass for Users.
class User(Member):
	def get_status(self):
		return f"{self.firstname} is a regular User"


# Joe = Member('Joe', 'Anybody')
# print(Joe.firstname)
# print(Joe.lastname)
# print(Joe.expiry_date)

Ann = Admin('Annie', 'Angst', 'PRESTO')
print(Ann.firstname, Ann.lastname, Ann.expiry_date, Ann.secret_code)
print(Ann.get_status())
print()

Uli = User('Uli', 'Ungula')
print(Uli.firstname, Uli.lastname, Uli.expiry_date, Uli.secret_code)
print(Uli.get_status())
print()

Manny = Member('Mindy', 'Membo')
print(Manny.firstname, Manny.lastname, Manny.secret_code)
print(Manny.get_status())
