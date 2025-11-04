# Student Course Management System
# Uses: Control Flow, Loops, Functions, Lists, Dictionary, Tuple, Operators

# ------------ Data Structures ------------
students = []  # list
courses = ("Python", "C Programming", "Data Science", "Web Development")  # tuple
enrolled = {}  # dictionary student_name: course_name

# ------------ Functions ------------

def show_courses():
    print("\nAvailable Courses:")
    for i, course in enumerate(courses, start=1):
        print(f"{i}. {course}")


def add_student():
    name = input("Enter student name: ").strip()
    
    if name in students:
        print("❌ Student already exists!")
    else:
        students.append(name)
        print(f"✅ {name} added successfully!")


def enroll_student():
    if not students:
        print("⚠️ No students available. Add students first.")
        return
    
    name = input("Enter student name to enroll: ").strip()
    
    if name not in students:
        print("❌ Student not found. Add student first.")
        return
    
    show_courses()
    choice = int(input("Select course number: "))
    
    if 1 <= choice <= len(courses):  # comparison operator
        enrolled[name] = courses[choice - 1]
        print(f"✅ {name} enrolled in {courses[choice - 1]}")
    else:
        print("❌ Invalid course selection!")


def view_all():
    print("\n📌 Students and Enrolled Courses")
    if not enrolled:
        print("No enrollments yet.")
    else:
        for student, course in enrolled.items():
            print(f"{student} → {course}")


# ------------ Main Program / Control Flow ------------

while True:
    print("\n===== Student Course Management System =====")
    print("1. Add Student")
    print("2. Enroll Student in Course")
    print("3. View All Enrollments")
    print("4. Show Available Courses")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        enroll_student()
    elif choice == "3":
        view_all()
    elif choice == "4":
        show_courses()
    elif choice == "5":
        print("👋 Exiting... Thank you!")
        break
    else:
        print("❌ Invalid choice! Try again.")
