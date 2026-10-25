from fileinput import filename
import sys

from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QWidget,
    QFileDialog,
    QGridLayout,
    QPushButton,
    QLabel,
    QListWidget

)

from pathlib import Path

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("File Dialog")
        self.setGeometry(100,100,300,150)


        layout = QGridLayout()
        self.setLayout(layout)


        browsebtn = QPushButton('Browse')
        browsebtn.clicked.connect(self.open_file_dialog)

        self.file_list= QListWidget(self)

        layout.addWidget(QLabel('Files:'), 0, 0)
        layout.addWidget(self.file_list, 1,0)
        layout.addWidget(browsebtn, 2, 0)


        self.show()

    def open_file_dialog(self):
        dialog = QFileDialog(self)
        dialog.setDirectory(r'C:\images')
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("Images(*.png)")
        dialog.setViewMode(QFileDialog.ViewMode.List)

        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                self.file_list.addItems([str(Path(filename)) for filename in filenames])


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
