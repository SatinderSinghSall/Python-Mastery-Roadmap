# Methods: Instance, Class & Static

class Laptop:
    storage_type = "SSD"

    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"Storage Type: {cls.storage_type}")

    def get_info(self):
        print(f"Laptop has {self.ram} RAM and {self.storage} {self.storage_type} storage.")

laptop1 = Laptop("16GB", "512GB")
laptop2 = Laptop("8GB", "256GB")

laptop1.get_info()
laptop2.get_info()

print(laptop1.get_storage_type())
print(laptop2.get_storage_type())
