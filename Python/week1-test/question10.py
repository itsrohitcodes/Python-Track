# ========================================
# LibraryBook Class
# ========================================

# This class represents one book in the library.
class LibraryBook:

    # ----------------------------------------
    # Create a new book
    # ----------------------------------------

    def __init__(self, title, author, price):

        # Store the book title
        self.title = title

        # Store the author's name
        self.author = author

        # Store the price of the book
        self.price = price

        # When a new book is created,
        # we assume that it is available
        self.is_available = True


    # ----------------------------------------
    # Borrow the book
    # ----------------------------------------

    def borrow_book(self):

        # Check if the book is currently available
        if self.is_available:

            # Change the status to unavailable
            # because someone borrowed the book
            self.is_available = False

            return "Book borrowed successfully."

        else:

            # The book is already borrowed
            return "Book is already borrowed."


    # ----------------------------------------
    # Return the book
    # ----------------------------------------

    def return_book(self):

        # Check if the book is currently borrowed
        if not self.is_available:

            # Change the status back to available
            self.is_available = True

            return "Book returned successfully."

        else:

            # The book was already available
            return "Book is already available."


    # ----------------------------------------
    # Display book information
    # ----------------------------------------

    def __str__(self):

        # Decide which text should be displayed
        # based on the availability of the book
        if self.is_available:
            status = "Available"
        else:
            status = "Borrowed"

        # Return all book information
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Price: ₹{self.price}\n"
            f"Status: {status}"
        )


# ========================================
# LibraryManager Class
# ========================================

# This class manages all the books
# inside the library.
class LibraryManager:

    # ----------------------------------------
    # Create a new library
    # ----------------------------------------

    def __init__(self):

        # Create an empty list
        # to store LibraryBook objects
        self.books = []


    # ----------------------------------------
    # Add a book to the library
    # ----------------------------------------

    def add_book(self, book):

        # Add the book object to the books list
        self.books.append(book)


    # ----------------------------------------
    # Display all books
    # ----------------------------------------

    def display_books(self):

        # Check if there are no books
        if not self.books:

            print("No books in the library.")

            # Stop this method here
            return


        # Go through every book in the library
        for book in self.books:

            # Print the book information
            # __str__() is called automatically
            print(book)

            # Print an empty line
            # to make the output easier to read
            print()


    # ----------------------------------------
    # Search for a book by title
    # ----------------------------------------

    def search_by_title(self, title):

        # Check every book in the library
        for book in self.books:

            # Convert both titles to lowercase
            # so the search is not case-sensitive
            if book.title.lower() == title.lower():

                # Return the book if we find it
                return book


        # If the loop finishes without finding
        # the book, return None
        return None


    # ----------------------------------------
    # Count available and borrowed books
    # ----------------------------------------

    def count_books(self):

        # Start both counters at zero
        available = 0
        borrowed = 0


        # Check every book in the library
        for book in self.books:

            # If the book is available
            if book.is_available:

                # Increase available count
                available += 1

            else:

                # Otherwise, increase borrowed count
                borrowed += 1


        # Return both counts
        return available, borrowed


# ========================================
# Create some books
# ========================================

# Create the first book
book1 = LibraryBook(
    "Python",
    "Rohit",
    500
)

# Create the second book
book2 = LibraryBook(
    "Java",
    "Salman",
    600
)

# Create the third book
book3 = LibraryBook(
    "SQL",
    "Vinay",
    400
)


# ========================================
# Create the library
# ========================================

# Create a LibraryManager object
library = LibraryManager()


# Add all three books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


# ========================================
# Display all books
# ========================================

print("----- All Books -----")

library.display_books()


# ========================================
# Search for a book
# ========================================

# Ask the user for a book title
title = input("Enter book title: ").strip()


# Search for the book
book = library.search_by_title(title)


# Check whether the book was found
if book:

    print("\n----- Book Found -----")

    # Display the book information
    print(book)


    # Ask the user if they want to borrow it
    choice = input(
        "\nDo you want to borrow this book? "
    ).strip().lower()


    # If the user says yes
    if choice == "yes":

        # Try to borrow the book
        print(book.borrow_book())

        print()

        # Display the updated book information
        print(book)

else:

    # The book was not found
    print("Book not found.")


# ========================================
# Display library statistics
# ========================================

# Get the number of available and borrowed books
available, borrowed = library.count_books()


print("\n----- Library Statistics -----")

print("Available Books:", available)

print("Borrowed Books:", borrowed)
