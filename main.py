import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QMessageBox
from utils.database import Database
from ui.login_page import LoginPage
from ui.categories_page import CategoriesPage
from ui.products_page import ProductsPage
from ui.product_detail_page import ProductDetailPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('E-Ticaret Uygulaması')
        self.db = Database()
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.current_user = None
        self.cart = []
        self.init_login()

    def init_login(self):
        self.login_page = LoginPage(self.handle_login)
        self.stack.addWidget(self.login_page)
        self.stack.setCurrentWidget(self.login_page)

    def handle_login(self, username, password):
        user = self.db.get_user(username, password)
        if user:
            self.current_user = user
            self.show_categories()
        else:
            QMessageBox.warning(self, 'Hata', 'Geçersiz kullanıcı adı veya şifre.')

    def show_categories(self):
        categories = self.db.get_categories()
        self.categories_page = CategoriesPage(categories, self.show_products)
        self.stack.addWidget(self.categories_page)
        self.stack.setCurrentWidget(self.categories_page)

    def show_products(self, category):
        products = self.db.get_products_by_category(category)
        self.products_page = ProductsPage(products, lambda idx: self.show_product_detail(products[idx]))
        self.stack.addWidget(self.products_page)
        self.stack.setCurrentWidget(self.products_page)

    def show_product_detail(self, product):
        self.product_detail_page = ProductDetailPage(product, self.show_categories, self.add_to_cart)
        self.stack.addWidget(self.product_detail_page)
        self.stack.setCurrentWidget(self.product_detail_page)

    def add_to_cart(self, product):
        self.cart.append(product)
        QMessageBox.information(self, 'Sepet', f'{product.name} sepete eklendi!')

    def show_cart(self):
        from ui.cart_page import CartPage
        self.cart_page = CartPage(self.cart, self.show_categories, self.show_payment)
        self.stack.addWidget(self.cart_page)
        self.stack.setCurrentWidget(self.cart_page)

    def show_payment(self):
        from ui.payment_page import PaymentPage
        self.payment_page = PaymentPage(self.cart, self.payment_success, self.show_cart)
        self.stack.addWidget(self.payment_page)
        self.stack.setCurrentWidget(self.payment_page)

    def payment_success(self):
        self.cart.clear()
        QMessageBox.information(self, 'Başarılı', 'Siparişiniz alınmıştır!')
        self.show_categories()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    # Menüye sepet butonu ekle
    from PyQt5.QtWidgets import QAction
    cart_action = QAction('Sepet', window)
    cart_action.triggered.connect(window.show_cart)
    window.menuBar().addAction(cart_action)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
