from Student import Student
from Storage import save_data, load_student

def menu():
    while True:
        print("\nWelcome to Student Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            name = input("Enter name: ")
            roll = int(input("Enter roll: "))
            marks = int(input("Enter marks: "))
            s = Student(name, roll, marks)
            save_data(s)

        elif choice == "2":
            load_student()

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")

# entry point
if __name__ == "__main__":
    menu()