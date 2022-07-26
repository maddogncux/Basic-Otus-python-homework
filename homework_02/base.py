from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                print("Engine turned ON")
                self.started = True
            else:
                self.started = False
                raise LowFuelError("need more fuel")

        if self.started:
            print("engine allready started.i will turn off it")
            self.started = self.started
        # else:
        #     print("engine turn OFF")
        #     self.started = False

    def move(self, move_range):
        if move_range * self.fuel_consumption <= self.fuel != 0:
            self.fuel -= move_range * self.fuel_consumption
            print("u reached destination", "fuel lvl:", self.fuel)
        else:
            raise NotEnoughFuel("Not enough Fuel")
