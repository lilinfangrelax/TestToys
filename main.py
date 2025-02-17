from PySide6 import QtCore, QtGui, QtWidgets
from thread.MqttClientThread import MqttClientThread

class TestToys(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TestToys")
        self.setWindowIcon(QtGui.QIcon("public/icon.png"))
        self.resize(400, 400)
        self.show()

        self.button_a = QtWidgets.QPushButton("A")
        self.button_b = QtWidgets.QPushButton("B")
        self.button_a.clicked.connect(self.click_a)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button_a)
        self.layout.addWidget(self.button_b)

        self.client_a_thread = MqttClientThread(self, "button_a")
        self.client_b_thread = MqttClientThread(self, "button_b")
        self.client_a_thread.client_started.connect(self.client_started)
        self.client_a_thread.client_stopped.connect(self.client_stopped)
        self.client_b_thread.client_started.connect(self.client_started)
        self.client_b_thread.client_stopped.connect(self.client_stopped)
        self.client_a_thread.start()
        self.client_b_thread.start()

    def client_started(self, message):
        print(f"Client Status: {message}")

    def client_stopped(self):
        print("Client Stauts: Stopped")

    def click_a(self):
        self.client_a_thread.publish("button/button_b", "{'test':'hello'}")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    test_toys = TestToys()
    app.exec()