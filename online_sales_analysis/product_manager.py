from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)
        print(f"Proizvod {product.name} je dodat u sistem.")

  
    def remove_product(self, name: str):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"Proizvod {name} je uklonjen iz sistema.")
                return
        print(f"Proizvod {name} nije pronađen.")


class Cart:
    def __init__(self):
        self.cart_items = []
    
    def add_to_cart(self, product: Product):
        self.cart_items.append(product)
        print(f"Proizvod {product.name} je dodat u korpu.")
    
    def total_cart_value(self):
        return sum(product.price for product in self.cart_items)
    
    def display_cart(self):
        if not self.cart_items:
            print("Korpa je prazna.")
        else:
            print("Sadržaj korpe:")
            for product in self.cart_items:
                product.display_info()

if __name__ == "__main__":
    pm = ProductManager()
    p1 = Product("Laptop", 75000, 10)
    p2 = Product("Sporet", 530000, 3)
    
    pm.add_product(p1)
    pm.add_product(p2)
    pm.display_products()
    pm.total_value()

    cart = Cart()
    
    for product in pm.products[:3]:
        cart.add_to_cart(product)
    
    cart.display_cart()
    print(f"Ukupna vrednost za naplatu: {cart.total_cart_value():.2f} RSD")