from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload
"""
создайте класс `Plane`, наследник `Vehicle`
"""


class Plane(Vehicle):

    cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        # self.weight = weight
        # self.fuel = fuel
        # self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo

    def load_cargo(self, box_of_cargo):
        if self.max_cargo - self.cargo >= box_of_cargo:
            self.cargo += box_of_cargo
            print("cargo =", self.cargo)
        else:
            raise CargoOverload("Not enough space")

    def remove_all_cargo(self):
        loaded_cargo = self.cargo
        self.cargo -= loaded_cargo
        return loaded_cargo
