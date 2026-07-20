# Food Delivery Order System

class Order:

    # Constructor
    def __init__(self, customer_name, food_item, quantity, price):

        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price


    # Calculate Bill
    def calculate_bill(self):

        total = self.quantity * self.price

        if total > 800:

            delivery_charge = 0

            print("Eligible for Free Delivery")

        else:

            delivery_charge = 60

            print("Delivery Charge Applied")

        final_bill = total + delivery_charge

        print("\n------ BILL ------")
        print("Customer :", self.customer_name)
        print("Food Item :", self.food_item)
        print("Quantity :", self.quantity)
        print("Food Amount :", total)
        print("Delivery Charge :", delivery_charge)
        print("Final Bill :", final_bill)



# Object

order1 = Order("Anfer", "Pizza", 3, 300)

order1.calculate_bill()