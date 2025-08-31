class MainController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.button.clicked.connect(self.increment_count)
        self.update_view()

    def increment_count(self):
        self.model.increment()
        self.update_view()

    def update_view(self):
        count = self.model.get_count()
        self.view.label.setText(f"Count: {count}")