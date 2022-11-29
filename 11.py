class Car(object):

    def __init__(
            self,
            color: str,
            count_passenger_seats: int,
            is_baby_seat: bool
    ) -> None:
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self) -> str:
        return f'Car: {self.color=} {self.count_passenger_seats} {self.is_baby_seat=} {self.is_busy=}'


class Taxi(object):

    def __init__(self, cars: list[Car]) -> None:
        self.cars = cars

    def find_car(self, count_passengers: int, is_baby: bool) -> Car | None:
        for car in self.cars:
            if not car.is_busy and car.count_passenger_seats >= count_passengers:
                if is_baby and car.is_baby_seat:
                    car.is_busy = True
                    return car
                elif not is_baby:
                    car.is_busy = True
                    return car


# car1 = Car(color='black', count_passenger_seats=5, is_baby_seat=True)
# car2 = Car(color='white', count_passenger_seats=4, is_baby_seat=False)
# car3 = Car(color='red', count_passenger_seats=5, is_baby_seat=False)
# cars = [car1, car2, car3]
# taxi = Taxi(cars=cars)
# print(taxi.find_car(5, True))
# print(taxi.find_car(4, False))
# print(taxi.find_car(4, False))
# print(taxi.find_car(4, False))

class Category(object):

    categories: list[str] = []

    @classmethod
    def add(cls, category: str) -> int:
        category = category.title()
        if category in cls.categories:
            raise ValueError('category is  not unique')
        cls.categories.append(category)
        return cls.categories.index(category)
        # return len(cls.categories) - 1

    @classmethod
    def get(cls, pk: int) -> str:
        try:
            return cls.categories[pk]
        except IndexError as e:
            raise ValueError(e)

    @classmethod
    def delete(cls, pk: int) -> None:
        try:
            del cls.categories[pk]
        except IndexError:
            ...  # pass

    @classmethod
    def update(cls, pk: int, new_category_name: str):
        new_category_name = new_category_name.title()
        if new_category_name in cls.categories:
            raise ValueError('category is not unique')
        try:
            cls.get(pk=pk)
        except ValueError:
            cls.add(category=new_category_name)
        else:
            cls.categories[pk] = new_category_name
