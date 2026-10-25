import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPalette
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QStyle,
    QToolButton,
    QVBoxLayout,
    QWidget,
)


class CustomTitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        self.setBackgroundRole(QPalette.ColorRole.Highlight)
        self.inital_pos = None
        titlela = QHBoxLayout(self)
        titlela.setContentsMargins(1,1,1,1)
        titlela.setSpacing(2)




        #top bar buttons

        self.min_button = QToolButton(self)
        min_icon = self.style().standardIcon(
            QStyle.StandardPixmap.SP_TitleBarMinButton
        )
        self.min_button.setIcon(min_icon)
        self.min_button.clicked.connect(self.window().showMinimized)




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Organiser")
        self.resize(900,800)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        central_widget = QWidget()
        self.title_bar = CustomTitleBar(self)

        layout = QVBoxLayout()
        layout.setContentsMargins(11,11,11,11)
        layout.addWidget(QLabel("hello world", self))


        #central widget layout
        cw_l = QVBoxLayout()
        cw_l.setAlignment(Qt.AlignmentFlag.AlignTop)
        cw_l.addWidget(self.title_bar)
        cw_l.addLayout(layout)

        central_widget.setLayout(cw_l)
        self.setCentralWidget(central_widget)






app= QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
