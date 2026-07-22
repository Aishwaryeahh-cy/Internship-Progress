# Online Shopping Cart

class Product:

    def __init__(self, product_id, product_name, price, quantity):

        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity


    # Calculate Item Total
    def item_total(self):

        return self.price * self.quantity


    # Display Product
    def display(self):

        print("----------------------------------")
        print("Product ID :", self.product_id)
        print("Product Name :", self.product_name)
        print("Price :", self.price)
        print("Quantity :", self.quantity)
        print("Item Total :", self.item_total())


# Main Function
def main():

    products = []

    n = int(input("Enter Number of Products : "))

    for i in range(n):

        print("\nEnter Product", i+1)

        pid = int(input("Product ID : "))
        pname = input("Product Name : ")
        price = float(input("Price : "))
        qty = int(input("Quantity : "))

        p = Product(pid, pname, price, qty)

        products.append(p)


    grand_total = 0

    print("\n========== INVOICE ==========")

    for product in products:

        product.display()

        grand_total += product.item_total()


    if grand_total > 5000:

        discount = grand_total * 0.15

    elif grand_total > 3000:

        discount = grand_total * 0.10

    else:

        discount = 0


    final_bill = grand_total - discount


    print("\nGrand Total :", grand_total)
    print("Discount :", discount)
    print("Final Bill :", final_bill)


main()