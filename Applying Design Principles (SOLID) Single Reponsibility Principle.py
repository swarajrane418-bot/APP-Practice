class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


class GradeCalculator:
    def calculate_grade(self, student):
        if student.marks >= 90:
            return "A"
        elif student.marks >= 75:
            return "B"
        else:
            return "C"


class StudentDatabase:
    def save(self, student):
        print(f"Saving {student.name} to database...")


class EmailService:
    def send_grade(self, student, grade):
        print(f"Sending email to {student.name}: Your grade is {grade}")


# Usage
student = Student("Swaraj", 88)

calculator = GradeCalculator()
grade = calculator.calculate_grade(student)

db = StudentDatabase()
db.save(student)

email = EmailService()
email.send_grade(student, grade)