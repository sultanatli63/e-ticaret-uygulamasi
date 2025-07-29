from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class LoginPage(QWidget):
    def __init__(self, on_login):
        super().__init__()
        self.on_login = on_login
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('Kullanıcı Adı')
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('Şifre')
        self.password_input.setEchoMode(QLineEdit.Password)
        login_btn = QPushButton('Giriş Yap')
        login_btn.clicked.connect(self.handle_login)
        layout.addWidget(QLabel('Giriş'))
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(login_btn)
        self.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if not username or not password:
            QMessageBox.warning(self, 'Hata', 'Kullanıcı adı ve şifre giriniz.')
            return
        self.on_login(username, password)
