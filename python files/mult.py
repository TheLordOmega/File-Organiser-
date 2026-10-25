import time

from PySide6.QtCore import QTimer, Slot, QRunnable, QThreadPool
from PySide6.QtWidgets import(
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0

        layout = QVBoxLayout()

        self.label = QLabel("start")
        button = QPushButton("Danger")
        button.pressed.connect(self.oh_no)


        layout.addWidget(self.label)
        layout.addWidget(button)

        w= QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        self.show()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

        self.threadpool = QThreadPool()
        thread_count = self.threadpool.maxThreadCount()
        print(f"Multithreadinn with maximum {thread_count} threads")

    def oh_no(self):
        worker = Worker()
        self.threadpool.start(worker)
    def recurring_timer(self):
        self.counter += 1
        self.label.setText(f"Counter:{self.counter}")


class Worker(QRunnable):
    """Worker thread"""

    @Slot()
    def run(self):
        """Your long-running job goes in this method"""
        print("Thread start")
        time.sleep(5)
        print("Thread complete")




app = QApplication()
window= MainWindow()
window.show()
app.exec()
