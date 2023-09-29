# Initialize an empty dictionary to store student records
student_records = {}

# Function to add a new student record
def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")

    # Check if the student ID already exists
    if student_id in student_records:
        print("Student ID already exists. Use 'Update Student' option to modify.")
    else:
        student_records[student_id] = {"Name": name, "Grade": grade}
        print("Student record added successfully.")

# Function to view all student records
def view_students():
    if not student_records:
        print("No student records available.")
    else:
        print("Student Records:")
        for student_id, info in student_records.items():
            print(f"ID: {student_id}, Name: {info['Name']}, Grade: {info['Grade']}")

# Function to update a student record
def update_student():
    student_id = input("Enter student ID to update: ")
    if student_id in student_records:
        name = input(f"Enter new name for student {student_id}: ")
        grade = input(f"Enter new grade for student {student_id}: ")
        student_records[student_id] = {"Name": name, "Grade": grade}
        print("Student record updated successfully.")
    else:
        print("Student ID not found. Use 'Add Student' option to add a new student.")

# Function to delete a student record
def delete_student():
    student_id = input("Enter student ID to delete: ")
    if student_id in student_records:
        del student_records[student_id]
        print("Student record deleted successfully.")
    else:
        print("Student ID not found. Use 'View Students' option to see the available IDs.")

# Main menu and user interaction
while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
# <Student Management> by Moutasim Qazi
