# # # # # # # # # # def decimal_to_binary(decimal):
# # # # # # # # # #     binary = ''
# # # # # # # # # #     while decimal > 0:
# # # # # # # # # #         binary = str(decimal % 2) + binary
# # # # # # # # # #         decimal //= 2
# # # # # # # # # #     return binary
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # def binary_to_decimal(binary):
# # # # # # # # # #     decimal = 0
# # # # # # # # # #     for i in binary[::-1]:
# # # # # # # # # #         decimal += int(i)
# # # # # # # # # #         decimal *= 2
# # # # # # # # # #     return decimal
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # def binary_to_decimal2(binary):
# # # # # # # # # #     decimal = 0
# # # # # # # # # #     binary = binary[::-1]
# # # # # # # # # #     for i in range(len(binary)):
# # # # # # # # # #         if binary[i] == '1':
# # # # # # # # # #             decimal += 2 ** i
# # # # # # # # # #     return decimal
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # print(binary_to_decimal2(binary=decimal_to_binary(decimal=18)))
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # morse = {
# # # # # # # # #     'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•',
# # # # # # # # #     'g': '——•', 'h': '••••', 'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
# # # # # # # # #     'm': '——', 'n': '—•', 'o': '———', 'p': '•——•', 'q': '——•—', 'r': '•—•',
# # # # # # # # #     's': '•••', 't': '—', 'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
# # # # # # # # #     'y': '—•——', 'z': '——••'}
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # def text_to_morse(text):
# # # # # # # # #     global morse
# # # # # # # # #     result = ''
# # # # # # # # #     text = text.lower()
# # # # # # # # #     for i in text:
# # # # # # # # #         if i in morse:
# # # # # # # # #             result += morse[i] + ' '
# # # # # # # # #         elif i == ' ':
# # # # # # # # #             result += '  '
# # # # # # # # #     return result
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # def morse_to_text(morse_text):
# # # # # # # # #     global morse
# # # # # # # # #     morse_text = morse_text.replace('   ', ' | ').split()
# # # # # # # # #     text = ''
# # # # # # # # #     for i in morse_text:
# # # # # # # # #         if i == '|':
# # # # # # # # #             text += ' '
# # # # # # # # #         else:
# # # # # # # # #             for key, val in morse.items():
# # # # # # # # #                 if i == val:
# # # # # # # # #                     text += key
# # # # # # # # #                     break
# # # # # # # # #     return text
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # print(morse_to_text(text_to_morse(text='Hello world')))
# # # # # # # #
# # # # # # # #
# # # # # # # # def list_offset(lst, n):
# # # # # # # #     n -= len(lst) * (n // len(lst))
# # # # # # # #     lst = lst[-n:] + lst[:-n]
# # # # # # # #     return lst
# # # # # # # #
# # # # # # # #
# # # # # # # # print(list_offset([1, 2, 3, 4, 5, 6, 7], -9))
# # # # # # #
# # # # # # #
# # # # # # # lst = [2, 3, 4, 5, 'fghj', True, [], None, 'dfgh', 'fgh']
# # # # # # # # var 1
# # # # # # # # lst = list(filter(lambda x: isinstance(x, str), lst))
# # # # # # # # print(lst)
# # # # # # # # var 2
# # # # # # # i = 0
# # # # # # # while i < len(lst):
# # # # # # #     if not isinstance(lst[i], str):
# # # # # # #         del lst[i]
# # # # # # #     else:
# # # # # # #         i += 1
# # # # # # # print(lst)
# # # # # #
# # # # # # numbers = [1, 2, 3, 4, 5, 6, 7]
# # # # # #
# # # # # #
# # # # # # def my_reversed(lst):
# # # # # #     for i in range(len(lst) // 2):
# # # # # #         j = len(lst) - 1 - i  # индекс элемента с противоположной стороны
# # # # # #         lst[i], lst[j] = lst[j], lst[i]
# # # # # #         # lst[i], lst[~i] = lst[~i], lst[i]
# # # # # #     return lst
# # # # # #
# # # # # #
# # # # # # print(my_reversed(numbers))
# # # # #
# # # # # numbers = [2, 6, 3, 4, 3, 3, 5, 6, 8, 2, 34, 6, 4]
# # # # #
# # # # #
# # # # # def my_sort(numbers):
# # # # #     # result = []
# # # # #     # for i in range(len(numbers)):
# # # # #     #     if numbers[i] % 2:
# # # # #     #         result.append(numbers[i])
# # # # #     #     else:
# # # # #     #         result.insert(0, numbers[i])
# # # # #     # return result
# # # # #     # for i in range(len(numbers)):
# # # # #     #     if numbers[i] % 2 == 0:
# # # # #     #         numbers.insert(0, numbers.pop(i))
# # # # #     # return numbers
# # # # #     numbers = list(filter(lambda x: not x % 2, numbers)) + list(filter(lambda x: x % 2, numbers))
# # # # #     return numbers
# # # # #
# # # # #
# # # # # print(my_sort(numbers))
# # # #
# # # #
# # # # def sum_neighbor(numbers):
# # # #     result = []
# # # #     for i in range(len(numbers)):
# # # #         if i < len(numbers) - 1:
# # # #             result.append(numbers[i-1] + numbers[i+1])
# # # #         else:
# # # #             result.append(numbers[i-1] + numbers[0])
# # # #     return result
# # # #
# # # #
# # # # numbers = [1, 2, 3, 4, 5, 6, 7]
# # # # print(sum_neighbor(numbers))
# # # #
# # #
# # # countries = {
# # #     'телемелитрямдия': ['нарния'],
# # #     'россия': ['москва', 'питер'],
# # #     'беларусь': ['минск', 'могилев', 'гомель']
# # # }
# # #
# # #
# # # def find_country(city):
# # #     global countries
# # #     for country, cities in countries.items():
# # #         if city.lower() in cities:
# # #             return country
# # #     return 'страна не найдена'
# # #
# # #
# # # print(find_country('могилев'))
# #
# #
# # users = {
# #     1: {
# #         'name': 'alex',
# #         'email': 'alex@gmail.com'
# #     },
# #     2: {
# #         'name': 'pavel',
# #         'email': ''
# #     },
# #     3: {
# #         'name': 'masha'
# #     }
# # }
# #
# # for user in users.values():
# #     # var 1
# #     # if 'email' not in user:
# #     #     print(user['name'])
# #     # elif user['email'] == '':
# #     #     print(user['name'])
# #
# #     # var2
# #     if not user.get('email'):
# #         print(user.get('name'))
#
#
# # print(bin(10))
# # print(bin(14))
# # print(bin(10 ^ 14))
# # print(~123)
# # print(bin(14))
# # print(bin(14 >> 2))
#
#
# # аннотация типов при определении переменных и изменении типа данных
# # a: int = int(input())
# # a += 1
# # a: str = str(a)
# #
# # расширенная типизация до python 3.10
# # from typing import List, Tuple, Any, Optional
# #
# #
# # def foo(numbers: List[Any, str]) -> Optional[List[Tuple[int, int]]]:
# #     return numbers
#
# # расширенная типизация с python 3.10
# # def bar(numbers: list[str, str]) -> list[tuple[int, int]] | None:
# #     a: str = numbers[0]
# #     return None
# #
# #
# # bar(1234)
#
#
# # Данна сумма вклада и процент вклада,
# # сказать через сколько лет сумма вклада увеличится в двое
# # (ставка рефинансирования)
# # 100$ 10% -> 8 year
#
#
# def calculate_deposit(deposit: float | int, percent: float | int, k: float | int) -> int:
#     expected_deposit = deposit * k
#     percent /= 100
#     years = 0
#     while deposit < expected_deposit:
#         deposit += deposit * percent
#         deposit = round(deposit, 2)
#         years += 1
#         print(f'{years=} {deposit=}')
#     return years
#
#
# print(calculate_deposit(
#     float(input('deposit: ')),
#     float(input('percent: ')),
#     float(input('k: ')))
# )

# C2H5OH -> {'C': 2, 'H': 6, 'O': 1}
# H2O -> {'H': 2, 'O': 1}

data = {}
formula = 'C2H5OH'
formula += '1' if formula[-1].isalpha() else ''
print(formula)

for i in range(len(formula)):
    if formula[i].isalpha():
        if formula[i+1].isdigit():
            if formula[i] in data:
                data[formula[i]] += int(formula[i+1])
            else:
                data[formula[i]] = int(formula[i+1])
        else:
            if formula[i] in data:
                data[formula[i]] += 1
            else:
                data[formula[i]] = 1
print(data)

