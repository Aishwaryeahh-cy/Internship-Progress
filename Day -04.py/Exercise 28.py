# Library Book Management System

class Book:

    # Constructor
    def __init__(self, book_id, title, author, copies):

        # Private variables (Encapsulation)
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__copies = copies


    # Issue Book
    def issue_book(self):

        if self.__copies > 0:

            self.__copies -= 1

            print("Book Issued Successfully")

        else:

            print("Book Not Available")


    # Return Book
    def return_book(self):

        self.__copies += 1

        print("Book Returned Successfully")


    # Display Book Details
    def display_book(self):

        print("\n------ BOOK DETAILS ------")
        print("Book ID :", self.__book_id)
        print("Title :", self.__title)
        print("Author :", self.__author)
        print("Available Copies :", self.__copies)


# Main Function
def main():

    book_id = int(input("Enter Book ID : "))
    title = input("Enter Title : ")
    author = input("Enter Author : ")
    copies = int(input("Enter Available Copies : "))

    book = Book(book_id, title, author, copies)

    while True:

        print("\n1. Issue Book")
        print("2. Return Book")
        print("3. Display Book Details")
        print("4. Exit")

        choice = int(input("Enter Choice : "))

        if choice == 1:
            book.issue_book()

        elif choice == 2:
            book.return_book()

        elif choice == 3:
            book.display_book()

        elif choice == 4:
            print("Thank You")
            break

        else:
            print("Invalid Choice")


main()