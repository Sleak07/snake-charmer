# Abstract classes in python and utilities
#
from abc import ABC, abstractmethod
from typing import override


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    @override
    def go(self):
        print("You can drive")

    @override
    def stop(self):
        print("You cannot go")


car = Car()
car.go()
car.stop()
