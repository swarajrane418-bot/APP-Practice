from abc import ABC, abstractmethod

# Base class
class Bird:
    def eat(self):
        print("Bird is eating")


# Interface for flying birds
class FlyingBird(ABC):
    @abstractmethod
    def fly(self):
        pass


class Sparrow(Bird, FlyingBird):
    def fly(self):
        print("Sparrow is flying")


class Eagle(Bird, FlyingBird):
    def fly(self):
        print("Eagle is flying")


class Penguin(Bird):
    def swim(self):
        print("Penguin is swimming")


# Usage
sparrow = Sparrow()
sparrow.eat()
sparrow.fly()

penguin = Penguin()
penguin.eat()
penguin.swim()