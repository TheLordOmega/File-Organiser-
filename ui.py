import sys
from pathlib import Path

from PySide6.QtCore import QEvent, QSize, Qt
from PySide6.QtGui import QAction, QIcon, QCursor
from PySide6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMenu,
    QMessageBox,
    QPushButton,
    QStackedWidget,
    QToolButton,
    QVBoxLayout,
    QWidget,
)

from scanner import organizer


# Code to customise the title bar.
class CustomTitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedHeight(50)
        self._drag_offset = None

        titlela = QHBoxLayout(self)
        titlela.setContentsMargins(8, 4, 8, 4)
        titlela.setSpacing(0)

        # Spacer on the left balances the controls on the right,
        # keeping the window title centered.
        left_spacer = QWidget(self)
        left_spacer.setFixedWidth(132)
        titlela.addWidget(left_spacer)

        # Title label.
        self.title = QLabel(parent.windowTitle(), self)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setAttribute(
            Qt.WidgetAttribute.WA_TransparentForMouseEvents
        )
        parent.windowTitleChanged.connect(self.title.setText)
        self.title.setStyleSheet(
            """
            QLabel {
                text-transform: uppercase;
                font-size: 10pt;
                color: white;
            }
            """
        )
        titlela.addWidget(self.title, 1)

        # Keep the original right-side window controls and SVG icons.
        controls = QWidget(self)
        controls.setFixedWidth(132)
        controls_layout = QHBoxLayout(controls)
        controls_layout.setContentsMargins(0, 0, 0, 0)
        controls_layout.setSpacing(4)

        icon_dir = Path(__file__).resolve().parent

        # Minimize button.
        self.min_button = QToolButton(self)
        min_icon = QIcon(str(icon_dir / "min.svg"))
        self.min_button.setIcon(min_icon)
        self.min_button.clicked.connect(self.window().showMinimized)

        # Maximize button.
        self.max_button = QToolButton(self)
        max_icon = QIcon(str(icon_dir / "max.svg"))
        self.max_button.setIcon(max_icon)
        self.max_button.clicked.connect(self.toggle_maximize)

        # Restore button.
        self.normal_button = QToolButton(self)
        normal_icon = QIcon(str(icon_dir / "normal.svg"))
        self.normal_button.setIcon(normal_icon)
        self.normal_button.clicked.connect(self.toggle_maximize)
        self.normal_button.setVisible(False)

        # Close button.
        self.close_button = QToolButton(self)
        close_icon = QIcon(str(icon_dir / "close.svg"))
        self.close_button.setIcon(close_icon)
        self.close_button.clicked.connect(self.window().close)

        # Configure the original buttons.
        buttons = [
            self.min_button,
            self.max_button,
            self.normal_button,
            self.close_button,
        ]

        for button in buttons:
            button.setIconSize(QSize(14, 14))
            button.setToolTip("Window control")
            button.setFixedSize(QSize(40, 32))
            button.setStyleSheet(
                """
                QToolButton {
                    border: none;
                    padding: 2px;
                }
                QToolButton:hover {
                    background-color: #555555;
                }
                """
            )
            controls_layout.addWidget(button)

        titlela.addWidget(controls)

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

            # Fallback for platforms that do not support startSystemMove().
            self._drag_offset = (
                event.globalPosition().toPoint()
                - self.window().frameGeometry().topLeft()
            )
            event.accept()
            return

        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if (
            self._drag_offset is not None
            and event.buttons() & Qt.MouseButton.LeftButton
        ):
            self.window().move(
                event.globalPosition().toPoint() - self._drag_offset
            )
            event.accept()
            return

        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self._drag_offset = None
        super().mouseReleaseEvent(event)


