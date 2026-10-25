import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QMenu,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

#code to customise the main window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Organiser") #name of window
        self.label = QLabel()  #makes a label

        self.button = QPushButton("Organise Directory") #button with name that is checkable
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_clicked) #connects it to a signal when clicked
        self.button.clicked.connect(self.button_checked)
        self.resize(900, 600) #default size

        layout = QVBoxLayout()  #layout maker
        layout.addWidget(self.label)
        layout.addWidget(self.button)


        container = QWidget()
        container.setLayout(layout)


        #central widget is container
        self.setCentralWidget(container)

        #signals for context menu
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.contextMenuEvent)


    def button_clicked(self):
        self.setWindowTitle("Done!")

#######mouse presses tracking
    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.RightButton:
            self.label.setText("left clicked")
        if e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("middle clicked")

    def button_checked(self, checked):
        button_status = checked
        print(button_status)
###makes the context menu with different actions
    def contextMenuEvent(self, pos):
        context= QMenu(self)



        context.addAction(QAction("test 1",self))
        context.addAction(QAction("test 2",self))
        context.addAction(QAction("test 3",self))
        context.exec(self.mapToGlobal(pos))

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
