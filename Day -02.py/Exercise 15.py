# ---------------- MOVIE CLASS ----------------

class Movie:

    def __init__(self, name, duration):

        self.name = name
        self.duration = duration



# ---------------- SEAT CLASS ----------------

class Seat:

    def __init__(self, seat_number):

        self.seat_number = seat_number

        # Encapsulation
        self.__is_booked = False



    def book_seat(self):

        if self.__is_booked:

            raise Exception(
                "Seat already booked"
            )

        self.__is_booked = True



    def cancel_seat(self):

        self.__is_booked = False



    def is_available(self):

        return not self.__is_booked



# ---------------- SCREEN CLASS ----------------

class Screen:


    def __init__(self, screen_number):

        self.screen_number = screen_number

        # Composition
        self.seats = []


        for i in range(1, 11):

            self.seats.append(
                Seat(i)
            )



    def display_available_seats(self):

        print("\nAvailable Seats:")


        for seat in self.seats:

            if seat.is_available():

                print(
                    seat.seat_number,
                    end=" "
                )

        print()



# ---------------- THEATER CLASS ----------------

class Theater:


    def __init__(self, name):

        self.name = name

        # Composition
        self.screens = []



    def add_screen(self, screen):

        self.screens.append(screen)



# ---------------- CUSTOMER CLASS ----------------

class Customer:


    def __init__(self, name, customer_type):

        self.name = name
        self.customer_type = customer_type



    # Polymorphism

    def discount(self):

        return 0



# Student Customer

class Student(Customer):


    def discount(self):

        return 20



# Senior Citizen Customer

class SeniorCitizen(Customer):


    def discount(self):

        return 30



# ---------------- PAYMENT CLASS ----------------

class Payment:


    def pay(self, amount):

        print(
            "Online payment successful : ₹",
            amount
        )



# ---------------- BOOKING CLASS ----------------

class Booking:


    def __init__(
        self,
        customer,
        movie,
        screen,
        seat,
        payment
    ):

        self.customer = customer
        self.movie = movie
        self.screen = screen
        self.seat = seat
        self.payment = payment



    def calculate_price(self):

        base_price = 200


        discount = (
            base_price *
            self.customer.discount()
            /100
        )


        final_price = (
            base_price -
            discount
        )


        return final_price



    def book_ticket(self):

        try:

            self.seat.book_seat()


            amount = (
                self.calculate_price()
            )


            self.payment.pay(
                amount
            )


            self.generate_ticket()


        except Exception as e:

            print(
                e
            )



    def cancel_ticket(self):

        self.seat.cancel_seat()

        print(
            "Ticket cancelled"
        )



    def generate_ticket(self):

        print("\n------ MOVIE TICKET ------")

        print(
            "Customer:",
            self.customer.name
        )

        print(
            "Movie:",
            self.movie.name
        )

        print(
            "Seat:",
            self.seat.seat_number
        )

        print(
            "Amount:",
            self.calculate_price()
        )



# ---------------- MAIN PROGRAM ----------------


# Add Movie

movie1 = Movie(
    "Avengers",
    "3 Hours"
)



# Create Theater

theater = Theater(
    "PVR Cinemas"
)



screen1 = Screen(1)


theater.add_screen(
    screen1
)



# Display Seats

screen1.display_available_seats()



# Create Customer

customer1 = Student(
    "Anusha",
    "Student"
)



# Payment

payment = Payment()



# Booking

booking1 = Booking(
    customer1,
    movie1,
    screen1,
    screen1.seats[2],
    payment
)


booking1.book_ticket()



# Display seats after booking

screen1.display_available_seats()



# Try double booking same seat

booking2 = Booking(
    Customer("Rahul","Normal"),
    movie1,
    screen1,
    screen1.seats[2],
    payment
)


booking2.book_ticket()



# Cancel Ticket

booking1.cancel_ticket()