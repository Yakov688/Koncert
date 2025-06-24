from abc import ABC, abstractmethod
from math import pi
from typing import List


class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount: int):
        self.__balance += amount
        return "Баланс счета пополнен"

    def get_balance(self):
        return f"Текущий баланс счета {self.__balance}"

    def withdraw(self, amount):
        if self.__balance - amount < 0:
            return "Недостаточно средств"
        return f"Остаток средств {self.__balance - amount}"


class Employee:
    def __init__(self, name: str, position: str, salary: int):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        print(f'My name is {self.name} and my current position is {self.position}')


class Developer(Employee):
    def __init__(self, programming_language: str, name: str, position: str, salary: int):
        super().__init__(name, position, salary)
        self.programming_language = programming_language

    def get_info(self):
        super().get_info()
        print(f'My favorite programming language is {self.programming_language}\n')

#
# dev = Developer('Python', 'Yakov', 'developer', 150000)
# dev.get_info()


class Manager(Employee):
    def __init__(self, employees: List[str], name: str, position: str, salary: int):
        super().__init__(name, position, salary)
        self.employees = employees

    def get_info(self):
        super().get_info()
        print(f'I\'m managering these people {" ".join(self.employees)}')


# manager = Manager(['Sasha, Vasya'], 'Kirill', 'manager', 12000)
# manager.get_info()
# print()


class Shape:
    def area(self):
        return 0

    def perimetr(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimetr(self):
        return (self.width + self.height) * 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimetr(self):
        return 2 * pi * self.radius


rectangle = Rectangle(5, 10)
circle = Circle(7)


def area(figure):
    return figure.area()


def perimetr(figure):
    return figure.perimetr()


for i in [rectangle, circle]:
    print(area(i))
print()

for i in [rectangle, circle]:
    print(perimetr(i))
print()


class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Car(Transport):
    def start_engine(self):
        return 'Двигатель машины завелся'

    def stop_engine(self):
        return 'Двигатель машины заглушен'

    def move(self):
        return 'Машина поехала'


class Boat(Transport):
    def start_engine(self):
        return 'Двигатель лодки завелся'

    def stop_engine(self):
        return 'Двигатель лодки заглушен'

    def move(self):
        return 'Лодка поехала'

#
# car = Car()
# print(car.move())
# print(car.stop_engine())
# print()
#
# boat = Boat()
# print(boat.start_engine())
# print(boat.move())


class Flyable:
    @staticmethod
    def fly():
        return 'I\'m flying'


class Swimmable:
    @staticmethod
    def swim():
        return 'I\'m swimming'


class Duck(Flyable, Swimmable):
    @staticmethod
    def make_sound():
        return 'Quack!'


duck = Duck()
print(duck.swim())
print(duck.fly())
print(duck.make_sound())
print()


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def move(self):
        return 'Собака (бежит)'

    def speak(self):
        return 'Woof!'


class Bird(Flyable, Animal):
    def move(self):
        return self.fly()

    def speak(self):
        return 'Tweet!'


class Fish(Swimmable, Animal):
    def move(self):
        return self.swim()

    def speak(self):
        return '*Тишина*'


animals = [Dog(), Fish(), Bird()]
for animal in animals:
    print(animal.move())
    print(animal.speak())
    print()
