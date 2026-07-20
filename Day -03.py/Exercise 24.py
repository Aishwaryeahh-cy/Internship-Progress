# Electricity Bill Calculator


class ElectricityBill:


    def __init__(self, consumer_number, customer_name, units):

        self.consumer_number = consumer_number
        self.customer_name = customer_name
        self.units = units



    def calculate_bill(self):


        if self.units <= 100:

            total = self.units * 5


        elif self.units <= 200:

            total = (100 * 5) + ((self.units - 100) * 7)


        else:

            total = (100 * 5) + (100 * 7) + ((self.units - 200) * 10)



        if total > 5000:

            surcharge = total * 0.05

        else:

            surcharge = 0



        final_bill = total + surcharge



        print("\n------ ELECTRICITY BILL ------")

        print("Consumer Number :", self.consumer_number)

        print("Customer Name :", self.customer_name)

        print("Units Consumed :", self.units)

        print("Bill Amount :", total)

        print("Surcharge :", surcharge)

        print("Final Bill :", final_bill)



# Object

bill1 = ElectricityBill(101, "Amogha", 350)

bill1.calculate_bill()