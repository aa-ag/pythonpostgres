class ClassTest:
    def instace_method(self):
        print(f"Called instance_method of {self}")

test = ClassTest()

# option 1
test.instace_method()

# option 2 (exactly the same)
ClassTest.instace_method(test)