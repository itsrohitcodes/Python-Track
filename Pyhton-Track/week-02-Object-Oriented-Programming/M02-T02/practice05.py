# Count Created Library Book Objects

class LibraryBook:
    # Add the class variable here
    book_count = 0

    def __init__(self, title):
        self.title = title
        # Update the counter here
        LibraryBook.book_count += 1


n = int(input())

for _ in range(n):
    title = input().strip()
    LibraryBook(title)

print(f"Books Created: {LibraryBook.book_count}")