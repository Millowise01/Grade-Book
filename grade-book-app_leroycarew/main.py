from student import Student
from course import Course
from gradebook import GradeBook

def main():
    gradebook = GradeBook()

    while True:
        print("\nGrade Book Application")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate GPA")
        print("5. Calculate Ranking")
        print("6. Search by Grade")
        print("7. Generate Transcript")
        print("8. Exit")
        
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
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
