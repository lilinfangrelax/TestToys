from PySide6.QtWidgets import QWidget, QHBoxLayout, QTextEdit, QPushButton, QVBoxLayout, QTreeWidget, QLineEdit, QLabel


class GetResponse(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setup_ui()

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
        self._toggle_http_server = QPushButton("Toggle HTTP Server")
        self._refresh = QPushButton("Refresh")
        self._data_count_label = QLabel("counts:")
        self._data_count_value = QLabel("0")
        self._center_top_panel_layout.addWidget(self._toggle_http_server)
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