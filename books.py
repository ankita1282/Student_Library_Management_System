from data import load_data,save_data

# Add new book
def add_book():
    books = load_data("books.json")

    book_id = input("Enter Book ID: ")

    for book in books:
        if book["book_id"] == book_id:
            print("Book ID already exists!")
            return

    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    category = input("Enter Category: ")

    try:
        copies = int(input("Enter Number of Copies: "))
    except ValueError:
        print("Enter a valid number!")
        return

    if copies <= 0:
        print("Copies must be greater than zero!")
        return

    book = {
        "book_id": book_id,
        "book_name": name,
        "author": author,
        "category": category,
        "available_copies": copies,
        "total_issued": 0
    }

    books.append(book)
    save_data("books.json", books)

    print("Book added successfully!")


# Display all books
def display_books():
    books = load_data("books.json")
    issued = load_data("issued_books.json")
    students = load_data("students.json")

    if len(books) == 0:
        print("No books available!")
        return

    # Arrange books alphabetically
    for i in range(len(books)):
        for j in range(i + 1, len(books)):
            if books[i]["book_name"].lower() > books[j]["book_name"].lower():
                temp = books[i]
                books[i] = books[j]
                books[j] = temp

    total_copies = 0

    print("\n----- ALL BOOKS -----")

    for book in books:
        total = book["available_copies"] + book["total_issued"]
        total_copies = total_copies + total

        print("\nBook ID:", book["book_id"])
        print("Book Name:", book["book_name"])
        print("Author:", book["author"])
        print("Category:", book["category"])
        print("Total Copies:", total)
        print("Available Copies:", book["available_copies"])

    print("\nTotal Book Titles:", len(books))
    print("Total Copies in Library:", total_copies)
    print("Total Registered Students:", len(students))

    # Most frequently issued book
    highest = 0
    popular_book = "No book issued yet"

    for book in books:
        if book["total_issued"] > highest:
            highest = book["total_issued"]
            popular_book = book["book_name"]

    print("Most Frequently Issued Book:", popular_book)

    save_data("books.json", books)


# Search book
def search_book():
    books = load_data("books.json")

    search = input("Enter Book ID, Name or Author: ").lower()
    found = False

    for book in books:
        if (search == book["book_id"].lower() or
            search in book["book_name"].lower() or
            search in book["author"].lower()):

            print("\nBook Found!")
            print("Book ID:", book["book_id"])
            print("Name:", book["book_name"])
            print("Author:", book["author"])
            print("Category:", book["category"])
            print("Available Copies:", book["available_copies"])

            found = True

    if found == False:
        print("Book not found!")

#Delete a Book

def delete_book():
    books = load_data("books.json")
    issued = load_data("issued_books.json")

    book_id = input("Enter Book ID to delete: ")

    for record in issued:
        if record["book_id"] == book_id:
            print("Cannot delete! Book is currently issued.")
            return

    for book in books:
        if book["book_id"] == book_id:
            books.remove(book)
            save_data("books.json", books)

            print("Book deleted successfully!")
            return

    print("Book not found!")