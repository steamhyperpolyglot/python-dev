# user_profile.py
# Import necessary modules
import sys, os.path
from PyQt5.QtWidgets import *   # for QApplication, QLabel, QWidget
from PyQt5.QtGui import *       # QFont and QPixmap

class UserProfile(QWidget):

    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setGeometry(50, 50, 250, 420)
        self.setWindowTitle("2.1 - User Profile GUI")
        self.displayImages()
        self.displayUserInfo()

        self.show()
    
    def displayImages(self):
        """
        Display background and profile images.
        Check to see if images files exist, if not throw an exception.
        """
        background_image = "Chapter02\images\skyblue.png"
        profile_image = "Chapter02\images\profile_image.png"

        try:
            with open(background_image):
                background = QLabel(self)
                pixmap = QPixmap(background_image)
                background.setPixmap(pixmap)
        except FileNotFoundError:
            print("Image not found.")
        
        try:
            with open(profile_image):
                user_image = QLabel(self)
                pixmap = QPixmap(profile_image)
                user_image.setPixmap(pixmap)
                user_image.move(80, 20)
        except FileNotFoundError:
            print("Image not found.")
    
    def displayUserInfo(self):
        """
        Create the labels to be displayed for the User Profile.
        """
        user_name = QLabel(self)
        user_name.setText("John Doe")
        user_name.move(85, 140)
        user_name.setFont(QFont('SF Pro Display', 16))

        bio_title = QLabel(self)
        bio_title.setText("Biography")
        bio_title.move(15, 170)
        bio_title.setFont(QFont('SF Pro Display', 15))

        about = QLabel(self)
        about.setText("I'm a Software Engineer with 8 years" \
            " experience creating awesome code.")
        about.setWordWrap(True)
        about.move(15, 200)

        skills_title = QLabel(self)
        skills_title.setText("Skills")
        skills_title.move(15, 240)
        skills_title.setFont(QFont('SF Pro Display', 15))

        skills = QLabel(self)
        skills.setText("Python  |  PHP  |  SQL  |  JavaScript")
        skills.move(15, 265)
        skills.setFont(QFont('SF Pro Display', 10))

        experience_title = QLabel(self)
        experience_title.setText("Experience")
        experience_title.move(15, 290)
        experience_title.setFont(QFont('SF Pro Display', 15))

        experience = QLabel(self)
        experience.setText("Python Developer")
        experience.move(15, 315)
        experience.setFont(QFont('SF Pro Display', 10))

        dates = QLabel(self)
        dates.setText("Mar 2011 - Present")
        dates.move(15, 335)
        dates.setFont(QFont('SF Pro Display', 10))

        experience = QLabel(self)
        experience.setText("Pizza Delivery Driver")
        experience.move(15, 355)
        experience.setFont(QFont('SF Pro Display', 10))

        dates = QLabel(self)
        dates.setText("Aug 2015 - Dec 2017")
        dates.move(15, 375)
        dates.setFont(QFont('SF Pro Display', 10))


# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserProfile()
    sys.exit(app.exec_())
