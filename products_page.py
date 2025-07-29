from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget

class ProductsPage(QWidget):
    def __init__(self, products, on_product_selected):
        super().__init__()
        self.on_product_selected = on_product_selected
        self.init_ui(products)

    def init_ui(self, products):
        from PyQt5.QtWidgets import QScrollArea, QWidget, QHBoxLayout, QPushButton
        from PyQt5.QtGui import QFont
        layout = QVBoxLayout()
        title = QLabel('Ürünler')
        title.setFont(QFont('Arial', 18, QFont.Bold))
        layout.addWidget(title)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        container = QWidget()
        grid = QHBoxLayout()
        for idx, product in enumerate(products):
            card = QWidget()
            card_layout = QVBoxLayout()
            name = QLabel(product.name)
            name.setFont(QFont('Arial', 14, QFont.Bold))
            price = QLabel(f"{product.price} TL")
            price.setFont(QFont('Arial', 12))
            desc = QLabel(product.description)
            desc.setWordWrap(True)
            detail_btn = QPushButton('Detay')
            detail_btn.clicked.connect(lambda _, i=idx: self.on_product_selected(i))
            card_layout.addWidget(name)
            card_layout.addWidget(price)
            card_layout.addWidget(desc)
            card_layout.addWidget(detail_btn)
            card.setLayout(card_layout)
            card.setStyleSheet('QWidget { border: 1px solid #ccc; border-radius: 8px; padding: 12px; background: #f9f9f9; min-width: 200px; max-width: 220px; }')
            grid.addWidget(card)
        container.setLayout(grid)
        scroll.setWidget(container)
        layout.addWidget(scroll)
        self.setLayout(layout)
