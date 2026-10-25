import sys
from fileinput import filename
from pathlib import Path

from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QGridLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QPushButton,
    QWidget,
)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("File Dialog")
        self.setGeometry(100,100,300,150)


        layout = QGridLayout()
        self.setLayout(layout)


        browsebtn = QPushButton('Browse')
        browsebtn.clicked.connect(self.open_dir_dialog)
        self.dir_name_edit =    QLineEdit()

        layout.addWidget(QLabel('Directory:'), 1, 0)
        layout.addWidget(self.dir_name_edit, 1,1)
        layout.addWidget(browsebtn, 1,2)


        self.show()

    def open_dir_dialog(self):
        dir_name = QFileDialog.getExistingDirectory(self, "Select a Directory")
        if dir_name:
            path= Path(dir_name)
            self.dir_name_edit.setText(str(path))







 #   def open_file_dialog(self):
  #      dialog = QFileDialog(self)
   #     dialog.setDirectory(r'C:\images')
    #    dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
     #   dialog.setNameFilter("Images(*.png)")
      #  dialog.setViewMode(QFileDialog.ViewMode.List)
#
 #       if dialog.exec():
  #          filenames = dialog.selectedFiles()
   #         if filenames:
    #            self.file_list.addItems([str(Path(filename)) for filename in filenames])


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
