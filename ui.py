from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

import sys





#code to customise the main window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Organiser")
        button = QpushButton("Organise Directory")

        #central widget is button
        self.setCentralWidget(button)


app= QApplication(sys.argv)
window= QMainWindow() #creates the window and shows it
window.show()

#starts the app
app.exec()


#{UI DESIGN:
# 1)
# buttons
#settings

##sidebar

#tiles like - liquid glass
