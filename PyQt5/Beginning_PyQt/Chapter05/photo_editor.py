# photo_editor.py
# Import necessary modules

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

class PhotoEditor(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initializeUI()
    
    def initializeUI(self):
        """
        Initialize the window and display its contents to the 
        screen.
        """
        self.setFixedSize(650, 650)
        self.setWindowTitle('5.2 - Photo Editor GUI')
        self.centerMainWindow()
        self.createToolsDockWidget()
        self.createMenu()
        self.createToolBar()
        self.photoEditorWidgets()

        self.show()

    def createMenu(self):
        """
        Create menu for photo editor GUI.
        """
        self.open_act = QAction(QIcon('images\\open_file.png'), 
            "Open", self)
        self.open_act.setShortcut('Ctrl+O')
        self.open_act.setStatusTip('Open a new image')
        self.open_act.triggered.connect(self.openImage)

        self.save_act = QAction(QIcon('images\\save_file.png'),
            "Save", self)
        self.save_act.setShortcut('Ctrl+S')
        self.save_act.setStatusTip('Save image')
        self.save_act.triggered.connect(self.saveImage)

        self.print_act = QAction(QIcon('images\\print.png'), 
            "Print", self)
        self.print_act.setShortcut('Ctrl+P')
        self.print_act.setStatusTip('Print image')
        self.print_act.triggered.connect(self.printImage)
        self.print_act.setEnabled(False)

        self.exit_act = QAction(QIcon('images\\exit.png'),
            "Exit", self)
        self.exit_act.setShortcut('Ctrl+Q')
        self.exit_act.setStatusTip('Quit program')
        self.exit_act.triggered.connect(self.close)

        # Create actions for edit menu
        self.rotate90_act = QAction("Rotate 90°", self)
        self.rotate90_act.setStatusTip('Rotate image 90° clockwise')
        self.rotate90_act.triggered.connect(self.rotateImage90)

        self.rotate180_act = QAction("Rotate 180°", self)
        self.rotate180_act.setStatusTip('Rotate image 180° clockwise')
        self.rotate180_act.triggered.connect(self.rotateImage180)

        self.flip_hor_act = QAction("Flip Horizontal", self)
        self.flip_hor_act.setStatusTip('Flip image across horizontal axis')
        self.flip_hor_act.triggered.connect(self.flipImageHorizontal)

        self.flip_ver_act = QAction("Flip Vertical", self)
        self.flip_ver_act.setStatusTip('Flip image across vertical axis')
        self.flip_ver_act.triggered.connect(self.flipImageVertical)

        self.resize_act = QAction("Resize Half", self)
        self.resize_act.setStatusTip('Resize image to half the original size')
        self.resize_act.triggered.connect(self.resizeImageHalf)

        self.clear_act = QAction(QIcon('images\\clear.png'), 
            "Clear Image", self)
        self.clear_act.setShortcut("Ctrl+D")
        self.clear_act.setStatusTip('Clear the current image')
        self.clear_act.triggered.connect(self.clearImage)

        #Create menubar
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        # Create file menu and add actions
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(self.open_act)
        file_menu.addAction(self.save_act)
        file_menu.addSeparator()
        file_menu.addAction(self.print_act)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_act)

        # Create edit meny and add action
        edit_menu = menu_bar.addMenu('Edit')
        edit_menu.addAction(self.rotate90_act)
        edit_menu.addAction(self.rotate180_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.flip_hor_act)
        edit_menu.addAction(self.flip_ver_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.resize_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.clear_act)

        # Create view menu and add actions
        view_menu = menu_bar.addMenu('View')
        view_menu.addAction(self.toggle_dock_tools_act)

        # Display info about tools, menu, and view in the status
        # bar.
        self.setStatusBar(QStatusBar(self))

    def createToolBar(self):
        """
        Create toolbar for photo editor GUI
        """
        tool_bar = QToolBar("Photo Editor Toolbar")
        tool_bar.setIconSize(QSize(24, 24))
        self.addToolBar(tool_bar)

        # Add actions to toolbar
        tool_bar.addAction(self.open_act)
        tool_bar.addAction(self.save_act)
        tool_bar.addAction(self.print_act)
        tool_bar.addAction(self.clear_act)
        tool_bar.addSeparator()
        tool_bar.addAction(self.exit_act)

    def createToolsDockWidget(self):
        """
        Use View -> Edit Image Tools menu and click the dock widget
        on or off. Tools dock can be replaced on the left or right
        of the main window.
        """
        # Set up QDockWidget
        self.dock_tools_view = QDockWidget()
        self.dock_tools_view.setWindowTitle("Edit Image Tools")
        self.dock_tools_view.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

        # Create container QWidget to hold all widgets inside dock 
        # widget.
        self.tools_contents = QWidget()

        # Create the tool push buttons
        self.rotate90 = QPushButton("Rotate 90°")
        self.rotate90.setMinimumSize(QSize(130, 40))
        self.rotate90.setStatusTip('Rotate image 90° clockwise')
        self.rotate90.clicked.connect(self.rotateImage90)

        self.rotate180 = QPushButton("Rotate 180°")
        self.rotate180.setMinimumSize(QSize(130, 40))
        self.rotate180.setStatusTip('Rotate image 180° clockwise')
        self.rotate180.clicked.connect(self.rotateImage180)

        self.flip_horizontal = QPushButton("Flip Horizontal")
        self.flip_horizontal.setMinimumSize(QSize(130, 40))
        self.flip_horizontal.setStatusTip('Flip image across horizontal axis')
        self.flip_horizontal.clicked.connnect(self.flipImageHorizontal)

        self.flip_vertical = QPushButton("Flip Vertical")
        self.flip_vertical.setMinimumSize(QSize(130, 40))
        self.flip_vertical.setStatusTip('Flip image across vertical axis')
        self.flip_vertical.clicked.connect(self.flipImageVertical)

        self.resize_half = QPushButton("Resize Half")
        self.resize_half.setMinimumSize(QSize(130, 40))
        self.resize_half.setStatusTip('Resize image to half the original size')
        self.resize_half.clicked.connect(self.resizeImageHalf)

        # Set up vertical layout to contain all the push buttons.
        dock_v_box = QVBoxLayout()
        dock_v_box.addWidget(self.rotate90)
        

    def photoEditorWidgets(self):
        pass

    def openImage(self):
        pass

    def saveImage(self):
        pass

    def printImage(self):
        pass

    def clearImage(self):
        pass

    def rotateImage90(self):
        pass

    def rotateImage180(self):
        pass
    
    def flipImageHorizontal(self):
        pass

    def flipImageVertical(self):
        pass

    def resizeImageHalf(self):
        pass

    def centerMainWindow(self):
        pass


# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DontShowIconsInMenus, True)
    window = PhotoEditor()
    sys.exit(app.exec_())