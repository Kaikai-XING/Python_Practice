"""
Revisit the basics of python class
"""

class Student(object):

    # Initialization using the method __init__
    # Set attribute name, age to the object Student
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    
    def study(self, course_name):
        print('%s is studying %s' % (self.name, course_name) )
    
    def relaxing(self):
        if self.gender == "M":
            print('%s is shopping' % (self.name))
        else:
            print('%s is playing video games' % (self.name))


def main_1():
    # initialize a new student object
    student_1 = Student("Klein", "M")
    # use the method study
    student_1.study("Python")
    # use the method relaxing
    student_1.relaxing()

    # initialize second student object
    student_1 = Student("Kate", "F")
    # use the method study
    student_1.study("Physics")
    # use the method relaxing
    student_1.relaxing()


# The methods and attributes in python classes are private or public
# The method are normally set to be public
# To set the attributes/methods as private, compose the attribute name staring with two underscores __


class Test():

    def __init__(self, foo):
        self.__foo = foo
    
    def __bar(self):
        print(self.__foo)
        print('__bar')


def main_2():
    # initialize a test object
    test = Test("hello")
    # test.__bar()      # AttributeError: 'Test' object has no attribute '__bar'
    # print(test.__foo) # AttributeError: 'Test' object has no attribute '__foo'


# However, python actually just changes those "private" attributes or methods name so that you they are not easily accible
# They are not strictly not accessible
# if you know the convention of how the names are changed, you can still visit them using proper names

# exmaple:
def main_3():
    test_2 = Test('Hello again')
    test_2._Test__bar()
    print(test_2._Test__foo)


if __name__ == '__main__':
    print("------ Section 1: Basics ------")
    main_1()
    print("\n")
    print("------ Section 2: Access of the attributes and methods ------")
    main_2()
    print("\n")
    print("------ Section 3: Not an actual strict private ------")
    main_3()
