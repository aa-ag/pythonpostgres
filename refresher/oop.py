class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a_person_named_bob_who_is_35 = Person("Bob", 35)
print(a_person_named_bob_who_is_35)



# class Student:
#     def __init__(self, s, l):
#         self.name = s
#         self.grades = l

#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)

# a_student = Student("Aaron", [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(a_student.name, a_student.average_grade())