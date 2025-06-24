from abc import ABC, abstractmethod


# Принцип разделения ответственности
class Content:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class PDF:
    def generate_pdg(self):
        print('PFG generated')


class File:
    def save_to_file(self, filename):
        print(f'Saved {filename}')


# Принцип открытости/закрытости
class PaymentMethod(ABC):
    @abstractmethod
    def current_method(self):
        pass


class PayPal(PaymentMethod):
    def current_method(self):
        return 'PayPal'


class CreditCard(PaymentMethod):
    def current_method(self):
        return 'CreditCard'


class Crypto(PaymentMethod):
    def current_method(self):
        return 'Crypto'


class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def pay(self):
        return f'Сейчас буду оплачивать с помощью {self.payment_method.current_method()}'


payment1 = PaymentProcessor(payment_method=CreditCard())
payment2 = PaymentProcessor(payment_method=PayPal())
payment3 = PaymentProcessor(payment_method=Crypto())
print(payment1.pay())
# print(payment3.pay())
# print(payment2.pay())


# Принцип подстановки Барбары Лисков
class Bird(ABC):
    @abstractmethod
    def explanation(self):
        pass


class Sparrow(Bird):
    def explanation(self):
        return 'I\'m Sparrow'


class Pinguin(Bird):
    def explanation(self):
        return 'I\'m Pinguin'


sparrow = Sparrow()
print(sparrow.explanation())

pinguin = Pinguin()
print(pinguin.explanation())


# Принцип разделения интерфейса
class RunningAnimal(ABC):
    @abstractmethod
    def run(self):
        pass


class FlyingAnimal(ABC):
    @abstractmethod
    def fly(self):
        pass


class SwimmingAnimal(ABC):
    @abstractmethod
    def swim(self):
        pass


class Lion(RunningAnimal):
    def run(self):
        return 'Лев (бежит)'


class Duck(FlyingAnimal, SwimmingAnimal):
    def fly(self):
        return 'Утка летит'

    def swim(self):
        return 'Утка плывет'


lion = Lion()
print(lion.run())

duck = Duck()
print(duck.swim(), duck.fly())


# classmethod, property,staticmethod
class Temperature:
    def __init__(self, temperature: float):
        self.temperature = temperature

    @staticmethod
    def is_freezing(your_temperature):
        if your_temperature < 0:
            return 'Water will freeze'
        return 'Water will not freeze'

    @property
    def celsius_to_kelvin(self):
        return self.temperature + 273.15

    @classmethod
    def celsius_to_fahrenheit(cls, temperature):
        return (temperature * 9 / 5) + 32


tmp = Temperature(16)
print(Temperature.celsius_to_fahrenheit(15))
