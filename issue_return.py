from data import load_data, save_data
from datetime import date

# Issue book
def issue_book():
    books = load_data("books.json")
    students = load_data("students.json")
    issued = load_data("issued_books.json")

    student_id = input("Enter Student ID: ")
    book_id = input("Enter Book ID: ")

    student_found = False
    book_found = False
    student_name = ""

    for student in students:
        if student["student_id"] == student_id:
            student_found = True
            student_name = student["student_name"]

    if student_found == False:
        print("Student is not registered!")
        return

    student_count = 0

    for record in issued:
        if record["student_id"] == student_id:
            student_count = student_count + 1

    if student_count >= 3:
        print("Maximum 3 books can be issued to one student!")
        return

    for record in issued:
        if record["student_id"] == student_id and record["book_id"] == book_id:
            print("This book is already issued to this student!")
            return

    for book in books:
        if book["book_id"] == book_id:
            book_found = True

            if book["available_copies"] > 0:
                book["available_copies"] = book["available_copies"] - 1
                book["total_issued"] = book["total_issued"] + 1

                record = {
                    "student_id": student_id,
                    "student_name": student_name,
                    "book_id": book_id,
                    "issue_date": str(date.today())
                }

                issued.append(record)

                save_data("books.json", books)
                save_data("issued_books.json", issued)

                print("Book issued successfully!")
            else:
                print("Book is not available!")

            break

    if book_found == False:
        print("Book not found!")


#Display Issued Books
def display_issued_books():
    issued = load_data("issued_books.json")
    books = load_data("books.json")
    students = load_data("students.json")

    if len(issued) == 0:
        print("No books are currently issued!")

    else:
        print("\n----- ISSUED BOOKS -----")

        for record in issued:
            print("\nStudent ID:", record["student_id"])
            print("Student Name:", record["student_name"])
            print("Book ID:", record["book_id"])
            print("Issue Date:", record["issue_date"])

    print("\nTotal Registered Students:", len(students))

    highest = 0
    popular_book = "No book issued yet"

    for book in books:
        if book["total_issued"] > highest:
            highest = book["total_issued"]
            popular_book = book["book_name"]

    print("Most Frequently Issued Book:", popular_book)   


# Return a Book
def return_book():
    books = load_data("books.json")
    issued = load_data("issued_books.json")

    student_id = input("Enter Student ID: ")
    book_id = input("Enter Book ID: ")

    found = False

    for record in issued:
        if record["student_id"] == student_id and record["book_id"] == book_id:
            found = True

            for book in books:
                if book["book_id"] == book_id:
                    book["available_copies"] = book["available_copies"] + 1
                    break

            issued.remove(record)
            break

    if found == True:
        save_data("books.json", books)
        save_data("issued_books.json", issued)

        print("Book returned successfully!")

    else:
        print("Issue record not found!")


