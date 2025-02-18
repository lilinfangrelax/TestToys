from PySide6 import QtCore, QtGui, QtWidgets
from thread.MqttClientThread import MqttClientThread
from view.NodeSketchpad import *


class TestToys(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_node_sketchpad()

    def setup_node_sketchpad(self):
        self.setWindowTitle("TestToys")
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowIcon(QtGui.QIcon("public/icon.png"))

        self.scene = NodeSketchpadScene()
        self.view = NodeSketchpadView(self.scene, self)

        self.layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.LeftToRight, self)
        self.layout.addWidget(self.view)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # self.button_a = QtWidgets.QPushButton("A")
        # self.button_b = QtWidgets.QPushButton("B")
        # self.button_a.clicked.connect(self.click_a)
        # self.layout.addWidget(self.button_a)
        # self.layout.addWidget(self.button_b)
        # self.client_a_thread = MqttClientThread(self, "button_a")
        # self.client_b_thread = MqttClientThread(self, "button_b")
        # self.client_a_thread.client_started.connect(self.client_started)
        # self.client_a_thread.client_stopped.connect(self.client_stopped)
        # self.client_b_thread.client_started.connect(self.client_started)
        # self.client_b_thread.client_stopped.connect(self.client_stopped)
        # self.client_a_thread.start()
        # self.client_b_thread.start()
        self.show()

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
