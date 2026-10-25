
import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPalette, QIcon
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
        self.setFixedHeight(36)

        self.initial_pos = None
        titlela = QHBoxLayout(self)
        titlela.setContentsMargins(1, 1, 1, 1)
        titlela.setSpacing(2)
        self.title = QLabel(f"{self.__class__.__name__}", self)

        # Title label
        self.title = QLabel(parent.windowTitle(), self)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setAttribute(
            Qt.WidgetAttribute.WA_TransparentForMouseEvents
        )
        self.title.setStyleSheet(
            """
            QLabel {
            text-transform: uppercase;
            font-size: 10pt;
            margin-left: 48px;
            color: white;
            }
        """
        )

        titlela.addWidget(self.title, 1)
        # Minimize button
        self.min_button = QToolButton(self)
        min_icon = QIcon()
        min_icon.addFile('min.svg')
        self.min_button.setIcon(min_icon)
        self.min_button.clicked.connect(self.window().showMinimized)

        # Maximize button
        self.max_button = QToolButton(self)
        max_icon = QIcon()
        max_icon.addFile('max.svg')
        self.max_button.setIcon(max_icon)
        self.max_button.clicked.connect(self.toggle_maximize)

        # Restore button
        self.normal_button = QToolButton(self)
        normal_icon = QIcon()
        normal_icon.addFile('normal.svg')
        self.normal_button.setIcon(normal_icon)
        self.normal_button.clicked.connect(self.toggle_maximize)
        self.normal_button.setVisible(False)

        # Close button
        self.close_button = QToolButton(self)
        close_icon = QIcon()
        close_icon.addFile('close.svg')
        self.close_button.setIcon(close_icon)
        self.close_button.clicked.connect(self.window().close)

        # Configure buttons
        buttons = [
            self.min_button,
            self.max_button,
            self.normal_button,
            self.close_button,
        ]

        for button in buttons:
            button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            button.setFixedSize(QSize(16,16))
            button.setStyleSheet(
                """QToolButton{
                        border:none;
                        padding: 2px;
                        }
                        QToolButton:hover {
                        background-color: #555555;
                            }
                            """
            )
            titlela.addWidget(button)

    def toggle_maximize(self):
        window = self.window()

        if window.isMaximized():
            window.showNormal()
        else:
            window.showMaximized()

        self.update_window_state()

    def update_window_state(self):
        maximized = self.window().isMaximized()

        self.max_button.setVisible(not maximized)
        self.normal_button.setVisible(maximized)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            handle = self.window().windowHandle()

            if handle is not None and handle.startSystemMove():
                event.accept()
                return

        super().mousePressEvent(event)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Organiser")
        self.resize(900, 800)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet("background-color:gray; border-radius:10px;")
        central_widget = QWidget()

        central_widget.setObjectName("Container")
        central_widget.setStyleSheet(
            """#Container{
                    background: qlineargradient(x1:0 y1:0, x2:1 y2:1, stop:0 #051c2a stop:1 #44315f);
                    border-radius: 5px;
            }

            """
        )

        self.title_bar = CustomTitleBar(self)

        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(11, 11, 11, 11)
        content_layout.addWidget(QLabel("Hello world"))

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(self.title_bar)
        main_layout.addLayout(content_layout)

        self.setCentralWidget(central_widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
