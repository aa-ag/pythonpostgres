class ClassTest:
    def instace_method(self):
        '''
         used for most things: produce an action 
         with the data inside an object, or if you
         want to modify the data inside an object
        '''
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        '''
         commonly used as factories
        '''
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        '''
         used to place a method inside a class
        '''
        print("Called static_method.")


ClassTest.static_method()