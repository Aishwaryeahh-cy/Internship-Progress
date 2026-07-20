# Movie Ticket Booking

class MovieTicket:

    def __init__(self, customer_name, movie_name, tickets, ticket_price):

        self.customer_name = customer_name
        self.movie_name = movie_name
        self.tickets = tickets
        self.ticket_price = ticket_price


    def booking_summary(self):

        total = self.tickets * self.ticket_price

        if self.tickets >= 5:

            discount = total * 0.15

        elif self.tickets >= 3:

            discount = total * 0.10

        else:

            discount = 0


        final_bill = total - discount


        print("\n------ BOOKING SUMMARY ------")
        print("Customer :", self.customer_name)
        print("Movie :", self.movie_name)
        print("Tickets :", self.tickets)
        print("Total :", total)
        print("Discount :", discount)
        print("Final Bill :", final_bill)



# Object

ticket1 = MovieTicket("Rahul", "Leo", 5, 250)

ticket1.booking_summary()