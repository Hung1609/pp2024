def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

def input_student_information():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    return {'id': student_id, 'name': student_name, 'dob': student_dob}

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_information():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return {'id': course_id, 'name': course_name}

def input_marks_for_course(students, course_id):
    marks = {}
    for student in students:
        mark = float(input(f"Enter marks for {student['name']} in course {course_id}: "))
        marks[student['id']] = mark
    return marks

def list_courses(courses):
    print("\nList of Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def list_students(students):
    print("\nList of Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}")

def show_student_marks_for_course(marks, students, course_id):
    if course_id in marks:
        print(f"\nStudent Marks for Course {course_id}:")
        for student_id, mark in marks[course_id].items():
            student_name = next(student['name'] for student in students if student['id'] == student_id)
            print(f"Student ID: {student_id}, Name: {student_name}, Mark: {mark}")
    else:
        print(f"No marks recorded for Course {course_id}")

def run():
    students = []
    num_students = input_number_of_students()

    for _ in range(num_students):
        student_info = input_student_information()
        students.append(student_info)

    courses = []
    num_courses = input_number_of_courses()

    for _ in range(num_courses):
        course_info = input_course_information()
        courses.append(course_info)

    while True:  # Corrected from 'true' to 'True'
        print("1. Input marks")
        print("2. List courses")
        print("3. List students")
        print("4. Show students marks")

        choice = input("Your choice is: \n")
        if choice == '1':
            selected_course_id = input("Enter the ID of the course you want to input marks for: ")
            marks = input_marks_for_course(students, selected_course_id)
        elif choice == '2':
            list_courses(courses)
        elif choice == '3':
            list_students(students)
        elif choice == '4':
            show_student_marks_for_course(marks, students, selected_course_id)
            break
        else:
            print("Invalid")

if __name__ == "__main__":
    run()