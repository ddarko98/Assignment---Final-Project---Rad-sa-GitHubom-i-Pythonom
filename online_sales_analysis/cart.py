class Cart:
    def __init__(self):
        self.cart_items = []
    
    def add_to_cart(self, product: Product):
        """Dodaje proizvod u korpu."""
        self.cart_items.append(product)
        print(f"Proizvod {product.name} je dodat u korpu.")
    
    def total_cart_value(self):
        """Računa ukupnu vrednost korpe."""
        return sum(product.price for product in self.cart_items)
    
    def display_cart(self):
        """Prikazuje sadržaj korpe."""
        if not self.cart_items:
            print("Korpa je prazna.")
        else:
            print("Sadržaj korpe:")
            for product in self.cart_items:
                product.display_info()