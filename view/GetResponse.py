from PySide6.QtWidgets import QWidget, QHBoxLayout, QTextEdit, QPushButton, QVBoxLayout, QTreeWidget, QLineEdit, QLabel
from PySide6.QtCore import QTimer
import os


class GetResponse(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._timer = QTimer(self)
        self._timer.setSingleShot(True)
        self._data_path = "./data"
        self.setup_ui()
        self.load_content()

    def setup_ui(self):
        # Left Area
        self.api_uri_input_textedit = QTextEdit()
        self.api_uri_input_textedit.setPlaceholderText("Please paste your apis here")

        # Center Area
        self._center_panel = QWidget()
        self._center_panel_layout = QVBoxLayout()
        self._center_panel.setLayout(self._center_panel_layout)
        # top panel
        self._center_top_panel = QWidget()
        self._center_top_panel_layout = QHBoxLayout()
        self._center_top_panel.setLayout(self._center_top_panel_layout)
        self._toggle_http_server = QPushButton("Start HTTP Server")
        self._open_extension_path = QPushButton("Open Extension Path")
        self._refresh = QPushButton("Refresh")
        self._refresh.setToolTip("Refresh the data in the below tree")
        self._data_count_label = QLabel("counts:")
        self._data_count_value = QLabel("0")
        self._center_top_panel_layout.addWidget(self._toggle_http_server)
        self._center_top_panel_layout.addWidget(self._open_extension_path)
        self._center_top_panel_layout.addWidget(self._refresh)
        self._center_top_panel_layout.addWidget(self._data_count_label)
        self._center_top_panel_layout.addWidget(self._data_count_value)
        # bottom panel
        self._center_bottom_tree = QTreeWidget()
        self._center_bottom_tree.setHeaderHidden(True)
        # add layout
        self._center_panel_layout.addWidget(self._center_top_panel)
        self._center_panel_layout.addWidget(self._center_bottom_tree)

        # Right Area
        self._right_panel = QWidget()
        self._right_panel_layout = QVBoxLayout()
        self._right_panel.setLayout(self._right_panel_layout)
        self._request_url = QLineEdit()
        self._request_url.setPlaceholderText("Request URL")
        self._request_method = QLineEdit()
        self._request_method.setPlaceholderText("Method")
        self._request_body = QTextEdit()
        self._request_body.setPlaceholderText("Request Body")
        self._response_body = QTextEdit()
        self._response_body.setPlaceholderText("Response Body")
        self._right_panel_layout.addWidget(self._request_url)
        self._right_panel_layout.addWidget(self._request_method)
        self._right_panel_layout.addWidget(self._request_body)
        self._right_panel_layout.addWidget(self._response_body)
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.api_uri_input_textedit)
        self.layout.addWidget(self._center_panel)
        self.layout.addWidget(self._right_panel)

        # Add Event
        self._toggle_http_server.clicked.connect(self._toggle_http_server_clicked)
        self._open_extension_path.clicked.connect(self._open_extension_path_clicked)
        self._refresh.clicked.connect(self._refresh_clicked)
        self.api_uri_input_textedit.textChanged.connect(self._api_uri_input_textedit_text_changed)

    def load_content(self):
        try:
            with open(f"{self._data_path}/api_uri_input.txt", "r") as f:
                self.api_uri_input_textedit.setText(f.read())
        except FileNotFoundError:
            pass

    def _toggle_http_server_clicked(self):
        print(self._toggle_http_server.text())
        if self._toggle_http_server.text() == "Start HTTP Server":
            self._toggle_http_server.setText("Stop HTTP Server")
        elif self._toggle_http_server.text() == "Stop HTTP Server":
            self._toggle_http_server.setText("Start HTTP Server")
        pass

    def _open_extension_path_clicked(self):
        os.startfile(f"{os.getcwd()}/chrome_extensions/GetResponse")

    def _refresh_clicked(self):
        pass

    def _api_uri_input_textedit_text_changed(self):
        """Automatically save user input"""
        self._timer.start(1000)
        self._timer.timeout.connect(self._delayed_save)

    def _delayed_save(self):
        if not os.path.exists(f"{self._data_path}/api_uri_input.txt"):
            os.makedirs(f"{self._data_path}")
        with open(f"{self._data_path}/api_uri_input.txt", "w") as f:
            f.write(self.api_uri_input_textedit.toPlainText())