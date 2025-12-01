students = []

def display_menu():
    print("\nSelect an Option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

def add_student():
    print("\nEnter student details:")

    student_id = input("Student ID: ")
    name = input("Name: ")

    while True:
        try:
            age = int(input("Age: "))
            if age <= 0:
                print("Age must be a positive number. Try again.")
                continue
            break
        except ValueError:
            print("Invalid age. Please enter a number.")

    grade = input("Grade: ")
    dob = input("Date of Birth (DD/MM/YYYY): ")

    subjects_input = input("Subjects (comma-separated): ")
    subjects = set(sub.strip() for sub in subjects_input.split(","))

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "grade": grade,
        "dob": dob,
        "subjects": subjects
    }

    students.append(student)
    print("\nStudent added successfully!")

def display_students():
    if not students:
        print("\nNo students available.")
        return

    print("\nDisplay All Students:")
    print("="*50)  
    for s in students:
        print(
            f"Student ID: {s['id']} | "
            f"Name: {s['name']} | "
            f"Age: {s['age']} | "
            f"Grade: {s['grade']} | "
            f"DOB: {s['dob']} | "
            f"Subjects: {', '.join(s['subjects'])}"
        )
    print("="*50)  

def update_student():
    student_id = input("\nEnter Student ID to Update: ")

    for s in students:
        if s["id"] == student_id:
            print("\nLeave blank to keep existing value.")

            new_age = input("New Age: ")
            new_subjects = input("New Subjects (comma-separated): ")

            if new_age.strip():
                try:
                    s["age"] = int(new_age)
                    if s["age"] <= 0:
                        print("Age must be a positive number. Keeping previous value.")
                except ValueError:
                    print("Invalid age. Keeping previous value.")

            if new_subjects.strip():
                s["subjects"] = set(sub.strip() for sub in new_subjects.split(","))

            print("\nStudent updated successfully!")
            return

    print("Student not found!")

def delete_student():
    student_id = input("\nEnter Student ID to Delete: ")

    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            print("\nStudent deleted successfully!")
            return

    print("Student not found!")

def display_subjects_offered():
    all_subjects = set()
    for s in students:
        all_subjects.update(s["subjects"])

    if all_subjects:
        print("\nUnique Subjects Offered:")
        print("="*50)  
        for sub in all_subjects:
            print("- ", sub)
        print("="*50) 
    else:
        print("\nNo subjects available.")


print("Welcome to the Student Data Organizer!")

while True:
    display_menu()
    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        display_subjects_offered()
    elif choice == "6":
        print("\nThank you for using the Student Data Organizer!")
        break
    else:
        print("Invalid choice. Please try again.")