# Code to customise the main window.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Organiser")
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | Qt.WindowType.Window
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setMinimumSize(720, 480)
        self.resize(900, 600)
        self.setMinimumSize(720, 480)

        self.selected_directory = ""
        self.title_bar = CustomTitleBar(self)

        page_names = ["Clean", "Optimize", "History", "Settings"]

        # Top pill navigation.
        self.naviwi = QWidget()
        self.naviwi.setObjectName("NavBar")
        self.naviwi.setFixedHeight(56)

        navila = QHBoxLayout(self.naviwi)
        navila.setContentsMargins(8, 6, 8, 6)
        navila.setSpacing(4)
        navila.addStretch(1)

        self.nav_group = QButtonGroup(self)
        self.nav_group.setExclusive(True)

        for index, name in enumerate(page_names):
            button = QPushButton(name)
            button.setObjectName("NavButton")
            button.setCheckable(True)
            self.nav_group.addButton(button, index)
            navila.addWidget(button)

        navila.addStretch(1)

        # The page stack changes when a navigation button is clicked.
        self.pages = QStackedWidget()
        self.button = QPushButton("Organise Directory")
        self.button.clicked.connect(self.button_clicked)

        clean_page = QWidget()
        cleanla = QVBoxLayout(clean_page)
        cleanla.addWidget(QLabel("File Organiser"))

        self.label = QLabel("Choose a folder to start.")
        cleanla.addWidget(self.label)

        self.choose_button = QPushButton("Choose folder…")
        self.choose_button.clicked.connect(self.choose_folder)
        cleanla.addWidget(self.choose_button)
        cleanla.addWidget(self.button)
        cleanla.addStretch(1)
        self.pages.addWidget(clean_page)

        for name in page_names[1:]:
            page = QWidget()
            pagela = QVBoxLayout(page)
            pagela.addWidget(QLabel(f"{name} later"))
            self.pages.addWidget(page)

        self.nav_group.idClicked.connect(self.pages.setCurrentIndex)
        self.nav_group.button(0).setChecked(True)

        # One central widget contains the title bar, navigation, and pages.
        central_widget = QWidget()
        central_widget.setObjectName("Container")
        central_widget.setAttribute(
            Qt.WidgetAttribute.WA_StyledBackground, True
        )
        central_widget.setStyleSheet(
            """
            #Container {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgba(5, 28, 42, 248),
                    stop: 1 rgba(68, 49, 95, 248)
                );
                border: 1px solid rgba(255, 255, 255, 45);
                border-radius: 16px;
            }
            #NavBar {
                background-color: rgba(255, 255, 255, 24);
                border: 1px solid rgba(255, 255, 255, 42);
                border-radius: 28px;
            }
            QPushButton#NavButton {
                background: transparent;
                border: none;
                border-radius: 20px;
                color: rgba(255, 255, 255, 205);
                padding: 8px 16px;
            }
            QPushButton#NavButton:hover {
                background-color: rgba(255, 255, 255, 28);
            }
            QPushButton#NavButton:checked {
                background-color: rgba(250, 248, 245, 250);
                color: #282326;
                font-weight: 600;
            }
            QPushButton {
                padding: 8px 12px;
            }
            """
        )

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(12, 8, 12, 12)
        main_layout.setSpacing(12)
        main_layout.addWidget(self.title_bar)
        main_layout.addWidget(
            self.naviwi,
            0,
            Qt.AlignmentFlag.AlignHCenter,
        )
        main_layout.addWidget(self.pages, 1)

        self.setCentralWidget(central_widget)

        # Context menu on the central background.
        central_widget.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu
        )
        central_widget.customContextMenuRequested.connect(
            self.show_context_menu
        )

    def choose_folder(self):
        directory = QFileDialog.getExistingDirectory(
            self,
            "Choose a folder to organize",
            self.selected_directory or str(Path.home()),
        )

        if directory:
            self.selected_directory = directory
            self.label.setText(f"Selected folder: {directory}")

    def button_clicked(self):
        if not self.selected_directory:
            self.label.setText("Choose a folder first.")
            return

        answer = QMessageBox.question(
            self,
            "Organize files",
            "Organize files directly inside this folder?\n\n"
            f"{self.selected_directory}\n\n"
            "Files will be moved into text_files subfolders.",
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if answer != QMessageBox.StandardButton.Yes:
            self.label.setText("Cancelled. No files were moved.")
            return
        try:
            moved, errors = organizer(self.selected_directory)
        except (OSError, ValueError) as error:
            self.label.setText(f"Could not organize folder: {error}")
            return


        if errors:
            self.label.setText(
                f"Moved {moved} files, but some errors occurred"
            )
            QMessageBox.warning(
                self,
                "Organizer errors",
                "\n".join(errors[:5])
            )
        else:
            self.label.setText(f"Organized {moved} files")

        # Connect the organizer function here when it is ready.
        self.label.setText(
            f"Ready to organize: {self.selected_directory}"
        )

    def show_context_menu(self, pos):
       context = QMenu(self)

       choose_action = context.addAction("Choose folder…")
       clear_action = context.addAction("Clear selected folder")

       # QCursor.pos() is already a global screen position.
       selected_action = context.exec(QCursor.pos())

       if selected_action == choose_action:
           self.choose_folder()
       elif selected_action == clear_action:
           self.selected_directory = ""
           self.label.setText("Choose a folder to start.")

    def changeEvent(self, event):
        super().changeEvent(event)

        if (
            event.type() == QEvent.Type.WindowStateChange
            and hasattr(self, "title_bar")
        ):
            self.title_bar.update_window_state()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
