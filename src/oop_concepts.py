from abc import ABC, abstractmethod
from typing import List

class Animal(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def make_sound(self) -> str:
        pass

class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof!"

class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow!"

class Vehicle:
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model

    def __str__(self) -> str:
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand: str, model: str, num_doors: int) -> None:
        super().__init__(brand, model)
        self.num_doors = num_doors

    def __str__(self) -> str:
        return f"{super().__str__()} with {self.num_doors} doors"

# Instantiate objects
dog: Animal = Dog("Buddy")
cat: Animal = Cat("Whiskers")

# Polymorphism
animals: List[Animal] = [dog, cat]
for animal in animals:
    print(f"{animal.name} says: {animal.make_sound()}")

# Inheritance and method overriding
car: Vehicle = Car("Toyota", "Camry", 4)
print(f"Car: {car}")

# Property decorator
class Temperature:
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return (self.celsius * 9/5) + 32

temp: Temperature = Temperature(25)
print(f"Temperature: {temp.celsius}°C, {temp.fahrenheit}°F")
temp.celsius = 30
print(f"New temperature: {temp.celsius}°C, {temp.fahrenheit}°F")