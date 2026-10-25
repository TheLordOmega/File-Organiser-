from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
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
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("settings.png"), "Settings", self)
        button_action.setStatusTip("this is button")
        button_action.triggered.connect(self.toolbar_button_clicked)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)


        self.setStatusBar(QStatusBar(self))



    def toolbar_button_clicked(self, s):
        print("click", s)





app = QApplication([])
window = MainWindow()
window.show()
app.exec()
