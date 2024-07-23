class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.gpa = 0.0

    def calculate_gpa(self):
        if not self.courses_registered:
            self.gpa = 0.0
        else:
            total_credits = sum(course['credits'] for course in self.courses_registered)
            total_points = sum(course['grade'] * course['credits'] for course in self.courses_registered)
            self.gpa = total_points / total_credits

    def register_for_course(self, course, grade):
        self.courses_registered.append({
            'course': course,
            'credits': course.credits,
            'grade': grade
        })
        self.calculate_gpa()

    def __str__(self):
        return f"{self.names} ({self.email}) - GPA: {self.gpa:.2f}"
