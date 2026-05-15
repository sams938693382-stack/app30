# Online Shop System
# Python OOP loyiha

from datetime import datetime


class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def get_info(self):
        return f"{self.name} | {self.price}$ | Soni: {self.count}"

    def reduce_count(self, amount):
        if amount <= self.count:
            self.count -= amount
            return True
        return False


class User:
    def __init__(self, fullname, balance):
        self.fullname = fullname
        self.balance = balance
        self.cart = []

    def add_to_cart(self, product, amount):
        if product.reduce_count(amount):
            self.cart.append((product, amount))
            print(f"{product.name} savatga qo'shildi")
        else:
            print("Mahsulot yetarli emas")

    def show_cart(self):
        print(f"\n{self.fullname} savati:")
        total = 0

        for product, amount in self.cart:
            price = product.price * amount
            total += price
            print(f"{product.name} x {amount} = {price}$")

        print("Jami:", total, "$")

    def checkout(self):
        total = 0

        for product, amount in self.cart:
            total += product.price * amount

        if total <= self.balance:
            self.balance -= total
            print(f"\nTo'lov amalga oshdi")
            print("Qolgan balans:", self.balance, "$")
        else:
            print("\nBalans yetarli emas")


class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        print(f"\n=== {self.name} Mahsulotlari ===")

        for i, product in enumerate(self.products, start=1):
            print(f"{i}. {product.get_info()}")

    def search_product(self, name):
        print("\nQidiruv natijasi:")

        found = False

        for product in self.products:
            if name.lower() in product.name.lower():
                print(product.get_info())
                found = True

        if not found:
            print("Topilmadi")


class History:
    def __init__(self):
        self.logs = []

    def add_log(self, text):
        time = datetime.now().strftime("%H:%M:%S")
        self.logs.append(f"[{time}] {text}")

    def show_logs(self):
        print("\n=== History ===")

        for log in self.logs:
            print(log)


# Shop yaratish
shop = Shop("Tech Market")

# Mahsulotlar
p1 = Product("iPhone 15", 1200, 5)
p2 = Product("Samsung S24", 1000, 7)
p3 = Product("AirPods Pro", 300, 10)
p4 = Product("Gaming Mouse", 80, 15)
p5 = Product("Mechanical Keyboard", 150, 8)

# Shopga qo'shish
shop.add_product(p1)
shop.add_product(p2)
shop.add_product(p3)
shop.add_product(p4)
shop.add_product(p5)

# Mahsulotlarni chiqarish
shop.show_products()

# User
user1 = User("Xursandbek", 2500)

# Savatga qo'shish
user1.add_to_cart(p1, 1)
user1.add_to_cart(p3, 2)
user1.add_to_cart(p4, 1)

# Savatni ko'rish
user1.show_cart()

# To'lov
user1.checkout()

# History
history = History()

history.add_log("Xursandbek iPhone 15 sotib oldi")
history.add_log("Xursandbek AirPods Pro sotib oldi")

history.show_logs()

# Mahsulot qidirish
shop.search_product("iPhone")

# Eng qimmat mahsulot
expensive = max(shop.products, key=lambda x: x.price)

print("\nEng qimmat mahsulot:")
print(expensive.get_info())

# Eng arzon mahsulot
cheap = min(shop.products, key=lambda x: x.price)

print("\nEng arzon mahsulot:")
print(cheap.get_info())

# Jami mahsulot soni
total_products = 0

for product in shop.products:
    total_products += product.count

print("\nOmbordagi jami mahsulot:", total_products)

# Narxlar yig'indisi
total_price = 0

for product in shop.products:
    total_price += product.price

average = total_price / len(shop.products)

print("O'rtacha narx:", average)

# Qimmat mahsulotlar
print("\n=== 500$ dan qimmat mahsulotlar ===")

for product in shop.products:
    if product.price > 500:
        print(product.get_info())

# Kam qolgan mahsulotlar
print("\n=== Kam qolgan mahsulotlar ===")

for product in shop.products:
    if product.count < 6:
        print(product.get_info())

# Sana
now = datetime.now()

print("\nSana:", now.strftime("%d-%m-%Y"))
print("Vaqt:", now.strftime("%H:%M:%S"))

# Mahsulotlarni sort qilish
print("\n=== Narx bo'yicha saralash ===")

sorted_products = sorted(shop.products, key=lambda x: x.price)

for product in sorted_products:
    print(product.get_info())

# User ma'lumoti
print("\n=== User Info ===")
print("Ism:", user1.fullname)
print("Balans:", user1.balance)

# Bonus tizimi
bonus = 50
user1.balance += bonus

print("\nBonus qo'shildi:", bonus)
print("Yangi balans:", user1.balance)

# Dastur tugadi
print("\nDastur yakunlandi!")