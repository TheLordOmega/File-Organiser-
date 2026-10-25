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

        button_action.setShortcut(QKeySequence("Ctrl +p "))
        toolbar.addAction(button_action)


        toolbar.addSeparator()

        button2 = QAction(QIcon("2.png"), "2", self)
        button2.setStatusTip("second button")
        button2.triggered.connect(self.toolbar_button_clicked)
        button2.setCheckable(True)
        toolbar.addAction(button2)

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())


        self.setStatusBar(QStatusBar(self))


        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button2)

        file_submenu = file_menu.addMenu("submenu")
        file_submenu.addAction(button2)




    def toolbar_button_clicked(self, s):
        print("click", s)





app = QApplication([])
window = MainWindow()
window.show()
app.exec()
