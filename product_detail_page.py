from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class ProductDetailPage(QWidget):
    def __init__(self, product, on_back, on_add_cart):
        super().__init__()
        self.product = product
        self.on_back = on_back
        self.on_add_cart = on_add_cart
        self.init_ui()

    def init_ui(self):
        from PyQt5.QtWidgets import QHBoxLayout, QPushButton
        from PyQt5.QtGui import QFont
        layout = QVBoxLayout()
        title = QLabel(self.product.name)
        title.setFont(QFont('Arial', 18, QFont.Bold))
        layout.addWidget(title)
        layout.addWidget(QLabel(f"Kategori: <b>{self.product.category}</b>"))
        price = QLabel(f"Fiyat: <span style='color:#27ae60;font-size:18px;'><b>{self.product.price} TL</b></span>")
        price.setTextFormat(1)  # RichText
        layout.addWidget(price)
        desc = QLabel(self.product.description)
        desc.setWordWrap(True)
        layout.addWidget(desc)
        btn_layout = QHBoxLayout()
        add_cart_btn = QPushButton('Sepete Ekle')
        fav_btn = QPushButton('Favorilere Ekle')
        back_btn = QPushButton('Geri Dön')
        add_cart_btn.clicked.connect(lambda: self.on_add_cart(self.product))
        back_btn.clicked.connect(self.on_back)
        btn_layout.addWidget(add_cart_btn)
        btn_layout.addWidget(fav_btn)
        btn_layout.addWidget(back_btn)
        layout.addLayout(btn_layout)
        self.setLayout(layout)
