# GradeBook Application

## Overview

The GradeBook Application is a Python program that allows users to create and manage student records, course records, and transcripts. It includes features for course registration, GPA calculation, and data structure search and ranking.

## Features

- Create student records using user input
- Store student information, including email, names, and courses registered
- Create course records with name, trimester, and credits
- Allow students to register for courses
- Allow students to unenroll from courses
- Remove students from the system
- Remove courses from the system
- Calculate and save the GPA for each student
- Provide a ranking of students based on their GPA
- Search students by grade obtained in a course
- Create transcripts for each student showing their GPA
- Save and load the student and course data to and from files

## How to Run

1. Clone the repository.
2. Navigate to the project directory.
3. Run `python3 main.py`.

## File Descriptions

- `main.py`: The main program file that runs the GradeBook application.
- `student.py`: Contains the `Student` class with attributes and methods related to student records.
- `course.py`: Contains the `Course` class with attributes related to course records.
- `gradebook.py`: Contains the `GradeBook` class with methods for managing students, courses, and performing various operations.
- `README.md`: This file, providing an overview of the project and instructions on how to run it.
