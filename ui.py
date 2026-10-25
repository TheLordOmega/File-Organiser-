import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

#code to customise the main window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Organiser")


        self.button = QPushButton("Organise Directory")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_clicked)
        self.button.clicked.connect(self.button_checked)
        self.resize(900, 600)
        #central widget is button
        self.setCentralWidget(self.button)
    def button_clicked(self):
        print("Already clicked!")
        self.button.setEnabled(False)
        self.setWindowTitle("Done!")



    def button_checked(self, checked):
        button_status = checked
        print(button_status)

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
