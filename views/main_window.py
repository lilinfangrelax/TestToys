# views/main_window.py
from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 Demo")

        # UI 组件
        self.label = QLabel("Hello, PySide6!")
        self.button = QPushButton("Click Me")

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
