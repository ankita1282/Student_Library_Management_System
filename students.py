from data import load_data,save_data

# Register student
def register_student():
    students = load_data("students.json")

    student_id = input("Enter Student ID: ")

    for student in students:
        if student["student_id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ")
    department = input("Enter Department: ")
    contact = input("Enter Contact Number: ")

    student = {
        "student_id": student_id,
        "student_name": name,
        "department": department,
        "contact": contact
    }

    students.append(student)
    save_data("students.json", students)

    print("Student registered successfully!")
