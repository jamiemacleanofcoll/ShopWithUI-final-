from controllers.product_controller import ProductController
from models.order import Address, Order, CreditCard


class OrderController:
    cart: dict[dict[int, int]] = {}
    orders: dict[dict[int, Order]] = {}
    product_controller: ProductController

    def __init__(self, product_controller):
        self.product_controller = product_controller

    def add_to_cart(self, user_id, product_id, quantity):
        current_quantity = self.cart.get(user_id, {}).get(product_id, 0)
        new_quantity = current_quantity + quantity
        product = self.product_controller.get_product(product_id)
        if product is None:
            return False
        if product.stock >= new_quantity:
            if user_id not in self.cart:
                self.cart[user_id] = {}
            self.cart[user_id][product_id] = new_quantity
            return True
        else:
            return False

    def checkout(self, user_id, valid_month, valid_year, credit_card_owner, credit_card_number, credit_card_cvv,
                 first_name, last_name, street, number, zip_code, city):
        if len(self.cart.get(user_id, [])) == 0:
            return None
        address = Address(first_name, last_name, street, number, zip_code, city)
        credit_card = CreditCard(valid_month, valid_year, credit_card_owner, credit_card_number, credit_card_cvv)
        order = Order(address, credit_card, self.cart[user_id])
        for product_id, quantity in self.cart[user_id].items():
            self.product_controller.buy_product(product_id, quantity)
        if user_id not in self.orders:
            self.orders[user_id] = []
        self.orders[user_id].append(order)
        self.clear_cart(user_id)

    def clear_cart(self, user_id):
        self.cart[user_id] = {}
