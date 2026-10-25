from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        self.setWindowTitle("File Organiser")
        self.resize(900,800)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)


app= QApplication
window = MainWindow
window.show()
app.exec()
