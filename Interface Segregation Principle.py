from abc import ABC, abstractmethod

# Small interface for working
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


# Small interface for eating
class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class HumanWorker(Workable, Eatable):
    def work(self):
        print("Human is working")

    def eat(self):
        print("Human is eating")


class RobotWorker(Workable):
    def work(self):
        print("Robot is working")


# Usage
human = HumanWorker()
human.work()
human.eat()

robot = RobotWorker()
robot.work()