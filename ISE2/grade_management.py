students = []
grades = []

while True:
    print("Grade Management System")
    print("1. Add Student")
    print("2. Update Student Grade")
    print("3. Remove Student")
    print("4. Calculate Average Grade")
    print("5. Display Highest and Lowest Grade")
    print("6. Display All Students")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")

        if name in students:
            print("Student already exists!")
        else:
            grade = float(input("Enter student grade (0-100): "))

            if 0 <= grade <= 100:
                students.append(name)
                grades.append(grade)
                print("Student added successfully!")
            else:
                print("Grade must be between 0 and 100.")

    elif choice == '2':
        name = input("Enter student name to update: ")

        if name in students:
            index = students.index(name)
            grade = float(input("Enter new grade (0-100): "))

            if 0 <= grade <= 100:
                grades[index] = grade
                print("Grade updated successfully!")
            else:
                print("Grade must be between 0 and 100.")
        else:
            print("Student not found!")

    elif choice == '3':
        name = input("Enter student name to remove: ")

        if name in students:
            index = students.index(name)
            students.pop(index)
            grades.pop(index)
            print("Student removed successfully!")
        else:
            print("Student not found!")

    elif choice == '4':
        if len(grades) > 0:
            average = sum(grades) / len(grades)
            print("Average grade:", round(average, 2))
        else:
            print("No student grades available.")

    elif choice == '5':
        if len(grades) > 0:
            highest = max(grades)
            lowest = min(grades)

            print("Highest grade:", highest)
            print("Lowest grade:", lowest)
            print("Highest grade student(s):",
                  [students[i] for i in range(len(grades))
                   if grades[i] == highest])
            print("Lowest grade student(s):",
                  [students[i] for i in range(len(grades))
                   if grades[i] == lowest])
        else:
            print("No student grades available.")

    elif choice == '6':
        if len(students) > 0:
            print("\nStudent Name\tGrade")
            for i in range(len(students)):
                print(students[i], "\t\t", grades[i])
        else:
            print("No students available.")

    elif choice == '7':
        print("Exiting Grade Management System. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")