# Library Book Borrowing System


class Book:


    # Constructor

    def __init__(self, book_id, title, author, available_copies):

        self.book_id = book_id

        self.title = title

        self.author = author

        self.available_copies = available_copies



    # Borrow Book

    def borrow_book(self):

        if self.available_copies > 0:

            self.available_copies -= 1

            print("Book Borrowed Successfully")

        else:

            print("Book Currently Unavailable")



    # Return Book

    def return_book(self):

        self.available_copies += 1

        print("Book Returned Successfully")



    # Display Availability

    def display_availability(self):

        print("\nBook ID :", self.book_id)

        print("Title :", self.title)

        print("Author :", self.author)

        print("Available Copies :", self.available_copies)



# Objects

book1 = Book(101, "Python Programming", "Guido", 2)



book1.display_availability()

book1.borrow_book()

book1.display_availability()

book1.borrow_book()

book1.display_availability()

book1.borrow_book()

book1.return_book()

book1.display_availability()