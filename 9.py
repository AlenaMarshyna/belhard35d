# # from random import randint, shuffle
# #
# #
# # class Student:
# #
# #     def __init__(self, first_name: str, group: int, marks: list[int]) -> None:
# #         self.first_name = first_name
# #         self.group = group
# #         self.marks = marks
# #
# #     def __str__(self) -> str:
# #         return f'Name: {self.first_name.title()}, Group: {self.group}, Marks: {self.marks}'
# #
# #
# # def student_sort(students: list[Student]) -> list[Student]:
# #     return sorted(students, key=lambda student: student.first_name)
# #
# #
# # user = Student('Alex', 45, [1, 2, 3])
# # user3 = Student('Ivan', 45, [5, 4, 3])
# # user2 = Student('Eva', 44, [4, 5, 6])
# # students = [user2, user3, user]
# # students = student_sort(students)
# # for student in students:
# #     print(student)
#
#
# class Rectangle:
#
#     def __init__(self, x: tuple[int, int], y: tuple[int, int]) -> None:
#         self.width = abs(x[0] - y[0])
#         self.height = abs(x[1] - y[1])
#
#     def perimeter(self) -> int:
#         return (self.width + self.height) * 2
#
#     def square(self) -> int:
#         return self.width * self.height


class Numbers:

    def __init__(self, numbers: list[int]) -> None:
        self.numbers = numbers

    def average(self) -> float:
        return sum(self.numbers) / len(self.numbers)

    def max_count(self) -> float:
        from collections import Counter
        numbers_counter = Counter(self.numbers)
        max_count_number = numbers_counter.most_common(1)[0][1]
        numbers = []
        for key, val in numbers_counter.items():
            if val == max_count_number:
                numbers.append(key)
        return sum(numbers) / len(numbers)


numbers = [1, 3, 5, 5, 23, 2, 45, 2, 5, 2, 4, 12, 34]
numbers = Numbers(numbers=numbers)
print(numbers.max_count())
