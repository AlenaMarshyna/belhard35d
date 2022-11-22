from random import randint, shuffle


class Student:

    def __init__(self, first_name: str, group: int, marks: list[int]) -> None:
        self.first_name = first_name
        self.group = group
        self.marks = marks

    def __str__(self) -> str:
        return f'Name: {self.first_name.title()}, Group: {self.group}, Marks: {self.marks}'


def student_sort(students: list[Student]) -> list[Student]:
    return sorted(students, key=lambda student: student.first_name)


user = Student('Alex', 45, [1, 2, 3])
user3 = Student('Ivan', 45, [5, 4, 3])
user2 = Student('Eva', 44, [4, 5, 6])
students = [user2, user3, user]
students = student_sort(students)
for student in students:
    print(student)
