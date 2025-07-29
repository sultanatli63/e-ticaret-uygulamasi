from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget

class CategoriesPage(QWidget):
    def __init__(self, categories, on_category_selected):
        super().__init__()
        self.on_category_selected = on_category_selected
        self.init_ui(categories)

    def init_ui(self, categories):
        from PyQt5.QtWidgets import QListWidgetItem
        from PyQt5.QtGui import QFont
        layout = QVBoxLayout()
        title = QLabel('Kategoriler')
        title.setFont(QFont('Arial', 18, QFont.Bold))
        layout.addWidget(title)
        self.list_widget = QListWidget()
        for cat in categories:
            item = QListWidgetItem(cat)
            item.setFont(QFont('Arial', 14))
            self.list_widget.addItem(item)
        self.list_widget.itemClicked.connect(lambda item: self.on_category_selected(item.text()))
        self.list_widget.setStyleSheet('QListWidget { background: #f4f4f4; border-radius: 8px; } QListWidget::item { padding: 12px; margin: 4px; }')
        layout.addWidget(self.list_widget)
        self.setLayout(layout)
