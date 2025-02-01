from product_manager import ProductManager
from product import Product

if __name__ == "__main__":
    productM = ProductManager()

    productM.add_product(Product("Televizor", 90000, 4))
    productM.add_product(Product("Laptop", 75000, 3))
    productM.add_product(Product("Telefon", 50000, 7))
    productM.add_product(Product("Tablet", 30000, 5))

    print("\nSpisak dostupnih proizvoda:")
    productM.display_product()

    print("\nUkupna vrednost inventara:")
    productM.total_value()