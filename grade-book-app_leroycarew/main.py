import pickle
from student import Student
from course import Course

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []
        self.load_data()

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student)

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)

    def remove_student(self, email):
        self.student_list = [s for s in self.student_list if s.email != email]

    def remove_course(self, name):
        self.course_list = [c for c in self.course_list if c.name != name]
        for student in self.student_list:
            student.courses_registered = [course for course in student.courses_registered if course['course'].name != name]
            student.calculate_gpa()

    def register_student_for_course(self, email, course_name, grade):
        student = next((s for s in self.student_list if s.email == email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)
        else:
            print("Student or course not found")

    def unenroll_student_from_course(self, email, course_name):
        student = next((s for s in self.student_list if s.email == email), None)
        if student:
            student.courses_registered = [course for course in student.courses_registered if course['course'].name != course_name]
            student.calculate_gpa()

    def calculate_ranking(self):
        return sorted(self.student_list, key=lambda s: s.gpa, reverse=True)

    def search_by_grade(self, course_name, grade):
        students = []
        for student in self.student_list:
            for course in student.courses_registered:
                if course['course'].name == course_name and course['grade'] == grade:
                    students.append(student)
        return students

    def generate_transcript(self, email):
        student = next((s for s in self.student_list if s.email == email), None)
        if student:
            print(f"Transcript for {student.names} ({student.email}):")
            for course in student.courses_registered:
                print(f"{course['course'].name} - {course['grade']}")
            print(f"GPA: {student.gpa:.2f}")
        else:
            print("Student not found")

    def display_students(self):
        if not self.student_list:
            print("No students available.")
        else:
            print("Students:")
            for student in self.student_list:
                print(student)

    def display_courses(self):
        if not self.course_list:
            print("No courses available.")
        else:
            print("Courses:")
            for course in self.course_list:
                print(course)

    def save_students(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.student_list, file)

    def load_students(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.student_list = pickle.load(file)
        except (FileNotFoundError, EOFError):
            self.student_list = []

    def save_courses(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.course_list, file)

    def load_courses(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.course_list = pickle.load(file)
        except (FileNotFoundError, EOFError):
            self.course_list = []

    def save_data(self):
        self.save_students('students.pkl')
        self.save_courses('courses.pkl')

    def load_data(self):
        self.load_students('students.pkl')
        self.load_courses('courses.pkl')
