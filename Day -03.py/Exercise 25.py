# Inventory Management System


class Product:


    def __init__(self, product_id, product_name, quantity, minimum_stock):

        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.minimum_stock = minimum_stock



    def sell_product(self, qty):

        if qty <= self.quantity:

            self.quantity -= qty

            print("Product Sold Successfully")

        else:

            print("Insufficient Stock")



    def restock_product(self, qty):

        self.quantity += qty

        print("Stock Updated Successfully")



    def check_stock(self):

        print("\nCurrent Stock :", self.quantity)

        if self.quantity == 0:

            print("Out of Stock")

        elif self.quantity <= self.minimum_stock:

            print("Low Stock")

        else:

            print("Stock Available")



# Object

product1 = Product(101, "Laptop", 20, 5)


while True:

    print("\n1. Sell Product")
    print("2. Restock Product")
    print("3. Check Stock")
    print("4. Exit")


    choice = int(input("Enter Choice : "))


    if choice == 1:

        qty = int(input("Enter Quantity to Sell : "))

        product1.sell_product(qty)


    elif choice == 2:

        qty = int(input("Enter Quantity to Restock : "))

        product1.restock_product(qty)


    elif choice == 3:

        product1.check_stock()


    elif choice == 4:

        print("Program Ended")

        break

    else:

        print("Invalid Choice")