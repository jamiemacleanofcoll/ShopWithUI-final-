from models.product import Product


class ProductController:
    products: list[Product] = [Product(1, "Dress", "Rib-knit dress", 29.97, 37, 100, "Clothes"),
                               Product(2, "Top", "Long-sleeved jersey top", 8.1, 10, 70, "Clothes"),
                               Product(3, "Cardigan", "Boxy-style cardigan", 32.4, 40, 85, "Clothes"),
                               Product(4, "Sweatshirt", "Oversized sweatshirt", 28.35, 35, 30, "Clothes"),
                               Product(5, "Shoes", "Knee-high boots", 56.7, 70, 92, "Clothes"),
                               Product(6, "Blazer", "Double-breasted blazer", 28.35, 35, 26, "Clothes"),
                               Product(7, "Trousers", "Tailored trousers", 32.4, 40, 18, "Clothes"),
                               Product(8, "Jeans", "Vintage Slim High Ankle Jeans", 44.55, 55, 48, "Clothes"),
                               Product(9, "Skirt", "Wrapover satin skirt", 12.15, 15, 93, "Clothes"),
                               Product(10, "Playsuit", "Drawstring playsuit", 10.53, 13, 35, "Clothes")]

    def __init__(self):
        pass

    def add_product(self, name, description, price_before_tax, price_after_tax, stock, category):
        product_id_list = [product.product_id for product in self.products]
        product_id = max(product_id_list, default=0) + 1
        self.products.append(Product(product_id, name, description, price_before_tax, price_after_tax, stock, category))

    def view_products(self):
        return self.products

    def get_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def buy_product(self, product_id, quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.stock -= quantity
                break
