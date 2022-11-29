# class Car(object):
#
#     def __init__(
#             self,
#             color: str,
#             count_passenger_seats: int,
#             is_baby_seat: bool
#     ) -> None:
#         self.color = color
#         self.count_passenger_seats = count_passenger_seats
#         self.is_baby_seat = is_baby_seat
#         self.is_busy = False
#
#     def __str__(self) -> str:
#         return f'Car: {self.color=} {self.count_passenger_seats} {self.is_baby_seat=} {self.is_busy=}'
#
#
# class Taxi(object):
#
#     def __init__(self, cars: list[Car]) -> None:
#         self.cars = cars
#
#     def find_car(self, count_passengers: int, is_baby: bool) -> Car | None:
#         for car in self.cars:
#             if not car.is_busy and car.count_passenger_seats >= count_passengers:
#                 if is_baby and car.is_baby_seat:
#                     car.is_busy = True
#                     return car
#                 elif not is_baby:
#                     car.is_busy = True
#                     return car
#
#
# # car1 = Car(color='black', count_passenger_seats=5, is_baby_seat=True)
# # car2 = Car(color='white', count_passenger_seats=4, is_baby_seat=False)
# # car3 = Car(color='red', count_passenger_seats=5, is_baby_seat=False)
# # cars = [car1, car2, car3]
# # taxi = Taxi(cars=cars)
# # print(taxi.find_car(5, True))
# # print(taxi.find_car(4, False))
# # print(taxi.find_car(4, False))
# # print(taxi.find_car(4, False))
#
# # class Category(object):
# #
# #     categories: list[str] = []
# #
# #     @classmethod
# #     def add(cls, category: str) -> int:
# #         category = category.title()
# #         if category in cls.categories:
# #             raise ValueError('category is  not unique')
# #         cls.categories.append(category)
# #         return cls.categories.index(category)
# #         # return len(cls.categories) - 1
# #
# #     @classmethod
# #     def get(cls, pk: int) -> str:
# #         try:
# #             return cls.categories[pk]
# #         except IndexError as e:
# #             raise ValueError(e)
# #
# #     @classmethod
# #     def delete(cls, pk: int) -> None:
# #         try:
# #             del cls.categories[pk]
# #         except IndexError:
# #             ...  # pass
# #
# #     # @classmethod
# #     # def update(cls, pk: int, new_category_name: str):
# #     #     new_category_name = new_category_name.title()
# #     #     if new_category_name in cls.categories:
# #     #         raise ValueError('category is not unique')
# #     #     try:
# #     #         cls.get(pk=pk)
# #     #     except ValueError:
# #     #         cls.add(category=new_category_name)
# #     #     else:
# #     #         cls.categories[pk] = new_category_name
# #
# #     @classmethod
# #     def update(cls, pk: int, new_category_name: str) -> None:
# #         new_category_name = new_category_name.title()
# #         if new_category_name in cls.categories:
# #             raise ValueError('category is not unique')
# #         try:
# #             cls.categories[pk] = new_category_name
# #         except IndexError:
# #             cls.add(category=new_category_name)
#
#
# class Category(object):
#
#     categories: list[dict] = []
#
#     @classmethod
#     def add(cls, category_name: str, is_published: bool) -> int:
#         category_name = category_name.title()
#         category = tuple(filter(lambda x: x['name'] == category_name, cls.categories))
#         if category:
#             raise ValueError('category is not unique')
#         cls.categories.append(
#             {
#                 'name': category_name,
#                 'is_published': is_published
#             }
#         )
#         return len(cls.categories) - 1
#
#     @classmethod
#     def get(cls, pk: int) -> dict:
#         try:
#             return cls.categories[pk]
#         except IndexError as e:
#             raise ValueError(e)
#
#     @classmethod
#     def delete(cls, pk: int) -> None:
#         try:
#             del cls.categories[pk]
#         except IndexError:
#             ...  # pass
#
#     @classmethod
#     def update(cls, new_category_name: str, pk: int) -> None:
#         new_category_name = new_category_name.title()
#         category = tuple(filter(lambda x: x['name'] == new_category_name, cls.categories))
#         if category:
#             raise ValueError('category is not unique')
#         try:
#             cls.categories[pk]['name'] = new_category_name
#         except IndexError:
#             cls.add(category_name=new_category_name, is_published=False)
#
#     @classmethod
#     def make_published(cls, pk: int) -> None:
#         try:
#             cls.categories[pk]['is_published'] = True
#         except IndexError as e:
#             raise ValueError(e)
#
#     @classmethod
#     def make_unpublished(cls, pk: int) -> None:
#         try:
#             cls.categories[pk]['is_published'] = False
#         except IndexError as e:
#             raise ValueError(e)
#
#
# print(Category.add('Food', True))
# print(Category.add('Drink', True))
# print(Category.add('food', False))
# from mypackage import is_palindrome

# is_palindrome()
# from app import baz

# baz()
# import re
#
#
# # email = '[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
# text = 'alex info@info.com pavel pavel@info.com'
# email = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
#
# print(re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text))

# for i in itertools.repeat('hello', 5):
#     for j in i:
#         print(j)

# words = ['', '', 'python', '', '']
# words = list(itertools.takewhile(lambda x: not x, words))
# print(words)

# print(list(itertools.compress('hello', (1, 1, 0, 1, 0))))
from itertools import zip_longest

text = '''
Hello
Python
World
Hello
Python
World
Hello
Python
World
'''
lines = [line for line in text.split('\n') if line]
# lines_iter = iter(lines)
# lines = list(zip_longest(*([lines_iter]*4)))
print(lines)
