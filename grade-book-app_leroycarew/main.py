from gradebook import GradeBook
import os

def main():
    gb = GradeBook()

    # Load existing data
    if os.path.exists("students.pkl"):
        gb.load_students("students.pkl")
    if os.path.exists("courses.pkl"):
        gb.load_courses("courses.pkl")

    while True:
        print("\nGradeBook Menu")
        print("1. Add student")
        print("2. Add course")
        print("3. Remove student")
        print("4. Remove course")
        print("5. Register student for course")
        print("6. Unenroll student from course")
        print("7. Calculate ranking")
        print("8. Search by grade")
        print("9. Generate transcript")
        print("10. Save and Exit")
        
        choice = input("Choose an action: ")

        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gb.add_student(email, names)
        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            gb.add_course(name, trimester, credits)
        elif choice == '3':
            email = input("Enter student email to remove: ")
            gb.remove_student(email)
        elif choice == '4':
            name = input("Enter course name to remove: ")
            gb.remove_course(name)
        elif choice == '5':
            email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            gb.register_student_for_course(email, course_name, grade)
        elif choice == '6':
            email = input("Enter student email: ")
            course_name = input("Enter course name to unenroll: ")
            gb.unenroll_student_from_course(email, course_name)
        elif choice == '7':
            ranking = gb.calculate_ranking()
            print("Student Ranking:")
            for student in ranking:
                print(student)
        elif choice == '8':
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            students = gb.search_by_grade(course_name, grade)
            print(f"Students with grade {grade} in {course_name}:")
            for student in students:
                print(student)
        elif choice == '9':
            email = input("Enter student email: ")
            gb.generate_transcript(email)
        elif choice == '10':
            gb.save_students("students.pkl")
            gb.save_courses("courses.pkl")
            print("GradeBook saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
