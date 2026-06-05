students = []

# Load data from file
def load_data():
    global students
    students = []

    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, roll = line.strip().split(",")
                students.append({"name": name, "roll": roll})
    except FileNotFoundError:
        pass


# Save data to file
def save_data():
    with open("students.txt", "w") as file:
        for student in students:
            file.write(f"{student['name']},{student['roll']}\n")


load_data()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search by Roll Number")
    print("4. Search by Name")
    print("5. Delete Student")
    print("6. Update Student")
    print("7. Total Students")
    print("8. Exit")

    choice = input("Enter your choice: ")

    # ADD STUDENT
    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")

        exists = False

        for student in students:
            if student["roll"] == roll:
                exists = True
                break

        if exists:
            print("Roll number already exists ❌")
        else:
            students.append({"name": name, "roll": roll})
            save_data()
            print("Student added successfully ✔")

    # VIEW STUDENTS
    elif choice == "2":

        if len(students) == 0:
            print("No students found ❌")

        else:
            print("\n--- Student List ---")

            for student in students:
                print("-" * 30)
                print("Name :", student["name"])
                print("Roll :", student["roll"])

            print("-" * 30)

    # SEARCH BY ROLL
    elif choice == "3":

        roll = input("Enter roll number: ")
        found = False

        for student in students:
            if student["roll"] == roll:
                print("\nStudent Found ✔")
                print("Name :", student["name"])
                print("Roll :", student["roll"])
                found = True
                break

        if not found:
            print("Student not found ❌")

    # SEARCH BY NAME
    elif choice == "4":

        name = input("Enter student name: ")
        found = False

        for student in students:
            if student["name"].lower() == name.lower():
                print("\nStudent Found ✔")
                print("Name :", student["name"])
                print("Roll :", student["roll"])
                found = True

        if not found:
            print("Student not found ❌")

    # DELETE STUDENT
    elif choice == "5":

        roll = input("Enter roll number to delete: ")
        found = False

        for student in students:
            if student["roll"] == roll:
                students.remove(student)
                save_data()
                print("Student deleted successfully ✔")
                found = True
                break

        if not found:
            print("Student not found ❌")

    # UPDATE STUDENT
    elif choice == "6":

        roll = input("Enter roll number to update: ")
        found = False

        for student in students:
            if student["roll"] == roll:

                new_name = input("Enter new name: ")
                new_roll = input("Enter new roll number: ")

                student["name"] = new_name
                student["roll"] = new_roll

                save_data()

                print("Student updated successfully ✔")
                found = True
                break

        if not found:
            print("Student not found ❌")

    # TOTAL STUDENTS
    elif choice == "7":

        print("Total Students:", len(students))

    # EXIT
    elif choice == "8":

        print("Exiting...")
        break

    else:
        print("Invalid choice ❌")