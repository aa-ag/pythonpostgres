class Student:
    def __init__(self, s):
        self.name = s
        self.grades = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

a_student = Student("Aaron")
print(a_student.name, a_student.average_grade())