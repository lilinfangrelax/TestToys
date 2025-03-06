from PySide6.QtWidgets import QMainWindow, QApplication, QTabWidget
import sys
from view.GetResponse import GetResponse


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("TestToys")
        self.resize(1200, 600)

        self._central_widget = QTabWidget(self)
        self.setCentralWidget(self._central_widget)

        self._central_widget.addTab(GetResponse(), "GetRespounse")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())