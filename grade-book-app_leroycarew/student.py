import json

class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = {}
        self.GPA = 0.0

    def calculate_GPA(self):
        total_points = sum(grade * credits for course, (grade, credits) in self.courses_registered.items())
        total_credits = sum(credits for course, (grade, credits) in self.courses_registered.items())
        if total_credits > 0:
            self.GPA = total_points / total_credits
        else:
            self.GPA = 0.0

    def register_for_course(self, course, grade):
        self.courses_registered[course.name] = (grade, course.credits)

    def to_dict(self):
        return {
            'email': self.email,
            'names': self.names,
            'courses_registered': self.courses_registered,
            'GPA': self.GPA
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(data['email'], data['names'])
        student.courses_registered = data['courses_registered']
        student.GPA = data['GPA']
        return student
