# Vehicle Rental System


class Vehicle:


    # Constructor
    def __init__(self, vehicle_id, vehicle_name, vehicle_type, price):

        self.vehicle_id = vehicle_id
        self.vehicle_name = vehicle_name
        self.vehicle_type = vehicle_type
        self.price = price



    # Calculate Rental

    def calculate_rental(self, days):

        total = self.price * days


        if days > 10:

            discount = total * 0.20


        elif days > 5:

            discount = total * 0.10


        else:

            discount = 0



        final_amount = total - discount


        return total, discount, final_amount



    # Display Vehicle Details

    def display_bill(self, days):

        total, discount, final = self.calculate_rental(days)


        print("\n------ RENTAL BILL ------")

        print("Vehicle ID :", self.vehicle_id)

        print("Vehicle Name :", self.vehicle_name)

        print("Vehicle Type :", self.vehicle_type)

        print("Rental Days :", days)

        print("Total Amount :", total)

        print("Discount :", discount)

        print("Final Amount :", final)




# Main Function

def main():


    vehicles = []


    vehicle1 = Vehicle(101, "Swift", "Car", 2000)

    vehicle2 = Vehicle(102, "Activa", "Bike", 500)



    vehicles.append(vehicle1)

    vehicles.append(vehicle2)



    print("Available Vehicles")

    for vehicle in vehicles:

        print(vehicle.vehicle_id, vehicle.vehicle_name)



    choice = int(input("\nEnter Vehicle ID : "))


    days = int(input("Enter Rental Days : "))



    for vehicle in vehicles:


        if vehicle.vehicle_id == choice:

            vehicle.display_bill(days)

            break


    else:

        print("Vehicle Not Available")



main()