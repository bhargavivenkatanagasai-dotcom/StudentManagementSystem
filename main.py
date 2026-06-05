students = []

# LOAD DATA
def load_data():
    global students
    students = []

    try:
        with open("students.txt", "r") as f:
            for line in f:
                name, roll = line.strip().split(",")
                students.append({"name": name, "roll": roll})
    except:
        pass


# SAVE DATA
def save_data():
    with open("students.txt", "w") as f:
        for s in students:
            f.write(s["name"] + "," + s["roll"] + "\n")


load_data()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # ADD STUDENT
    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")

        exists = False

        for s in students:
            if s["roll"] == roll:
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
        print("\n--- Student List ---")

        if len(students) == 0:
            print("No students found")
        else:
            for s in students:
                print(f"Name: {s['name']} | Roll: {s['roll']}")

    # SEARCH STUDENT
    elif choice == "3":
        roll = input("Enter roll number to search: ")

        found = False

        for s in students:
            if s["roll"] == roll:
                print(f"Found ✔ Name: {s['name']} | Roll: {s['roll']}")
                found = True
                break

        if not found:
            print("Student not found ❌")

    # DELETE STUDENT
    elif choice == "4":
        roll = input("Enter roll number to delete: ")

        found = False

        for s in students:
            if s["roll"] == roll:
                students.remove(s)
                save_data()
                print("Student deleted successfully ✔")
                found = True
                break

        if not found:
            print("Student not found ❌")

    # UPDATE STUDENT
    elif choice == "5":
        roll = input("Enter roll number to update: ")

        found = False

        for s in students:
            if s["roll"] == roll:
                new_name = input("Enter new name: ")

                s["name"] = new_name

                save_data()

                print("Student updated successfully ✔")

                found = True
                break

        if not found:
            print("Student not found ❌")

    # EXIT
    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice ❌")