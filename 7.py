# # def decimal_to_binary(decimal):
# #     binary = ''
# #     while decimal > 0:
# #         binary = str(decimal % 2) + binary
# #         decimal //= 2
# #     return binary
# #
# #
# # def binary_to_decimal(binary):
# #     decimal = 0
# #     for i in binary[::-1]:
# #         decimal += int(i)
# #         decimal *= 2
# #     return decimal
# #
# #
# # def binary_to_decimal2(binary):
# #     decimal = 0
# #     binary = binary[::-1]
# #     for i in range(len(binary)):
# #         if binary[i] == '1':
# #             decimal += 2 ** i
# #     return decimal
# #
# #
# # print(binary_to_decimal2(binary=decimal_to_binary(decimal=18)))
#
#
# morse = {
#     'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•',
#     'g': '——•', 'h': '••••', 'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
#     'm': '——', 'n': '—•', 'o': '———', 'p': '•——•', 'q': '——•—', 'r': '•—•',
#     's': '•••', 't': '—', 'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
#     'y': '—•——', 'z': '——••'}
#
#
# def text_to_morse(text):
#     global morse
#     result = ''
#     text = text.lower()
#     for i in text:
#         if i in morse:
#             result += morse[i] + ' '
#         elif i == ' ':
#             result += '  '
#     return result
#
#
# def morse_to_text(morse_text):
#     global morse
#     morse_text = morse_text.replace('   ', ' | ').split()
#     text = ''
#     for i in morse_text:
#         if i == '|':
#             text += ' '
#         else:
#             for key, val in morse.items():
#                 if i == val:
#                     text += key
#                     break
#     return text
#
#
# print(morse_to_text(text_to_morse(text='Hello world')))


def list_offset(lst, n):
    n -= len(lst) * (n // len(lst))
    lst = lst[-n:] + lst[:-n]
    return lst


print(list_offset([1, 2, 3, 4, 5, 6, 7], -9))
