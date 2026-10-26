import code
import time

from PySide6.QtCore import QTimer, Slot, QRunnable, QThreadPool
from PySide6.QtCore import QObject, Signal
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

    def execute_this_fn(self):
        print("Hello!")

    def oh_no(self):
        worker = Worker(
            self.execute_this_fn
        )
        self.threadpool.start(worker)
    def recurring_timer(self):
        self.counter += 1
        self.label.setText(f"Counter:{self.counter}")


class Worker(QRunnable):
    """Worker thread.

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread.
                     Supplied args and kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function
    """
    def __init__(self, fn , *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs


    @Slot()
    def run(self):
        """Initialise the runner function with passed args, kwargs"""
        self.fn(*self.args, **self.kwargs)

        try:
            result = self.fn(*self.args, **self.kwargs)
        except Exception:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit(self.thread_id)


class WorkerSignals(QObject):
    """signals from a running worker thread.

    finished
        int thread_id
    error
        tuple(exctype, value, traceback.format_exc())
    result
        object data returned from processing, anything
    progress
        tuple(thread_id, progress_value)

    """

    finished= Signal(int)
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(tuple)


app = QApplication()
window= MainWindow()
window.show()
app.exec()
