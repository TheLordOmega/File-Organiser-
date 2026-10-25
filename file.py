from PySide6.QtWidgets import QFileDialog

dialog= QFileDialog(self) #creates a doaglog object
dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)

#save as:
# dialog.setFileMode(QfileDialog.FileMode.AnyFile)
#


dialog.setNameFilter("Images(*.png *.jpg);;Documents(*.md, *docx")
