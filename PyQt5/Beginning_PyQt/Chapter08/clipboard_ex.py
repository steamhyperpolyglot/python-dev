# clipboard_ex.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ClipboardEx(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initializeUI()
    
    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """

        self.setMinimumSize(QSize(500, 300))
        self.setWindowTitle("Clipboard Example")

        self.central_widget = QTextEdit()
        self.setCentralWidget(self.central_widget)

        self.createClipboard()

        self.show()
    
    def createClipboard(self):
        """
        Set up clipboard and dock widget to display text from the clipboard.
        """

        # Create dock widget
        clipboard_dock = QDockWidget()
        clipboard_dock.setWindowTitle("Display Clipboard Contents")
        clipboard_dock.setAllowedAreas(Qt.TopDockWidgetArea)

        dock_frame = QFrame()
        self.cb_text = QTextEdit()
        paste_button = QPushButton("Paste")
        paste_button.clicked.connect(self.pasteText)

        dock_v_box = QVBoxLayout()
        dock_v_box.addWidget(self.cb_text)
        dock_v_box.addWidget(paste_button)

        # Set the main layout for the dock widget,
        # then set the main widget of the dock widget
        dock_frame.setLayout(dock_v_box)
        clipboard_dock.setWidget(dock_frame)

        # Set initial location of dock widget
        self.addDockWidget(Qt.TopDockWidgetArea, clipboard_dock)

        # Create instance of the clipboard
        self.clipboard = QApplication.clipboard()
        self.clipboard.dataChanged.connect(self.copyFromClipboard)
    
    def copyFromClipboard(self):
        """
        Get the contents of the system clipboard.
        """
        mime_data = self.clipboard.mimeData()
        if mime_data.hasText():
            self.cb_text.setText(mime_data.text())
    
    def pasteText(self):
        """
        Paste text from the clipboard if button is clicked.
        """
        self.central_widget.paste()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClipboardEx()
    sys.exit(app.exec_())