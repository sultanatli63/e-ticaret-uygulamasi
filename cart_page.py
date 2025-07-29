from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton

class CartPage(QWidget):
    def __init__(self, cart, on_back, on_payment):
        super().__init__()
        self.cart = cart
        self.on_back = on_back
        self.on_payment = on_payment
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Sepetim'))
        self.list_widget = QListWidget()
        total = 0
        for product in self.cart:
            self.list_widget.addItem(f"{product.name} - {product.price} TL")
            total += float(product.price)
        layout.addWidget(self.list_widget)
        layout.addWidget(QLabel(f"Toplam: {total} TL"))
        pay_btn = QPushButton('Ödemeye Geç')
        pay_btn.clicked.connect(self.on_payment)
        back_btn = QPushButton('Alışverişe Devam Et')
        back_btn.clicked.connect(self.on_back)
        layout.addWidget(pay_btn)
        layout.addWidget(back_btn)
        self.setLayout(layout)
