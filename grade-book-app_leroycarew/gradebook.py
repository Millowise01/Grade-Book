import json
from student import Student
from course import Course

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, student):
        self.student_list.append(student)

    def add_course(self, course):
        self.course_list.append(course)

    def register_student_for_course(self, email, course_name):
        student = next((s for s in self.student_list if s.email == email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            grade = float(input(f"Enter grade for {student.names} in {course.name}: "))
            student.register_for_course(course, grade)
        else:
            print("Student or Course not found.")

    def calculate_GPA(self, email):
        student = next((s for s in self.student_list if s.email == email), None)
        if student:
            student.calculate_GPA()
            print(f"GPA of {student.names}: {student.GPA}")
        else:
            print("Student not found.")

    def calculate_ranking(self):
        self.student_list.sort(key=lambda s: s.GPA, reverse=True)
        for rank, student in enumerate(self.student_list, start=1):
            print(f"{rank}. {student.names} - GPA: {student.GPA}")

    def search_by_grade(self, grade):
        result = [s for s in self.student_list if any(g == grade for g, c in s.courses_registered.values())]
        for student in result:
            print(f"{student.names} - GPA: {student.GPA}")

    def generate_transcript(self, email):
        student = next((s for s in self.student_list if s.email == email), None)
        if student:
            print(f"Transcript for {student.names}")
            for course, (grade, credits) in student.courses_registered.items():
                print(f"Course: {course}, Grade: {grade}, Credits: {credits}")
            print(f"Overall GPA: {student.GPA}")
        else:
            print("Student not found.")

    def delete_student(self, email):
        self.student_list = [s for s in self.student_list if s.email != email]

    def delete_course(self, name):
        self.course_list = [c for c in self.course_list if c.name != name]
        for student in self.student_list:
            if name in student.courses_registered:
                del student.courses_registered[name]

    def update_student_info(self, email, new_names):
        student = next((s for s in self.student_list if s.email == email), None)
        if student:
            student.names = new_names
        else:
            print("Student not found.")

    def update_course_info(self, name, new_name, new_trimester, new_credits):
        course = next((c for c in self.course_list if c.name == name), None)
        if course:
            course.name = new_name
            course.trimester = new_trimester
            course.credits = new_credits
        else:
            print("Course not found.")

    def view_all_students(self):
        for student in self.student_list:
            print(f"Email: {student.email}, Names: {student.names}, GPA: {student.GPA}")

    def view_all_courses(self):
        for course in self.course_list:
            print(f"Name: {course.name}, Trimester: {course.trimester}, Credits: {course.credits}")

    def save_to_file(self, filename):
        data = {
            'students': [student.to_dict() for student in self.student_list],
            'courses': [course.to_dict() for course in self.course_list]
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.student_list = [Student.from_dict(s) for s in data['students']]
                self.course_list = [Course.from_dict(c) for c in data['courses']]
        except FileNotFoundError:
            print(f"No data file found at {filename}. Starting with an empty grade book.")
