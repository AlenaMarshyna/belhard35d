# # # # # first_name = 'alex'
# # # # # age, city = 42, 'Minsk'
# # # # # print(first_name, age, city, end=' конец строки ', sep='---')
# # # # # print(city)
# # # #
# # # # # last_name = input('Enter last name: ')
# # # # # print(last_name)
# # # # # a = 23.5
# # # # # b = 24.5
# # # # # print(round(a))
# # # # # print(round(b))
# # # # # a = '3.45'
# # # # # a = float(a)
# # # # # print(a)
# # # #
# # # # # a = 0.1 + 0.1 + 0.1
# # # # # print(a)
# # # #
# # # # # a = -5
# # # # # a = abs(a)
# # # # # print(a)
# # # # # a = 2.0
# # # # # print(a.is_integer())
# # # # # first_name = 'Morgan'
# # # # # last_name = 'Freeman'
# # # # # fullname = first_name + ' ' + last_name
# # # # # print(fullname)
# # # # # first_name = 'Alex'
# # # # # print((first_name + ' ') * 3)
# # # # # text = 'hello world'
# # # # # symbol = text[::-1]
# # # # # print(symbol)
# # # #
# # # # # text = 'qwerty'
# # # # # print(text[:3] + text[3:])
# # # #
# # # # # text = 'hello world'
# # # # # a = len(text)
# # # # # print(a)
# # # #
# # # # # text = r'hello\nworld' + '\\'
# # # # # print(text)
# # # #
# # # # # name = 'Alex'
# # # # # age = 35
# # # # #
# # # # # text = 'Hello %(name)s, age %(age)d' % {'name': name, 'age': age}
# # # # # text2 = 'Hello {name}, age {age}'.format(age=age, name=name)
# # # # # text3 = f'Hello {name}, age {age}'
# # # # # print(text)
# # # # # print(text2)
# # # # # print(text3)
# # # #
# # # # # text = 'hello world python pycharm'
# # # # # words = text.split(' ')
# # # # # text2 = '.-.'.join(words)
# # # # # print(text2)
# # # #
# # # # # text = 'hello python hello world python'
# # # # # a = text.find('python', 7, 12)
# # # # # b = text.rfind('python', 0, 20)
# # # # # a = text.index('python')
# # # # # b = text.rindex('python')
# # # # # print(a)
# # # # # print(b)
# # # # # print(text.count('python'))
# # # #
# # # # # text = 'hello python world python pycharm'
# # # # # print(text.partition('python'))
# # # # # print(text.rpartition('python'))
# # # #
# # # # # text = 'hello java java, java'
# # # # # text = text.replace('java', 'python', 2)
# # # # # print(text)
# # # #
# # # # # text = 'Hello Python'
# # # # # print(text.startswith('hell'))
# # # # # print(text.endswith('hon1'))
# # # #
# # # # # text = 'HELLO PYTHON'
# # # # # text = text.lower()
# # # # # print(text)
# # # # # text = text.upper()
# # # # # print(text)
# # # # # text = text.title()
# # # # # print(text)
# # # # # text = text.capitalize()
# # # # # print(text)
# # # # # text = text.swapcase()
# # # # # print(text)
# # # #
# # # # # text = 'hello\tpython'
# # # # # text = text.expandtabs(15)
# # # # # print(text)
# # # #
# # # # # text = '.-=....+-hello=-.+python+-=-.'
# # # # # print(text.lstrip('.-=+'))
# # # # # print(text.rstrip('.-=+'))
# # # # # print(text.strip('.-=+'))
# # # #
# # # # # text = '<b>hello<b> python</b> world</b>'
# # # # # text2 = text.replace('<b>', '').replace('</b>', '')
# # # # # print(text)
# # # # # print(text2)
# # # #
# # # # # text = 'hello'
# # # # # text = text.center(13, '-')
# # # # # text = text.zfill(10)
# # # # # text = text.ljust(10, '-')
# # # # # text = text.rjust(10, '-')
# # # # # print(text)
# # # # # lst = ['hello', 1234, True]
# # # # # numbers = [i for i in range(1, 101)]
# # # # # print(numbers)
# # # # # print(lst[0])
# # # # # print(lst[:2])
# # # # # print(list('hello'))
# # # # # words = ['hello', 'world', 'python']
# # # # # print(words[1][4])
# # # #
# # # # # numbers = [1, 2, 3, 4]
# # # # # lst = [numbers, 5, 6, 7]
# # # # # numbers.append(5)
# # # # # print(lst)
# # # #
# # # #
# # # # # numbers = [1, 2, 3, 4, 5]
# # # # # a = numbers.pop(2)
# # # # # print(numbers)
# # # # # print(a)
# # # #
# # # # # numbers = [2, '3', 4, 2, '3', 2, ]
# # # # # numbers.remove('3')
# # # # # print(numbers)
# # # #
# # # #
# # # # # numbers = [1, 2, [3, 4]]
# # # # # # numbers.extend('hello')
# # # # # # numbers.insert(1, 'new element')
# # # # # numbers[2].append(5)
# # # # # numbers[2][0] = 'hello'
# # # # # print(numbers)
# # # #
# # # # # words = ['hello', 'python', 'hello']
# # # # # print(words.count('hello'))
# # # #
# # # # # words = ['hey', 'hello', 'hi', 'python']
# # # # # words.sort(reverse=True)
# # # # # sort_words = sorted(words, key=len, reverse=True)
# # # # # print(words)
# # # # # print(sort_words)
# # # # # words.reverse()
# # # # # print(words)
# # # # # rev_words = words[::-1]
# # # # # print(words)
# # # # # print(rev_words)
# # # # # c = [5, 6]
# # # # # a = [1, 2, 3, 4, c]
# # # # # b = a.copy()
# # # # # a.append(5)
# # # # # a[4].append(7)
# # # # # print(a)
# # # # # print(b)
# # # #
# # # # # a = [6, 7]
# # # # # numbers = (1, 2, 3, 4, 5, a)
# # # # # a.append(8)
# # # # # print(numbers)
# # # #
# # # # # letters = tuple('hello')
# # # # # print(letters)
# # # #
# # # # # s1 = {1, 2, 3, 4, 5}
# # # # # s2 = {2, 3, 5}
# # # # # print(s2.issubset(s1))
# # # # # print(s1.issuperset(s2))
# # # #
# # # # # s1 = {1, 2, 3, 8, 4}
# # # # # s2 = {3, 4, 5}
# # # # # s3 = {6, 7, 8, 4, 3}
# # # # # s3 = frozenset(s3)
# # # # # s3 = set(s3)
# # # # # print(s3)
# # # # # s1 &= s2 & s3
# # # # # s1.intersection_update(s2, s3)
# # # # # print(s1)
# # # # # print(s1 & s2 & s3)
# # # # # s4 = s1.difference(s2, s3)
# # # # # s5 = s1 - s2 - s3
# # # # # print(s4)
# # # # # print(s5)
# # # # # s4 = s1 | s2 | s3
# # # # # s5 = s2.union(s1, s3)
# # # # # print(s4)
# # # # # print(s5)
# # # #
# # # # # user = {
# # # # #     'name': 'alex',
# # # # #     'city': 'Minsk',
# # # # #     'age': 26,
# # # # # }
# # # # # user['age'] = [user['age'], 35]
# # # # # print(user)
# # # # # user.update({'age': 35, 'language': 'ru'})
# # # # # print(user)
# # # # # keys = list(user.keys())
# # # # # print(keys)
# # # # # print(list(user.items()))
# # # # # new_user = user | {'age': 35, 'language': 'ru'}
# # # # # print(user)
# # # # # print(new_user)
# # # #
# # # # # numbers1 = [1, 2, 3, 4]
# # # # # numbers2 = [4, 5, 6]
# # # # # numbers3 = sum(numbers1 + numbers2)
# # # # # print(numbers1)
# # # # # print(numbers2)
# # # # # print(numbers3)
# # # # # numbers = [i for i in range(10)]
# # # # # print(numbers)
# # # # # n = int(input('n: '))
# # # # # user = {i: {} for i in range(n)}
# # # # # print(user)
# # # # # from collections import Counter
# # # # # text = 'hello world'
# # # # # data = {text[i]: text.count(text[i]) for i in range(0, len(text)) if text[i].isalpha()}
# # # # # data2 = {i: text.count(i) for i in text if i.isalpha()}
# # # # # data3 = Counter(text)
# # # # # numbers = [2**i for i in range(10)]
# # # #
# # # #
# # # # # n = int(input('n: '))
# # # # # numbers = [2**i for i in range(n+1)]
# # # # # print(numbers)
# # # #
# # # # # n = int(input('n: '))
# # # # # data = {i: {'name': input('name: '), 'email': input('email: ')} for i in range(1, n+1)}
# # # # # print(data[2]['name'])
# # # # # word = input()
# # # # #
# # # # # if word.isdigit():
# # # # #     word = int(word)
# # # # #     print('digit')
# # # # # elif word.isalpha():
# # # # #     print('word')
# # # # # elif word.isalnum():
# # # # #     print('letters and numbers')
# # # # # else:
# # # # #     print('symbols')
# # # #
# # # # # number = 5
# # # # #
# # # # # is_even = 'нечетное' if number % 2 else 'четное'
# # # # #
# # # # # if number % 2:
# # # # #     is_even = False
# # # # # else:
# # # # #     is_even = True
# # # # #
# # # # # text = 'hello'
# # # # # res = 'слово' if text.isalpha() else 'число' if text.isdigit() else 'не слово'
# # # # #
# # # # # if text.isalpha():
# # # # #     res = 'слово'
# # # # # else:
# # # # #     res = 'не слово'
# # # #
# # # # # text = 'hello'
# # # # #
# # # # # if text.isalpha() or text.isalnum() and text.islower():
# # # # #     pass
# # # #
# # # #
# # # # # x = True
# # # # # y = False
# # # # # z = False
# # # # # if not x or y:
# # # # #     print(1)
# # # # # elif not x or not y and z:
# # # # #     print(2)
# # # # # elif not x or y or not y and x:
# # # # #     print(3)
# # # # # else:
# # # # #     print(4)
# # # #
# # # #
# # # # # for number in range(1, 10, 2):  # 1 3 5 7 9
# # # # #     number **= 2
# # # # #     print(number)
# # # #
# # # # # numbers = [2, 5, 3, 5, 6, 9]
# # # # # # итерация по индексам
# # # # # for i in range(len(numbers)):
# # # # #     print(numbers[i])
# # # # #
# # # # # # итерация по элементам
# # # # # for number in numbers:
# # # # #     print(number)
# # # # #
# # # # # # итерация по индексам и ключам одновременно
# # # # # for i, val in enumerate(numbers):
# # # # #     print({i: val})
# # # #
# # # #
# # # # # data = {
# # # # #     'name': 'vasya',
# # # # #     'email': 'vasya@info.com'
# # # # # }
# # # # #
# # # # # for key, val in data.items():
# # # # #     print(key, val)
# # # #
# # # # # numbers = [4, 6, 0, 3, 7, 4, 0]
# # # # # for i, number in enumerate(numbers):
# # # # #     if number == 8:
# # # # #         break
# # # # #     numbers[i] = number ** 2
# # # # # else:
# # # # #     print('закончился самостоятельно')
# # # # # print(numbers)
# # # #
# # # # # n = 100
# # # # # while True:
# # # # #     n -= 1
# # # # #     print(n)
# # # #
# # # # # users = {
# # # # #     1: {
# # # # #         'name': 'name1',
# # # # #         'email': 'email1'
# # # # #     },
# # # # #     2: {
# # # # #         'name': 'name2',
# # # # #         'email': 'email2'
# # # # #     }
# # # # # }
# # # #
# # # # # for _ in range(10):
# # # # #     print('hello world!')
# # # #
# # # # # Вводится текст, вывести слова длина которых больше 5
# # # # # text = input()
# # # # # words = text.split()
# # # # # for word in words:
# # # # #     if len(word) > 5:
# # # # #         print(word)
# # # #
# # # # # try:
# # # # #     a = int(input())
# # # # #     b = int(input())
# # # # #     c = a / b
# # # # # except ValueError:
# # # # #     print('ты ввел не число')
# # # # # except ZeroDivisionError:
# # # # #     print('на 0 делить нельзя')
# # # # # else:
# # # # #     print('ошибок не было')
# # # # # finally:
# # # # #     print('сработает в любом случае')
# # # #
# # # # # raise ValueError('пользователь дурак!')
# # # #
# # # #
# # # # # if (word := input()).isalpha():
# # # # #     print(word)
# # # # # print(word := input())
# # # #
# # # #
# # # # # n = int(input())
# # # # # numbers = []
# # # # # for i in range(1, n+1):
# # # # #     if i != 5:
# # # # #         numbers.append(2**i)
# # # # #
# # # # #
# # # # # numbers = [2**i for i in range(1, n+1) if i != 5]
# # # # #
# # # #
# # # # #
# # # # # text = input()
# # # # # data = {}
# # # # # for i in text:
# # # # #     if i.isalpha():
# # # # #         data[i] = text.count(i)
# # # # #
# # # # # data = {i: text.count(i) for i in text if i.isalpha()}
# # # #
# # # # # Спрашивать данные у пользователя с клавиатуры до тех пор пока он не введет число
# # # #
# # # # # while not (number := input('Enter number: ')).isdigit():
# # # # #     pass
# # # # # N = 44
# # # # # 2 4 6 8 10
# # # # # 12 14 16 18 20
# # # # # 22 24 26 28 30
# # # # # 32 34 36 38 40
# # # # # 42 44
# # # # #
# # # # # numbers = [0, 1, 2, 3]
# # # # # for i in range(1, len(numbers)):
# # # # #     print(numbers[i])
# # # #
# # # # # n = int(input('n: '))
# # # # # m = int(input('m: '))
# # # # # k = int(input('k: '))
# # # # #
# # # # # while n:
# # # # #     if k % m == 0:
# # # # #         print(k)
# # # # #         n -= 1
# # # # #         k += m
# # # # #     else:
# # # # #         k += 1
# # # #
# # # #
# # # # # print(eval(input()))
# # # #
# # # #
# # # # # n = int(input('n: '))
# # # # #
# # # # # for i in range(2, n+1, 10):
# # # # #     for j in range(i, i+9, 2):
# # # # #         if j <= n:
# # # # #             print(j, end=' ')
# # # # #         else:
# # # # #             break
# # # # #     print()
# # # # #
# # # # # c = 0
# # # # # matrix = []
# # # # # line = []
# # # # # for i in range(2, n+1, 2):
# # # # #     if c < 5:
# # # # #         line.append(i)
# # # # #         c += 1
# # # # #     else:
# # # # #         c = 1
# # # # #         matrix.append(line)
# # # # #         line = [i]
# # # # #
# # # # # matrix.append(line)
# # # # # for line in matrix:
# # # # #     print(line)
# # # #
# # # # # for i in 'qwerty':
# # # # #     print(f'{i=}')
# # # # #     for j in range(10):
# # # # #         print(f'{j=}')
# # # #
# # # # # numbers = []
# # # # # for i in range(10):
# # # # #     numbers.append(i)
# # # # #     print(numbers)
# # # # #
# # # # # while numbers:
# # # # #     del numbers[-1]
# # # # #     print(numbers)
# # # #
# # # #
# # # # def baz():
# # # #     print('baz')
# # # #
# # # #
# # # # print(__name__)
# # # # if __name__ == '__main__':
# # # #     baz()
# # # # import os
# # # # from dotenv import load_dotenv
# # # # os.mkdir('folder')
# # # #
# # # # load_dotenv()
# # # #
# # # # print(os.getenv('TOKEN'))
# # # # import os
# # # # from pathlib import Path
# # # #
# # # # BASE_DIR = Path(__file__).resolve().parent
# # # # print(BASE_DIR / 'mypackage')
# # # # print(os.path.join(BASE_DIR, 'mypackage'))
# # #
# # #
# # # from datetime import datetime, timedelta
# # #
# # # # date = datetime(
# # # #     year=2022,
# # # #     month=5,
# # # #     day=23
# # # # )
# # # date2 = datetime.now()
# # # # print(date)
# # # # print(date2)
# # # # print(date2 - date)
# # # # print(date2 > date)
# # # # print(date2.timestamp())
# # # # print(datetime.fromtimestamp(1669967841.145449))
# # # print(date2.strftime('%d %B %y %H:%M'))
# # # date_str = '02 December 22 11:01'
# # # print(datetime.strptime(date_str, '%d %B %y %H:%M'))
# # # delta = timedelta(days=5, hours=3)
# # # print(date2 + delta)
# # # from http import HTTPStatus
# # # status_code = 301
# # # if status_code != HTTPStatus.OK:
# # #     pass
# #
# # # from enum import Enum
# #
# #
# # # class Roles(int, Enum):
# # #     Admin = 5
# # #     Manager = 3
# # #     User = 7
# # #
# # #
# # # class User(object):
# # #
# # #     def __init__(self, name: str, role_id: int):
# # #         self.name = name
# # #         self.role_id = role_id
# # #
# # #
# # # vasya = User('vasya', 3)
# # # if vasya.role_id == Roles.Admin:
# # #     pass
# # # from enum import IntEnum
# # #
# # # roles = [('Admin', 2), ('Manager', 1), ('User', 3)]
# # # Roles = IntEnum('Roles', roles)
# # # print(3 == Roles.Admin)
# # from argparse import ArgumentParser
# #
# # parser = ArgumentParser()
# # parser.add_argument(
# #     '-p',
# #     '--port',
# #     help='PORT',
# #     default='8000'
# # )
# # parser.add_argument(
# #     '-d',
# #     '--debug',
# #     action='store_true'
# # )
# # args = parser.parse_args()
# # print(args)
#
# import logging
#
# logging.basicConfig(
#     filename='log.log',
#     filemode='a',
#     format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
# )
#
# logging.error('user mudak')
# from itertools import zip_longest
# from math import ceil

