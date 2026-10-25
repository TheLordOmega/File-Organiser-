import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

#code to customise the main window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Organiser")
        button = QPushButton("Organise Directory")
        self.setBaseSize(QSize(900,600))
        #central widget is button
        self.setCentralWidget(button)


app= QApplication(sys.argv)
window= MainWindow() #creates the window and shows it
window.show()

#starts the app
app.exec()


#{UI DESIGN:
# 1)
# buttons
#settings

##sidebar

#tiles like - liquid glass
