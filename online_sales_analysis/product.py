class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Proizvod: {self.name}, Cena: {self.price:.2f} RSD, Količina: {self.quantity}")

    def update_quantity(self, amount: int):
        if self.quantity + amount < 0:
            print("Nedovoljna kolicina na stanju!")
        else:
            self.quantity += amount
            print(f"Nova kolicina proizvoda {self.name}: {self.quantity}")


if __name__ == "__main__":
    p = Product("Laptop", 75000, 10)
    p.display_info()
    p.update_quantity(-3)
    p.display_info()
