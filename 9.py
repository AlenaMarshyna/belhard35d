# # # # # # # # from random import randint, shuffle
# # # # # # # #
# # # # # # # #
# # # # # # # # class Student:
# # # # # # # #
# # # # # # # #     def __init__(self, first_name: str, group: int, marks: list[int]) -> None:
# # # # # # # #         self.first_name = first_name
# # # # # # # #         self.group = group
# # # # # # # #         self.marks = marks
# # # # # # # #
# # # # # # # #     def __str__(self) -> str:
# # # # # # # #         return f'Name: {self.first_name.title()}, Group: {self.group}, Marks: {self.marks}'
# # # # # # # #
# # # # # # # #
# # # # # # # # def student_sort(students: list[Student]) -> list[Student]:
# # # # # # # #     return sorted(students, key=lambda student: student.first_name)
# # # # # # # #
# # # # # # # #
# # # # # # # # user = Student('Alex', 45, [1, 2, 3])
# # # # # # # # user3 = Student('Ivan', 45, [5, 4, 3])
# # # # # # # # user2 = Student('Eva', 44, [4, 5, 6])
# # # # # # # # students = [user2, user3, user]
# # # # # # # # students = student_sort(students)
# # # # # # # # for student in students:
# # # # # # # #     print(student)
# # # # # # #
# # # # # # #
# # # # # # # class Rectangle:
# # # # # # #
# # # # # # #     def __init__(self, x: tuple[int, int], y: tuple[int, int]) -> None:
# # # # # # #         self.width = abs(x[0] - y[0])
# # # # # # #         self.height = abs(x[1] - y[1])
# # # # # # #
# # # # # # #     def perimeter(self) -> int:
# # # # # # #         return (self.width + self.height) * 2
# # # # # # #
# # # # # # #     def square(self) -> int:
# # # # # # #         return self.width * self.height
# # # # # #
# # # # # #
# # # # # class Numbers:
# # # # #
# # # # #     def __init__(self, numbers: list[int]) -> None:
# # # # #         self.numbers = numbers
# # # # #
# # # # #     def average(self) -> float:
# # # # #         return sum(self.numbers) / len(self.numbers)
# # # # #
# # # # #     def max_count(self) -> float:
# # # # #         from collections import Counter
# # # # #         numbers_counter = Counter(self.numbers)
# # # # #         max_count_number = numbers_counter.most_common(1)[0][1]
# # # # #         numbers = []
# # # # #         for key, val in numbers_counter.items():
# # # # #             if val == max_count_number:
# # # # #                 numbers.append(key)
# # # # #         return sum(numbers) / len(numbers)
# # # # #
# # # # #
# # # # # numbers = [1, 3, 5, 5, 23, 2, 45, 2, 5, 2, 4, 12, 34]
# # # # # numbers = Numbers(numbers=numbers)
# # # # # print(numbers.max_count())
# # # #
# # # #
# # # # class User(object):
# # # #
# # # #     def __init__(self, name: str, age: int) -> None:
# # # #         self.name = name.title()
# # # #         self.age = age
# # # #
# # # #     def __str__(self) -> str:
# # # #         return f'User: {self.name=} {self.age=}'
# # # #
# # # #     def info(self):
# # # #         print(self)
# # # #
# # # #
# # # # class Manager(User):
# # # #
# # # #     def __init__(self, name: str, age: int, salary: float) -> None:
# # # #         super().__init__(name, age)
# # # #         self.salary = salary
# # # #
# # # #     def __float__(self) -> float:
# # # #         return self.salary
# # # #
# # # #     def __str__(self):
# # # #         return super(Manager, self).__str__() + f' {self.salary=}'
# # # #
# # # #
# # # # vasya = Manager(name='vasya', age=24, salary=1500.0)
# # # # print(vasya)
# # # # print(float(vasya))
# # #
# # #
# # # class Category:
# # #
# # #     categories = ['Food', 'Drink']
# # #
# # #     def get(self, pk: int):
# # #         return self.categories[pk]
# # #
# # #
# # # class Product:
# # #
# # #     products = ['Fish', 'Coffee', 'Meat']
# # #
# # #     def get(self, pk: int):
# # #         return self.products[pk]
# # #
# # #
# # # def handler(obj: Category | Product):
# # #     obj.get(2)
# # #
# #
# # class User:
# #
# #     def __init__(self, name, card_number):
# #         self.name = name.title()
# #         self.__card_number = card_number
# #
# #     @property
# #     def card_number(self):
# #         return '**** **** **** ' + self.__card_number[-4:]
# #
# #     @card_number.setter
# #     def card_number(self, value):
# #         if not isinstance(value, str):
# #             raise TypeError('argument `value` must be str')
# #         value = value.replace(' ', '')
# #         if len(value) != 16 or not value.isdigit():
# #             raise ValueError
# #         self.__card_number = value
# #
# #
# # vasya = User('vasya', '1234 1234 1234 1234')
# # vasya.name = 'Petya'
# # print(vasya.name)
# # vasya.card_number = '1234567890'
# # print(vasya.card_number)
#
#
# from abc import ABC, abstractmethod
#
#
# class Person(ABC):
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @abstractmethod
#     def info(self):
#         pass
#
#
# class User(Person):
#
#     def info(self):
#         return f'User: {self.name=} {self.surname=}'
#
#
# vasya = Person('vasya', 'pupkin')
# print(vasya.name)
# print(vasya.info())


# from dataclasses import dataclass
#
#
# @dataclass
# class User:
#     first_name: str
#     age: int
#
#
# vasya = User(first_name='vasya', age=24)
# print(vasya.first_name)
# print(vasya)

# def info(self):
#     return self.name
#
#
# User = type('User', (), {'name': None, 'surname': None, 'info': info})
# vasya = User()
# vasya.name = 'vasya'
# print(vasya.info())
