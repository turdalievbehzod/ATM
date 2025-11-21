class Product:
    def __init__(self, title, price, year):
        self.title = title
        self.price = price
        self.year = year
        self.type = "product"


class Water(Product):
    def __init__(self, title, price, year):
        super().__init__(title, price, year)
        self.type = "water"


class Food(Product):
    def __init__(self, title, price, year):
        super().__init__(title, price, year)
        self.type = "food"


class Spice(Product):
    def __init__(self, title, price, year):
        super().__init__(title, price, year)
        self.type = "spice"


class Shop:
    def __init__(self, title, phone):
        self.title = title
        self.phone = phone
        self.base = []
        self.base_water = []
        self.base_food = []
        self.base_spice = []

    def create_product(self, cls):
        title = input("Enter title: ")
        price = input("Enter price: ")
        year = input("Enter year: ")
        return cls(title, price, year)

    def add_water(self):
        p = self.create_product(Water)
        self.base.append(p)
        self.base_water.append(p)

    def add_food(self):
        p = self.create_product(Food)
        self.base.append(p)
        self.base_food.append(p)

    def add_spice(self):
        p = self.create_product(Spice)
        self.base.append(p)
        self.base_spice.append(p)

    def view_all(self):
        for item in self.base:
            print(f"Title: {item.title} Price: {item.price} Year: {item.year} Type: {item.type}")

    def view_category(self):
        choice = input("1. Water\n2. Food\n3. Spice\n4. Back\nChoose category: ")
        if choice == "1":
            base = self.base_water
        elif choice == "2":
            base = self.base_food
        elif choice == "3":
            base = self.base_spice
        else:
            return

        for item in base:
            print(f"Title: {item.title} Price: {item.price} Year: {item.year} Type: {item.type}")

    def edit_product(self):
        name = input("Enter the name of the product you want to edit: ")

        for item in self.base:
            if item.title == name:
                print(f"What would you like to edit? \n 1. Title \n 2. Price")
                choice = input("Choose option: ")

                if choice == "1":
                    item.title = input("Enter new title: ")
                    print("Title updated successfully.")
                elif choice == "2":
                    item.price = input("Enter new price: ")
                    print("Price updated successfully.")
                return

        print("Product not found.")

    def delete_product(self):
        name = input("Enter the name of the product you want to delete: ")

        for item in self.base:
            if item.title == name:
                self.base.remove(item)

                if item.type == "water":
                    self.base_water.remove(item)
                elif item.type == "food":
                    self.base_food.remove(item)
                elif item.type == "spice":
                    self.base_spice.remove(item)

                print("Product deleted successfully.")
                return

        print("Product not found.")


shop1 = Shop("Shop 1", 998997774433)


def shop_manager(shop: Shop):
    while True:
        code = input(
            "1. Add water\n 2. Add food\n 3. Add spice\n 4. View all\n 5. View category\n 6. Edit product\n 7. Delete product\n 8. Exit\n Choose action: ")

        if code == "1":
            shop.add_water()
        elif code == "2":
            shop.add_food()
        elif code == "3":
            shop.add_spice()
        elif code == "4":
            shop.view_all()
        elif code == "5":
            shop.view_category()
        elif code == "6":
            shop.edit_product()
        elif code == "7":
            shop.delete_product()
        elif code == "8":
            print("Exit")
            break


shop_manager(shop1)
