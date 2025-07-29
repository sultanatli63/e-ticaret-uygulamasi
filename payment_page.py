From PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class PaymentPage(QWidget):
    def __init__(self, cart, on_payment_success, on_back):
        super().__init__()
        self.cart = cart
        self.on_payment_success = on_payment_success
        self.on_back = on_back
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Ödeme Bilgileri'))
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText('Kart Üzerindeki İsim')
        self.card_input = QLineEdit()
        self.card_input.setPlaceholderText('Kart Numarası')
        self.card_input.setMaxLength(16)
        self.card_input.setInputMask('9999 9999 9999 9999;_')
        self.cvv_input = QLineEdit()
        self.cvv_input.setPlaceholderText('CVV')
        self.cvv_input.setMaxLength(3)
        self.cvv_input.setInputMask('999;_')
        pay_btn = QPushButton('Ödemeyi Tamamla')
        pay_btn.clicked.connect(self.handle_payment)
        back_btn = QPushButton('Geri Dön')
        back_btn.clicked.connect(self.on_back)
        layout.addWidget(self.name_input)
        layout.addWidget(self.card_input)
        layout.addWidget(self.cvv_input)
        layout.addWidget(pay_btn)
        layout.addWidget(back_btn)
        self.setLayout(layout)

    def handle_payment(self):
        if not self.name_input.text() or not self.card_input.text().replace(' ', '').isdigit() or not self.cvv_input.text().isdigit():
            QMessageBox.warning(self, 'Hata', 'Lütfen tüm ödeme bilgilerini doğru giriniz.')
            return
        QMessageBox.information(self, 'Başarılı', 'Ödeme başarıyla tamamlandı!')
        self.on_payment_success()
