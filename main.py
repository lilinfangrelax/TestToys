from PySide6.QtWidgets import QApplication
from models.counter_model import CounterModel
from views.main_view import MainView
from controllers.main_controller import MainController
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = CounterModel()
    view = MainView()
    controller = MainController(model, view)
    view.show()
    sys.exit(app.exec())