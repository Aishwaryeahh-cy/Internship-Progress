# Online Food Delivery System using OOP


# Parent Class
class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def login(self):
        print(self.name, "logged in successfully")


# Inheritance
class Customer(User):

    def __init__(self, name, email, address):
        super().__init__(name, email)
        self.address = address
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)
        print("Order placed successfully")


# Restaurant Class
class Restaurant:

    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_menu_item(self, item):
        self.menu.append(item)

    def show_menu(self):
        print("Menu of", self.name)

        for item in self.menu:
            item.display()


# Menu Item Class
class MenuItem:

    def __init__(self, item_name, price):
        self.item_name = item_name
        self.price = price

    def display(self):
        print(self.item_name, "-", self.price)


# Order Class
class Order:

    def __init__(self):

        # Encapsulation
        self.__items = []

        self.status = "Placed"


    # Composition
    def add_item(self, item):
        self.__items.append(item)


    def cancel_order(self):

        if self.status == "Placed":
            self.status = "Cancelled"
            print("Order cancelled")

        else:
            print("Cannot cancel order")


    def calculate_bill(self, coupon=None):

        total = 0

        for item in self.__items:
            total += item.price


        # Discount
        if coupon == "SAVE10":
            discount = total * 0.10
        else:
            discount = 0


        after_discount = total - discount


        # GST
        gst = after_discount * 0.05


        # Delivery charge
        delivery_charge = 40


        final_amount = after_discount + gst + delivery_charge


        print("\n------ BILL ------")
        print("Food Amount :", total)
        print("Discount :", discount)
        print("GST :", gst)
        print("Delivery :", delivery_charge)
        print("Final Amount :", final_amount)


        return final_amount



# Payment Parent Class
class Payment:


    def pay(self, amount):
        pass



# Polymorphism

class UPI(Payment):

    def pay(self, amount):
        print("Paid", amount, "using UPI")


class Card(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Card")


class Cash(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Cash")



# ---------------- MAIN PROGRAM ----------------


# Customer Registration
customer1 = Customer(
    "Aish",
    "aiisdhdjjks@gmail.com",
    "Bangalore"
)


customer1.login()



# Restaurant
restaurant1 = Restaurant("Food Palace")


# Adding menu items

pizza = MenuItem("Pizza", 250)

burger = MenuItem("Burger", 120)

juice = MenuItem("Juice", 60)


restaurant1.add_menu_item(pizza)
restaurant1.add_menu_item(burger)
restaurant1.add_menu_item(juice)


restaurant1.show_menu()



# Customer creates order

order1 = Order()


order1.add_item(pizza)
order1.add_item(burger)


customer1.place_order(order1)



# Generate bill

amount = order1.calculate_bill("SAVE10")



# Payment

payment = UPI()

payment.pay(amount)



# Cancel order example

order1.cancel_order()