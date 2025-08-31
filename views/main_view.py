from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class MainView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple MVC Example")
        self.layout = QVBoxLayout()
        self.label = QLabel("Count: 0")
        self.button = QPushButton("Increment")
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)