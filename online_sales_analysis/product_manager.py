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


if __name__ == "__main__":
    pm = ProductManager()
    p1 = Product("Laptop", 75000, 10)
    p2 = Product("Sporet", 530000, 3)
    
    pm.add_product(p1)
    pm.add_product(p2)
    pm.display_products()
    pm.total_value()
