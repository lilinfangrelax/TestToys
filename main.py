import sys

from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtCore import QSettings
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QDockWidget, QMainWindow, QListWidget, QTabWidget, QTextEdit, QFrame
from view.NodeSketchpad import *


class TestToys(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_node_sketchpad()

    def closeEvent(self, event):
        settings = QSettings("TestToys", "TestToys")
        settings.setValue('windowState', self.saveState())

    def setup_node_sketchpad(self):
        self.setWindowTitle("TestToys")
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowIcon(QtGui.QIcon("public/icon.png"))


        self.scene = NodeSketchpadScene()
        self.view = NodeSketchpadView(self.scene, self)
        self.center_tabs = QTabWidget()
        self.center_tabs.addTab(self.view, "Default")
        self.setCentralWidget(self.center_tabs)

        dock1 = QDockWidget("Browser", self)
        dock1_widget = QListWidget()
        dock1.setWidget(dock1_widget)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock1)

        dock2 = QDockWidget("Properties", self)
        dock2_widget = QListWidget()
        dock2.setWidget(dock2_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, dock2)

        dock3 = QDockWidget("Logger", self)
        dock3_widget = QTextEdit()
        dock3_widget.setReadOnly(True)
        dock3_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # Solve problem: there is a blue line in the bottom of QTextEdit
        # https://stackoverflow.com/questions/16436058/how-to-make-qtextedit-with-no-visible-border
        dock3_widget.setFrameStyle(QFrame.NoFrame)
        dock3.setWidget(dock3_widget)
        dock3.setMinimumHeight(150)
        self.addDockWidget(Qt.BottomDockWidgetArea, dock3)

        dock4 = QDockWidget("Result", self)
        web_view = QWebEngineView()
        web_view.setHtml('<a href="https://data.typeracer.com/pit/profile?user=hk_l&ref=badge" target="_top"><img src="https://data.typeracer.com/misc/badge?user=hk_l" border="0" alt="TypeRacer.com scorecard for user hk_l"/></a>')
        dock4.setWidget(web_view)
        dock4.setEnabled(False)
        self.addDockWidget(Qt.RightDockWidgetArea, dock4)

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
    app = QtWidgets.QApplication(sys.argv)
    test_toys = TestToys()
    # the companyName and appName is necessary to save DockWidget state, I don't know why.
    settings = QSettings("TestToys", "TestToys")
    state = settings.value('windowState')
    if state != None:
        test_toys.restoreState(state)
    app.exec()