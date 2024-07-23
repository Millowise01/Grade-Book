from student import Student
from course import Course
from gradebook import GradeBook

def main():
    filename = 'grades.txt'
    gradebook = GradeBook()
    gradebook.load_from_file(filename)

    while True:
        print("\nGrade Book Application")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate GPA")
        print("5. Calculate Ranking")
        print("6. Search by Grade")
        print("7. Generate Transcript")
        print("8. Delete Student")
        print("9. Delete Course")
        print("10. Update Student Information")
        print("11. Update Course Information")
        print("12. View All Students")
        print("13. View All Courses")
        print("14. Save and Exit")

        choice = input("Choose an action: ")

        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gradebook.add_student(Student(email, names))
        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter trimester: ")
            credits = int(input("Enter course credits: "))
            gradebook.add_course(Course(name, trimester, credits))
        elif choice == '3':
            email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            gradebook.register_student_for_course(email, course_name)
        elif choice == '4':
            email = input("Enter student email: ")
            gradebook.calculate_GPA(email)
        elif choice == '5':
            gradebook.calculate_ranking()
        elif choice == '6':
            grade = float(input("Enter grade to search for: "))
            gradebook.search_by_grade(grade)
        elif choice == '7':
            email = input("Enter student email: ")
            gradebook.generate_transcript(email)
        elif choice == '8':
            email = input("Enter student email to delete: ")
            gradebook.delete_student(email)
        elif choice == '9':
            name = input("Enter course name to delete: ")
            gradebook.delete_course(name)
        elif choice == '10':
            email = input("Enter student email to update: ")
            new_names = input("Enter new student names: ")
            gradebook.update_student_info(email, new_names)
        elif choice == '11':
            name = input("Enter course name to update: ")
            new_name = input("Enter new course name: ")
            new_trimester = input("Enter new trimester: ")
            new_credits = int(input("Enter new credits: "))
            gradebook.update_course_info(name, new_name, new_trimester, new_credits)
        elif choice == '12':
            gradebook.view_all_students()
        elif choice == '13':
            gradebook.view_all_courses()
        elif choice == '14':
            gradebook.save_to_file(filename)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
