class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.id = student_id
        self.name = student_name
        self.dob = student_dob

    def display_info(self):
        print(f"ID: {self.id}, Name: {self.name}, Date of Birth: {self.dob}")


class Course:
    def __init__(self, course_id, course_name):
        self.id = course_id
        self.name = course_name

    def display_info(self):
        print(f"ID: {self.id}, Name: {self.name}")


class MarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_number_of_students(self):
        return int(input("Enter the number of students in the class: "))

    def input_student_information(self):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth: ")
        return Student(student_id, student_name, student_dob)

    def input_number_of_courses(self):
        return int(input("Enter the number of courses: "))

    def input_course_information(self):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        return Course(course_id, course_name)

    def input_marks_for_course(self, students, course_id):
        marks = {}
        for student in students:
            mark = float(input(f"Enter marks for {student.name} in course {course_id}: "))
            marks[student.id] = mark
        return marks

    def list_courses(self):
        print("\nList of Courses:")
        for course in self.courses:
            course.display_info()

    def list_students(self):
        print("\nList of Students:")
        for student in self.students:
            student.display_info()

    def show_student_marks_for_course(self, course_id):
        if course_id in self.marks:
            print(f"\nStudent Marks for Course {course_id}:")
            for student_id, mark in self.marks[course_id].items():
                student = next(s for s in self.students if s.id == student_id)
                print(f"Student ID: {student_id}, Name: {student.name}, Mark: {mark}")
        else:
            print(f"No marks recorded for Course {course_id}")

    def run(self):
        self.students = []
        num_students = self.input_number_of_students()

        for _ in range(num_students):
            student_info = self.input_student_information()
            self.students.append(student_info)

        self.courses = []
        num_courses = self.input_number_of_courses()

        for _ in range(num_courses):
            course_info = self.input_course_information()
            self.courses.append(course_info)

        choice = ''
        while choice != '4':
            print("1. Input marks")
            print("2. List courses")
            print("3. List students")
            print("4. Show students marks")

            choice = input("Your choice is: \n")
            if choice == '1':
                selected_course_id = input("Enter the ID of the course you want to input marks for: ")
                self.marks = self.input_marks_for_course(self.students, selected_course_id)
            elif choice == '2':
                self.list_courses()
            elif choice == '3':
                self.list_students()
            elif choice == '4':
                self.show_student_marks_for_course(selected_course_id)
            else:
                print("Invalid")


if __name__ == "__main__":
    mark_manager = MarkManager()
    mark_manager.run()
