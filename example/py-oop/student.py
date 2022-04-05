from person import *
from typing import Union, Optional


class Student(Person):
    __slots__ = "Class", "school", "id", "name", "age"

    def __new__(cls, id, name, age, Class, school):
        print(
            "Creating Student instance - run before __init__ - ",
            cls,
            id,
            name,
            age,
            Class,
            school,
        )
        return super(Person, cls).__new__(cls)

    # The child's __init__() function overrides the inheritance of the parent's __init__() function.
    def __init__(self, Class, school, age, name, id):
        self.school = school
        self.Class = Class
        # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
        super().__init__(id, name, age)  # Person.__init__(self, name, age)

        # self._Person__id = 'st11'
        # print(f'Student {self._Person__id}:', self.name, self.age, self.Class, self.school, self.person)

    @staticmethod
    def _is_adult(age: Optional[int]):
        return age > 20

    # Override method _print_self of Person
    def _print_self(self):
        # Person._print_self(self) # _print_self of Person
        print(
            f"Student {self._Person__id}:",
            self._name,
            self.age,
            self.Class,
            self.school,
            self.person,
        )  # can not access self.__id


st1 = Student(id="st1", age=30, name="student1", Class="class1", school="school1")
print(st1)  # __str__() | __repr__()
# st1._print_self()
# st1("+-")  # # shorthand of st1.__call__()
# print(st1.__slots__)
# print("Number of person: ", st1.person_count)
