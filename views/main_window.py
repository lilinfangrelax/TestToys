# views/main_window.py
from PySide6.QtWidgets import (QMainWindow, QPushButton, QLabel, QVBoxLayout, 
                               QWidget, QMenuBar, QHBoxLayout, QSizePolicy, QGridLayout,
                                QGraphicsDropShadowEffect )
from PySide6.QtGui import QAction, QMouseEvent, QPainter, QBrush, QColor, QPainterPath, QRegion
from PySide6.QtCore import Qt, QRect

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TestToys")
        self.setMinimumSize(1010, 600)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.set_rounded_corners(8)

        main_container = QWidget()

        main_layout = QVBoxLayout(main_container)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        self.setStyleSheet("background-color: #171D25; color: #CECECE;")

        self.top_bar = CustomTopBar(self)
        main_layout.addWidget(self.top_bar)

        self.central_content_widget = QWidget()
        temp_layout = QVBoxLayout(self.central_content_widget)
        qlabel = QLabel("Centeral Content Area")
        qlabel.setStyleSheet("font-size: 24px; background-color: #2D333C; color: #EEEEEE;")
        temp_layout.addWidget(qlabel)
        temp_layout.setContentsMargins(0,0,0,0)
        main_layout.addWidget(self.central_content_widget)

        main_layout.addWidget(CustomBottomBar(self))

        self.setCentralWidget(main_container)

    def set_rounded_corners(self, radius):
        rect = QRect(0, 0, self.width(), self.height())
        path = QPainterPath()
        path.addRoundedRect(rect, radius, radius)
        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)

class CustomTopBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent
        self.setFixedHeight(65)

        grid_layout = QGridLayout(self)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setSpacing(0)

        self._create_menu_bar()
        grid_layout.addWidget(self.menu_bar, 0, 0, Qt.AlignLeft | Qt.AlignTop)

        control_buttons_layout = QHBoxLayout()
        control_buttons_layout.setContentsMargins(0, 0, 5, 0)
        control_buttons_layout.setSpacing(5)
        self.minimize_button = QPushButton("-")
        self.maximize_restore_button = QPushButton("[]") 
        self.close_button = QPushButton("X")
        self.minimize_button.setFixedSize(25, 25)
        self.maximize_restore_button.setFixedSize(25, 25)
        self.close_button.setFixedSize(25, 25)
        self.minimize_button.clicked.connect(self.parent_window.showMinimized)
        self.maximize_restore_button.clicked.connect(self._toggle_maximize_restore)
        self.close_button.clicked.connect(self.parent_window.close)
        control_buttons_layout.addWidget(self.minimize_button)
        control_buttons_layout.addWidget(self.maximize_restore_button)
        control_buttons_layout.addWidget(self.close_button)

        grid_layout.addLayout(control_buttons_layout, 0, 1, Qt.AlignRight | Qt.AlignTop)

        self._create_navigation_bar()
        self.bottom_navigation_bar = QHBoxLayout()
        self.bottom_navigation_bar.setContentsMargins(0, 0, 0, 0)
        self.bottom_navigation_bar.addWidget(self.nav_bar)
        grid_layout.addLayout(self.bottom_navigation_bar, 1, 0, Qt.AlignLeft | Qt.AlignTop)

        self.start_pos = None
        self.window_pos = None

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.start_pos = event.globalPosition().toPoint()
            self.window_pos = self.parent_window.pos()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.LeftButton and self.start_pos:
            delta = event.globalPosition().toPoint() - self.start_pos
            self.parent_window.move(self.window_pos + delta)
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.start_pos = None
        self.window_pos = None
        event.accept()

    def _create_menu_bar(self):
        menu_bar = QMenuBar(self)

        testtoys_menu = menu_bar.addMenu("TestToys")
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.parent_window.close)
        testtoys_menu.addAction(exit_action)

        view_menu = menu_bar.addMenu("View")

        help_menu = menu_bar.addMenu("Help")
        about_action = QAction("About", self)
        help_menu.addAction(about_action)

        self.menu_bar = menu_bar

    def _create_navigation_bar(self):
        nav_bar = QWidget(self)
        nav_layout = QHBoxLayout(nav_bar)
        nav_layout.setContentsMargins(15, 0, 0, 0)
        nav_layout.setSpacing(18)

        buttons = ["<",">","MAIN", "LIBRARY", "COMMUNITY", "PROFILE"]
        for btn_text in buttons:
            btn = QPushButton(btn_text)
            btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            btn.setStyleSheet(
                """
                QPushButton {
                    color: #CECECE;
                    border: none;
                    font-size: 18px;
                }
                QPushButton:hover {
                    color: #EEEEEE;
                }
                QPushButton:pressed {
                    border-bottom: 4px solid #1AA2FF;
                    color: #1AA2FF;
                }
                """
            )
            btn.setContentsMargins(0,0,0,0)
            nav_layout.addWidget(btn)

        self.nav_bar = nav_bar

    def _toggle_maximize_restore(self):
        if self.parent_window.isMaximized():
            self.parent_window.showNormal()
            self.maximize_restore_button.setText("[]")
        else:
            self.parent_window.showMaximized()
            self.maximize_restore_button.setText("口")


class CustomBottomBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent
        self.setFixedHeight(50)
        self.setStyleSheet("background-color: #171D25;")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 0, 10, 0)

        self.start_pos = None
        self.window_pos = None

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.start_pos = event.globalPosition().toPoint()
            self.window_pos = self.parent_window.pos()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.LeftButton and self.start_pos:
            delta = event.globalPosition().toPoint() - self.start_pos
            self.parent_window.move(self.window_pos + delta)
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.start_pos = None
        self.window_pos = None
        event.accept()