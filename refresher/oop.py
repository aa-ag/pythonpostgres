class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #def __str__(self):
    #    return f"Person: {self.name}; age: {self.age} years old."

    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"

a_person_named_bob_who_is_35 = Person("Bob", 35)
print(a_person_named_bob_who_is_35)