import books
import students
import issue_return


# Main menu
def main():

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add New Book")
        print("2. Display All Books")
        print("3. Search for a Book")
        print("4. Register a Student")
        print("5. Issue a book")
        print("6. Return a book ")
        print("7. Display Issued books" )
        print("8. Delete a Book ")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
           books.add_book()

        elif choice == "2":
           books.display_books()

        elif choice == "3":
            books.search_book()

        elif choice == "4":
             students.register_student()

        elif choice == "5":
             issue_return.issue_book()  

        elif choice == "6":
             issue_return.return_book()        

        elif choice == "7":
            issue_return.display_issued_books()

        elif choice == "8":
            books.delete_book()
       
        elif choice == "9":
            print("Thank you for using Library Management System!")
            break

        else:
            print("Invalid choice!")

main()
