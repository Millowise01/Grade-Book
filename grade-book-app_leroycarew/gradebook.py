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