# N = int(input('N: '))
# with open('numbers.txt', 'r', encoding='utf-8') as file:
#     lines = [line.strip() for line in file if line.strip()]
#     count = ceil(len(lines) / N)
#     lines_iter = iter(lines)
#     lines = list(zip_longest(*([lines_iter]*count)))
#
# for i in range(len(lines)):
#     with open(f'{i}.txt', 'w', encoding='utf-8') as file:
#         file.write('\n'.join([line for line in lines[i] if line]))


# N = int(input('N: '))
# with open('numbers.txt', 'r', encoding='utf-8') as file:
#     lines = [line.strip() for line in file if line.strip()]
#     lines_iter = iter(lines)
#     lines = list(zip_longest(*([lines_iter]*N)))
#
# for i in range(len(lines)):
#     with open(f'{i}.txt', 'w', encoding='utf-8') as file:
#         file.write('\n'.join([line for line in lines[i] if line]))
with open('numbers.txt', 'r', encoding='utf-8') as file:
    print(file.read())
    file.seek(0)
    words = file.read().lower().replace('\n', '').split()
vowels = 'ёуеэоаыяиюeyuioa'
vowels_count = 0
consonants_count = 0
for word in words:
    if word[0] in vowels:
        vowels_count += 1
    else:
        consonants_count += 1
if vowels_count > consonants_count:
    print('vowels')
elif consonants_count > vowels_count:
    print('consonants')
else:
    print('equal')
