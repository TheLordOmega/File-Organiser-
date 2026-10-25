
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
        self.setFixedHeight(36)

        self.setAutoFillBackground(True)
        self.setBackgroundRole(QPalette.ColorRole.Highlight)

        titlela = QHBoxLayout(self)
        titlela.setContentsMargins(1, 1, 1, 1)
        titlela.setSpacing(2)

        # Title label
        self.title = QLabel(parent.windowTitle(), self)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setAttribute(
            Qt.WidgetAttribute.WA_TransparentForMouseEvents
        )
        self.title.setStyleSheet("""
            QLabel {
                font-weight: bold;
                border: 2px;
                border-radius: 12px;
                margin: 2px;
            }
        """)

        titlela.addWidget(self.title, 1)

        # Minimize button
        self.min_button = QToolButton(self)
        self.min_button.setIcon(
            self.style().standardIcon(
                QStyle.StandardPixmap.SP_TitleBarMinButton
            )
        )
        self.min_button.clicked.connect(self.window().showMinimized)

        # Maximize button
        self.max_button = QToolButton(self)
        self.max_button.setIcon(
            self.style().standardIcon(
                QStyle.StandardPixmap.SP_TitleBarMaxButton
            )
        )
        self.max_button.clicked.connect(self.toggle_maximize)

        # Restore button
        self.normal_button = QToolButton(self)
        self.normal_button.setIcon(
            self.style().standardIcon(
                QStyle.StandardPixmap.SP_TitleBarNormalButton
            )
        )
        self.normal_button.clicked.connect(self.toggle_maximize)
        self.normal_button.setVisible(False)

        # Close button
        self.close_button = QToolButton(self)
        self.close_button.setIcon(
            self.style().standardIcon(
                QStyle.StandardPixmap.SP_TitleBarCloseButton
            )
        )
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
            button.setFixedSize(QSize(28, 28))
            button.setStyleSheet("""
                QToolButton {
                    border: 2px solid white;
                    border-radius: 12px;
                }
                QToolButton:hover {
                    background-color: #555555;
                }
            """)
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
