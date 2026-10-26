import sys
from pathlib import Path

from PySide6.QtCore import QEvent, QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMenu,
    QPushButton,
    QSizeGrip,
    QStackedWidget,
    QToolButton,
    QVBoxLayout,
    QWidget,
)


class CustomTitleBar(QWidget):
    """Small custom title bar with native window-move support."""

    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedHeight(46)
        self._drag_offset = None

        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 4, 8, 4)
        layout.setSpacing(0)

        # Matching spacer keeps the title centered despite the controls at right.
        left_spacer = QWidget(self)
        left_spacer.setFixedWidth(132)
        layout.addWidget(left_spacer)

        self.title = QLabel(parent.windowTitle(), self)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.title.setObjectName("WindowTitle")
        parent.windowTitleChanged.connect(self.title.setText)
        layout.addWidget(self.title, 1)

        controls = QWidget(self)
        controls.setFixedWidth(132)
        controls_layout = QHBoxLayout(controls)
        controls_layout.setContentsMargins(0, 0, 0, 0)
        controls_layout.setSpacing(4)

        self.min_button = self._make_button("—", "Minimize")
        self.max_button = self._make_button("□", "Maximize")
        self.close_button = self._make_button("×", "Close")
        self.close_button.setObjectName("CloseButton")

        self.min_button.clicked.connect(parent.showMinimized)
        self.max_button.clicked.connect(self.toggle_maximize)
        self.close_button.clicked.connect(parent.close)

        controls_layout.addWidget(self.min_button)
        controls_layout.addWidget(self.max_button)
        controls_layout.addWidget(self.close_button)
        layout.addWidget(controls)

    @staticmethod
    def _make_button(text, tooltip):
        button = QToolButton()
        button.setText(text)
        button.setToolTip(tooltip)
        button.setAccessibleName(tooltip)
        button.setFixedSize(QSize(38, 32))
        button.setObjectName("WindowButton")
        return button

    def toggle_maximize(self):
        if self.window().isMaximized():
            self.window().showNormal()
        else:
            self.window().showMaximized()
        self.update_window_state()

    def update_window_state(self):
        maximized = self.window().isMaximized()
        self.max_button.setText("❐" if maximized else "□")
        self.max_button.setToolTip("Restore" if maximized else "Maximize")
        self.max_button.setAccessibleName(self.max_button.toolTip())

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

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.toggle_maximize()
            event.accept()
            return
        super().mouseDoubleClickEvent(event)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Organiser")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Window)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setMinimumSize(720, 500)
        self.resize(960, 640)

        self.selected_directory = ""
        self.title_bar = CustomTitleBar(self)
        self.pages = QStackedWidget()
        self.nav_group = QButtonGroup(self)
        self.nav_group.setExclusive(True)

        central = QWidget(self)
        central.setObjectName("Container")
        central.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.central_surface = central

        root_layout = QVBoxLayout(central)
        root_layout.setContentsMargins(12, 8, 12, 8)
        root_layout.setSpacing(12)
        root_layout.addWidget(self.title_bar)

        self.nav_bar = self._make_navigation()
        root_layout.addWidget(self.nav_bar, 0, Qt.AlignmentFlag.AlignHCenter)

        self._make_pages()
        self.nav_group.idClicked.connect(self.pages.setCurrentIndex)
        self.nav_group.button(0).setChecked(True)
        root_layout.addWidget(self.pages, 1)

        # QSizeGrip provides a resize affordance for a frameless window.
        footer = QHBoxLayout()
        footer.setContentsMargins(0, 0, 2, 0)
        footer.addStretch(1)
        footer.addWidget(
            QSizeGrip(central),
            0,
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom,
        )
        root_layout.addLayout(footer)

        self.setCentralWidget(central)
        central.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        central.customContextMenuRequested.connect(self.show_context_menu)
        self.setStyleSheet(self._stylesheet())

    def _make_navigation(self):
        names = ["Clean", "Optimize", "History", "Settings"]
        bar = QWidget(self)
        bar.setObjectName("NavBar")
        bar.setFixedHeight(56)

        layout = QHBoxLayout(bar)
        layout.setContentsMargins(9, 6, 9, 6)
        layout.setSpacing(4)
        layout.addStretch(1)

        logo = QLabel("◈", bar)
        logo.setObjectName("BrandMark")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logo)

        separator = QFrame(bar)
        separator.setFrameShape(QFrame.Shape.VLine)
        separator.setObjectName("NavSeparator")
        layout.addWidget(separator)

        for index, name in enumerate(names):
            button = QPushButton(name, bar)
            button.setObjectName("NavButton")
            button.setCheckable(True)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            self.nav_group.addButton(button, index)
            layout.addWidget(button)

        layout.addStretch(1)
        return bar

    def _make_pages(self):
        clean_page = QWidget(self.pages)
        clean_layout = QVBoxLayout(clean_page)
        clean_layout.setContentsMargins(28, 24, 28, 24)
        clean_layout.setSpacing(14)

        heading = QLabel("Organize your files", clean_page)
        heading.setObjectName("PageHeading")
        description = QLabel(
            "Choose a folder to review before organizing its files.", clean_page
        )
        description.setObjectName("SecondaryText")
        description.setWordWrap(True)

        folder_card = QWidget(clean_page)
        folder_card.setObjectName("FolderCard")
        folder_layout = QVBoxLayout(folder_card)
        folder_layout.setContentsMargins(18, 16, 18, 16)
        folder_layout.setSpacing(12)

        folder_label = QLabel("SOURCE FOLDER", folder_card)
        folder_label.setObjectName("Eyebrow")
        self.folder_path_label = QLabel("No folder selected", folder_card)
        self.folder_path_label.setObjectName("FolderPath")
        self.folder_path_label.setWordWrap(True)
        self.folder_path_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )

        folder_buttons = QHBoxLayout()
        folder_buttons.addWidget(self.folder_path_label, 1)
        self.choose_button = QPushButton("Choose folder…", folder_card)
        self.choose_button.setObjectName("SecondaryButton")
        self.choose_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.choose_button.clicked.connect(self.choose_folder)
        folder_buttons.addWidget(self.choose_button)

        folder_layout.addWidget(folder_label)
        folder_layout.addLayout(folder_buttons)

        self.organize_button = QPushButton("Organise Directory", clean_page)
        self.organize_button.setObjectName("PrimaryButton")
        self.organize_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.organize_button.clicked.connect(self.organise_selected_folder)

        self.status_label = QLabel("Ready", clean_page)
        self.status_label.setObjectName("SecondaryText")
        self.status_label.setWordWrap(True)

        clean_layout.addWidget(heading)
        clean_layout.addWidget(description)
        clean_layout.addSpacing(8)
        clean_layout.addWidget(folder_card)
        clean_layout.addWidget(self.organize_button)
        clean_layout.addWidget(self.status_label)
        clean_layout.addStretch(1)
        self.pages.addWidget(clean_page)

        for name in ["Optimize", "History", "Settings"]:
            page = QWidget(self.pages)
            page_layout = QVBoxLayout(page)
            page_layout.setContentsMargins(28, 24, 28, 24)
            page_layout.addWidget(QLabel(name, page), 0, Qt.AlignmentFlag.AlignTop)
            page_layout.addWidget(
                QLabel(f"The {name.lower()} page is ready for your next feature.", page),
                0,
                Qt.AlignmentFlag.AlignTop,
            )
            page_layout.addStretch(1)
            self.pages.addWidget(page)

    def choose_folder(self):
        start_directory = self.selected_directory or str(Path.home())
        directory = QFileDialog.getExistingDirectory(
            self,
            "Choose a folder to organize",
            start_directory,
        )
        if directory:
            self.selected_directory = directory
            self.folder_path_label.setText(directory)
            self.status_label.setText("Folder selected. Review it before continuing.")

    def organise_selected_folder(self):
        if not self.selected_directory:
            self.status_label.setText("Choose a folder first.")
            return

        self.status_label.setText(
            "Folder selected. Connect your file-organizing function here; "
            "this UI does not move files yet."
        )

    def show_context_menu(self, position):
        menu = QMenu(self)
        choose_action = menu.addAction("Choose folder…")
        reset_action = menu.addAction("Clear selected folder")
        selected_action = menu.exec(self.central_surface.mapToGlobal(position))

        if selected_action == choose_action:
            self.choose_folder()
        elif selected_action == reset_action:
            self.selected_directory = ""
            self.folder_path_label.setText("No folder selected")
            self.status_label.setText("Ready")

    def changeEvent(self, event):
        super().changeEvent(event)
        if (
            event.type() == QEvent.Type.WindowStateChange
            and hasattr(self, "title_bar")
        ):
            self.title_bar.update_window_state()

    @staticmethod
    def _stylesheet():
        return """
            QWidget#Container {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgba(34, 29, 39, 248),
                    stop: 1 rgba(68, 40, 47, 248)
                );
                border: 1px solid rgba(255, 255, 255, 46);
                border-radius: 18px;
            }
            QLabel#WindowTitle {
                color: rgba(255, 255, 255, 220);
                font-size: 10pt;
                font-weight: 600;
            }
            QToolButton#WindowButton {
                color: rgba(255, 255, 255, 225);
                background: transparent;
                border: none;
                border-radius: 7px;
                font-size: 14pt;
            }
            QToolButton#WindowButton:hover {
                background: rgba(255, 255, 255, 35);
            }
            QToolButton#CloseButton:hover {
                background: #c84b55;
                color: white;
            }
            QWidget#NavBar {
                background: rgba(255, 255, 255, 25);
                border: 1px solid rgba(255, 255, 255, 42);
                border-radius: 25px;
            }
            QLabel#BrandMark {
                color: #fffaf4;
                background: rgba(255, 255, 255, 28);
                border-radius: 17px;
                min-width: 34px;
                max-width: 34px;
                min-height: 34px;
                max-height: 34px;
                font-size: 16pt;
            }
            QFrame#NavSeparator {
                color: rgba(255, 255, 255, 55);
                margin: 4px 5px;
            }
            QPushButton#NavButton {
                color: rgba(255, 255, 255, 205);
                background: transparent;
                border: none;
                border-radius: 19px;
                padding: 8px 15px;
                min-height: 22px;
                font-size: 10pt;
            }
            QPushButton#NavButton:hover {
                background: rgba(255, 255, 255, 28);
            }
            QPushButton#NavButton:checked {
                color: #282326;
                background: rgba(250, 248, 245, 250);
                font-weight: 600;
            }
            QLabel#PageHeading {
                color: #fffaf7;
                font-size: 23pt;
                font-weight: 600;
            }
            QLabel#SecondaryText {
                color: rgba(255, 255, 255, 175);
                font-size: 10pt;
            }
            QLabel#Eyebrow {
                color: rgba(255, 255, 255, 145);
                font-size: 8pt;
                font-weight: 600;
                letter-spacing: 1px;
            }
            QWidget#FolderCard {
                background: rgba(255, 255, 255, 22);
                border: 1px solid rgba(255, 255, 255, 38);
                border-radius: 14px;
            }
            QLabel#FolderPath {
                color: #fffaf7;
                font-size: 10pt;
            }
            QPushButton#SecondaryButton {
                color: #fffaf7;
                background: rgba(255, 255, 255, 30);
                border: 1px solid rgba(255, 255, 255, 55);
                border-radius: 10px;
                padding: 10px 14px;
            }
            QPushButton#SecondaryButton:hover {
                background: rgba(255, 255, 255, 48);
            }
            QPushButton#PrimaryButton {
                color: #282326;
                background: #f8f5f1;
                border: none;
                border-radius: 11px;
                padding: 12px 18px;
                font-weight: 600;
            }
            QPushButton#PrimaryButton:hover {
                background: #ffffff;
            }
            QPushButton#PrimaryButton:pressed {
                background: #e5dfd8;
            }
            QMenu {
                color: #fffaf7;
                background: #302a33;
                border: 1px solid rgba(255, 255, 255, 55);
                padding: 5px;
            }
            QMenu::item {
                padding: 7px 22px;
                border-radius: 5px;
            }
            QMenu::item:selected {
                background: rgba(255, 255, 255, 35);
            }
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("File Organiser")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
