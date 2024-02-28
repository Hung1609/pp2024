import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name

class MarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_number(self, message):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print("Invalid input. Please enter a number.")

    def input_marks(self, message):
        while True:
            try:
                return float(input(message))
            except ValueError:
                print("Invalid input. Please enter a number.")

    def round_down(self, score):
        return math.floor(score * 10) / 10  # Round down to 1 decimal place

    def input_student_information(self):
        print("Enter Student Information")
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth (YYYY-MM-DD): ")
        return Student(student_id, student_name, student_dob)

    def input_course_information(self):
        print("Enter Course Information:")
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        return Course(course_id, course_name)

    def input_marks_for_course(self, course_id):
        print(f"Enter marks for course {course_id}:")
        marks = {}
        for student in self.students:
            mark = self.round_down(self.input_marks(f"Enter marks for {student.name}: "))
            marks[student.id] = mark
        self.marks[course_id] = marks

    def calculate_student_gpa(self, student_id):
        gpa = 0
        total_credits = 0
        for course_id, marks in self.marks.items():
            if student_id in marks:
                course = next(c for c in self.courses if c.id == course_id)
                credit = 3  # Example credit value, replace with actual credit value
                total_credits += credit
                gpa += marks[student_id] * credit
        if total_credits != 0:
            gpa /= total_credits
        return gpa

    def calculate_student_average_gpa(self, student_id):
        student_marks = []
        student_credits = []
        for course_id, marks in self.marks.items():
            if student_id in marks:
                course = next(c for c in self.courses if c.id == course_id)
                credit = 3  # Example credit value, replace with actual credit value
                student_credits.append(credit)
                student_marks.append(marks[student_id])
        if len(student_marks) > 0:
            return np.average(student_marks, weights=student_credits)
        else:
            return 0

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: self.calculate_student_gpa(student.id), reverse=True)

    def list_students_by_gpa(self):
        self.sort_students_by_gpa()
        print("\nList of Students sorted by GPA:")
        for student in self.students:
            gpa = self.calculate_student_gpa(student.id)
            print(f"ID: {student.id}, Name: {student.name}, GPA: {gpa:.2f}")

    def list_courses(self):
        print("\nList of Courses:")
        for course in self.courses:
            print(f"ID: {course.id}, Name: {course.name}")

    def list_students(self):
        print("\nList of Students:")
        for student in self.students:
            print(f"ID: {student.id}, Name: {student.name}")

    def show_student_marks_for_course(self, course_id):
        if course_id in self.marks:
            print(f"\nMarks for Course {course_id}:")
            for student_id, mark in self.marks[course_id].items():
                student = next((s for s in self.students if s.id == student_id), None)
                if student:
                    print(f"Student: {student.name}, Mark: {mark}")
                else:
                    print(f"Student with ID {student_id} not found.")
        else:
            print("No marks found for the specified course.")

    def run(self):
        num_students = self.input_number("Enter the number of students in the class: ")

        for _ in range(num_students):
            student_info = self.input_student_information()
            self.students.append(student_info)

        num_courses = self.input_number("Enter the number of courses: ")

        for _ in range(num_courses):
            course_info = self.input_course_information()
            self.courses.append(course_info)

        while True:
            print("\nMenu:")
            print("1. Input marks")
            print("2. List courses")
            print("3. List students")
            print("4. Show student marks for a course")
            print("5. List students by GPA")
            print("6. Exit")

            choice = input("Your choice is: ")
            if choice == '1':
                course_id = input("Enter the ID of the course you want to input marks for: ")
                if course_id in [course.id for course in self.courses]:
                    self.input_marks_for_course(course_id)
                else:
                    print("Invalid course ID.")
            elif choice == '2':
                self.list_courses()
            elif choice == '3':
                self.list_students()
            elif choice == '4':
                course_id = input("Enter the ID of the course: ")
                self.show_student_marks_for_course(course_id)
            elif choice == '5':
                self.list_students_by_gpa()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    mark_manager = MarkManager()
    mark_manager.run()
