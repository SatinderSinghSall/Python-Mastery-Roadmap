class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f"Price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total Products in Store: {Product.count}")


product1 = Product("Phone", 10000)
product2 = Product("Tab", 20000)
product3 = Product("TV", 30000)

print(product1.get_info())
print(product2.get_info())
print(product3.get_info())
