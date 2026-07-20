class ShoppingCart:


    # Constructor

    def __init__(self, customer_name, product_name, quantity, price):

        self.customer_name = customer_name
        self.product_name = product_name
        self.quantity = quantity
        self.price = price



    # Calculate bill

    def calculate_bill(self):

        total_amount = self.quantity * self.price


        discount = 0


        if total_amount > 10000:

            discount = total_amount * 0.20


        elif total_amount > 5000:

            discount = total_amount * 0.10


        else:

            discount = 0



        final_amount = total_amount - discount


        return total_amount, discount, final_amount



    # Display bill

    def display_bill(self):

        total, discount, final = self.calculate_bill()


        print("\n------ BILL ------")

        print("Customer Name :", self.customer_name)

        print("Product Name :", self.product_name)

        print("Quantity :", self.quantity)

        print("Price per item :", self.price)

        print("Total Amount :", total)

        print("Discount :", discount)

        print("Final Amount :", final)




# Creating Objects


cart1 = ShoppingCart(
    "Anusha",
    "Laptop",
    1,
    60000
)


cart2 = ShoppingCart(
    "Rahul",
    "Mobile",
    1,
    8000
)



# Calling methods

cart1.display_bill()

cart2.display_bill()