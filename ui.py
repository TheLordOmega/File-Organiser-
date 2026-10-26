import sys
from pathlib import Path

from PySide6.QtCore import QSize, Qt, QEvent
from PySide6.QtGui import QAction, QIcon, QPalette
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMenu,
    QPushButton,
    QStyle,
    QToolButton,
    QVBoxLayout,
    QWidget,
    QButtonGroup,
    QStackedWidget
)

from e import controls_layout


#code to customise the titlebar
class CustomTitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedHeight(50)
        self._drag_offet = None

        titlela = QHBoxLayout(self)
        titlela.setContentsMargins(8, 4, 8,4 )
        titlela.setSpacing(0)
            #spacer to keep things centered
        left_spacer = QWidget(self)
        left_spacer.setFixedWidth(132)
        titlela.addWidget(left_spacer)

        # Title label
        self.title = QLabel(parent.windowTitle(), self)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setAttribute(
            Qt.WidgetAttribute.WA_TransparentForMouseEvents
        )
        parent.windowTitleChanged.connect(self.title.setText)
        titlela.addWidget(self.title, 1)



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

        controls = QWidget(self)
        controls.setFixedWidth(132)
        controls_layout = QHBoxLayout(controls)
        controls_layout.setContentsMargins( 0,0 , 0, 0)
        controls_layout.setSpacing(4)


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
            button.setIconSize(QSize(14,14))
            button.setToolTip("Window control")
            button.setFixedSize(QSize(40,32))
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
                # Fallback for platforms that do not support startSystemMove().
                self._drag_offset = (
                    event.globalPosition().toPoint()
                    - self.window().frameGeometry().topLeft()
                )
                event.accept()
                return
        super().mousePressEvent(event)


#code to customise the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Organiser") #name of window

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.title_bar = CustomTitleBar(self)


        page_names =["Clean", "Optimize", "History", "Settings"]


        self.naviwi = QWidget()
        self.naviwi.setObjectName("NavBar")
        self.naviwi.setFixedHeight(56)


        navila = QHBoxLayout(self.naviwi)
        navila.setContentsMargins(8,6,8,6)
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


        self.pages = QStackedWidget()


        self.button = QPushButton("Organise Directory")
        self.button.clicked.connect(self.button_clicked)

        clean_page = QWidget()
        cleanla = QVBoxLayout(clean_page)
        cleanla.addWidget(QLabel("File Organiser"))


        self.label = QLabel("choose a folder to start")
        cleanla.addWidget(self.button)

        self.pages.addWidget(clean_page)

        for name in page_names[1:]:
            page = QWidget()
            pagela = QVBoxLayout(page)
            pagela.addWidget(QLabel(f"{name} later"))
            self.pages.addWidget(page)

        self.nav_group.idClicked.connect(self.pages.setCurrentIndex)
        self.nav_group.button(0).setChecked(True)



        central_widget = QWidget()
        central_widget.setObjectName("Container")
        central_widget.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        central_widget.setStyleSheet(
            """#Container{
                    background: qlineargradient(x1:0 y1:0, x2:1 y2:1, stop:0 #051c2a stop:1 #44315f);
                    border-radius: 16px;
            }

            """
        )


        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(11, 11, 11, 11)
        content_layout.addWidget(QLabel("Hello world"))

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(self.title_bar)
        main_layout.addLayout(content_layout)

        self.setCentralWidget(central_widget)
        self.button = QPushButton("Organise Directory") #button with name that is checkable
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_clicked) #connects it to a signal when clicked
        self.button.clicked.connect(self.button_checked)
        self.resize(900, 600) #default size

        layout = QVBoxLayout()  #layout maker
        layout.addWidget(self.label)
        layout.addWidget(self.button)


        container = QWidget()
        container.setLayout(layout)


        #central widget is container
        self.setCentralWidget(container)

        #signals for context menu
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.contextMenuEvent)

    def button_clicked(self):
        ##organiser
        print("hello")
        #######mouse presses tracking
    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.RightButton:
            self.label.setText("left clicked")
        if e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("middle clicked")

    def button_checked(self, checked):
        button_status = checked
        print(button_status)
        #   ##makes the context menu with different actions
    def contextMenuEvent(self, pos):
        context= QMenu(self)



        context.addAction(QAction("test 1",self))
        context.addAction(QAction("test 2",self))
        context.addAction(QAction("test 3",self))
        context.exec(self.mapToGlobal(pos))

app= QApplication(sys.argv)
window= MainWindow() #creates the window and shows it
window.show()

#starts the app
app.exec()
