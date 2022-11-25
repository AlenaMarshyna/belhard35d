# # from dataclasses import dataclass, Field
# # from collections import namedtuple
# #
# #
# # # User = namedtuple('User', ('name', 'email', 'age'))
# # #
# # # vasya = User('vasya', 'vasya@email.com', 24)
# # # print(vasya._asdict())
# #
# # @dataclass
# # class User:
# #     name: str
# #     email: str
# #     age: int
# #
# #
# # vasya = User('vasya', 'vasya@email.com', 24)
# # print(vasya.email)
# # print(vasya.__dict__)
# # try:
# #     2 / 0
# # except ZeroDivisionError as e:
# #     print(e)
#
#
# # def create_decorator(a):
# #     def wrapper(b):
# #         print(a * b)
# #     return wrapper
# #
# #
# # c = create_decorator(4)
# # c(5)
# # c(6)
# # class A(object):
# #     a = 123
# #
# #
# # A.a = 321
# # a = A()
# # a.a = 321
# # b = A()
# # print(b.a)
# # print(a.__dir__())
#
# # file = open('source/input.txt', 'r', encoding='utf-8')
# ## text = file.read()
# ## print(text)
# # text = file.readline()
# # print(text)
# # text = file.readline()
# # print(text)
# # text = file.readline()
# # print(text)
# # lines = file.readlines()
# # print(lines)
# # lines = [line.strip() for line in file.readlines()]
# # print(lines)
# # lines = [line.strip() for line in file if line.strip()]
# # print(lines)
# # file.close()
# # file = open('numbers.txt', 'r', encoding='utf-8')
# # numbers = [int(line.strip()) for line in file if line.strip().isdigit()]
# # print(numbers)
# # file.close()
# # numbers = [4, 7, 5, 3, 6]
# # text = '\n'.join(list(map(str, numbers)))
# # print(text)
# # file = open('numbers.txt', 'a', encoding='utf-8')
# # file.write(text + '\n')
# # file.close()
# #
# # with open('source/input.txt', 'r', encoding='utf-8') as file:
# #     lines = [line.strip() for line in file if line.strip()]
# #     file.seek(0)
# #     print(file.readlines())
# #     file.seek(0)
# #     print(file.read())
# # print(lines)
#
# # import json
# # text = '''
# # {
# #   "1": {
# #     "name": "pavel",
# #     "email": "pavel@gmail.com"
# #   },
# #   "2": {
# #     "name": "masha",
# #     "email": "masha@gmail.com"
# #   }
# # }
# # '''
# # with open('users.json', 'r', encoding='utf-8') as file:
# #     data = json.load(file)
# # print(data)
# # data = {
# #     'first_name': 'алекс',
# #     'last_name': 'попов'
# # }
# # with open('alex.json', 'w', encoding='utf-8') as file:
# #     json.dump(data, file, indent=2, ensure_ascii=False)
#
#
# # from pydantic import BaseModel, EmailStr, Field
# #
# #
# # class Address(BaseModel):
# #     city: str
# #     street: str
# #     number: int = None
# #
# #
# # class User(BaseModel):
# #     name: str
# #     age: int
# #     email: EmailStr
# #     address: Address
# #
# #
# # data = [{
# #     'name': 'vasya',
# #     'age': '32',
# #     'email': 'vasya@info.com',
# #     'address': {
# #         'city': 'minsk',
# #         'street': 'beruta',
# #         # 'number': 23
# #     }
# # } for _ in range(15)]
# #
# # users = [User(**user) for user in data]
# # print(users)
# # print(vasya.age)
# # print(vasya.email)
# # print(vasya.dict())
#
# from csv import DictReader, DictWriter
#
# # with open('users.csv', 'r', encoding='utf-8') as file:
# #     reader = DictReader(file)
# #     for user in reader:
# #         print(user)
# users = [
#     {
#         'name': 'alex',
#         'email': 'alex@gmail.com',
#         'age': 23
#     },
#     {
#         'name': 'pavel',
#         'email': 'pavel@gmail.com',
#         'age': 43
#     }
# ]
# with open('users.csv', 'w', encoding='utf-8') as file:
#     fieldnames = ['name', 'email', 'age']
#     writer = DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(users)
