# Listing 10-5. Code to view SQL database using QSqlTableModel

import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel

class TableDisplay(QWidget):

    def __init__(self):
        super().__init__()

        self.initializeUI()
    
    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen.
        """
        self.setMinimumSize(1000, 500)
        self.setWindowTitle('SQL Table Model')

        self.createConnection()
        self.createTable()

        self.show()

    def createConnection(self):
        """
        Set up the connection to the database.
        Check for the tables needed.
        """
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("files/accounts.db")

        if not database.open():
            print("Unable to open data source file.")
            sys.exit(1)     # Error code 1 - signifies error
        
        # Check if the tables we need exist in the database
        tables_needed = { 'accounts' }
        tables_not_found = tables_needed - set(database.tables())

        if tables_not_found:
            QMessageBox.critical(None, 'Error', 
                f'The following tables are missing from the database: {tables_not_found}')
            sys.exit(1)     # Error code 1 - signifies error

    def createTable(self):
        """
        Create the table using model/view architecture.
        """
        # Create the model
        model = QSqlTableModel()
        model.setTable('accounts')

        table_view = QTableView()
        table_view.setModel(model)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Populate the model with data
        model.select()

        # Main layout
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(table_view)
        self.setLayout(main_v_box)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableDisplay()
    sys.exit(app.exec_())