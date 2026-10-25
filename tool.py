from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QKeySequence
from PySide6.Qtgui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("toolbar")

        toolbar = QToolBar("Options")
        self.addToolBar(toolbar)



app = QApplication([])
window = MainWindow()
window.show()
app.exec()
