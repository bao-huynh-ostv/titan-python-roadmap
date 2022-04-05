from datetime import date
from typing import Union, Optional

__all__ = ["Person"]


class Person:
    # __slots__ = (
    #     "__id",
    #     "_name",
    #     "age",
    # )  # Storing value references in __slots__ instead of __dict__.
    _protected = "protected"
    __private = "private"
    person = True
    person_count = 0

    def __new__(cls, id, name, age: int = 1):
        print("Creating Person instance - run before __init__ - ", cls, id, name, age)
        return super(Person, cls).__new__(cls)

    def __init__(self, id, name, age: int = 1):
        # self.__private = 'private1'
        # print('in class',self.__private)
        self.__id = id
        self._name = name
        self.age: int = age
        Person.person = not Person.person
        Person.person_count += 1
        # Person.age = 100
        print(f"Init person {self.__id}:", self._name, self.age, self.person)

    @classmethod
    def __infant(cls, *args, **kwargs):
        # print(cls.__init__.__code__.co_varnames)
        return cls(f"p{Person.person_count+1}", f"Name{Person.person_count+1}")

    @staticmethod
    def _is_adult(age: Optional[int]):
        if age is not None:
            return age > 18

    def __call__(self, para=""):
        print(f"{para}Person {self._name} was born in {date.today().year - self.age}")

    def __private_method(self):
        print("Number of person: ", self.person_count)

    def _print_self(self):
        print(f"Person {self.__id}:", self._name, self.age, self.person)

    def __repr__(self):
        return f"Person {self.__id}: {self._name}, {self.age}, {self.person}  | repr"

    def __str__(self):
        return f"Person {self.__id}: {self._name}, {self.age}, {self.person}  | str"

    def __add__(self, person: "Person"):
        if isinstance(self.age, int) and isinstance(person.age, int):
            p = Person(
                id=f"{self.__id}-{person.__id}",
                name=f"{self._name}-{person._name}",
                age=self.age + person.age,
            )
            print(p)
            return p
        else:
            raise Exception("Age Must Be Interger")

    # Destructors are called when an object gets destroyed
    # Destructors are not needed as much in Python cuz Python has a garbage collector that handles memory management automatically
    # def __del__(self):
    #     print('delete', self)


# p1 = Person("p1", "Name1", 4)
# p2 = Person("p2", "Name2", age=2)
# p = p2.__infant() #Person.infant()
# print(p2._is_adult(19)) #Person
# # p1._print_self()
# print(p1) # print(str(p1)) => call function __str__ | print(repr(p1)) => call function __repr__
# p3 = p1 + p2
# print(p2.__dict__) #deny creation __dict__ if declare __slots__
# print(p2.__slots__)
# p1._Person__private_method()  # p1.__private_method() => can't not access
