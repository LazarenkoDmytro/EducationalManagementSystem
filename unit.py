# Program Name: Unit Class
# Description: This program defines a Unit class that represents a course unit.
#              It includes methods to generate a unique unit ID and check if a unit ID exists.

import random
import os


class Unit:
    def __init__(self, unit_id=None, unit_code=None, unit_name=None, unit_capacity=0):
        """
        Initialize a new Unit object with the given parameters. If no unit_id is provided,
        generate a unique unit ID using the generate_unit_id method.
        """
        if unit_id is None:
            self.unit_id = self.generate_unit_id()
        else:
            self.unit_id = unit_id
        self.unit_code = unit_code
        self.unit_name = unit_name
        self.unit_capacity = unit_capacity

    def __str__(self):
        """
        Return a string representation of the Unit object.
        """
        return f"{self.unit_id}, {self.unit_code}, {self.unit_name}, {self.unit_capacity}"

    def generate_unit_id(self):
        """
        Generate a unique unit ID by randomly selecting a 7-digit number between 1000000 and 9999999,
        and checking if it already exists in the "data/unit.txt" file using the check_unit_id_exists method.
        If the unit ID is unique, return it.
        """
        while True:
            unit_id = random.randint(1000000, 9999999)
            if not self.check_unit_id_exists(unit_id):
                return unit_id

    @staticmethod
    def check_unit_id_exists(unit_id):
        """
        Check if the given unit ID already exists in the "data/unit.txt" file.
        If it does, return True. Otherwise, return False.
        """
        if os.path.exists("data/unit.txt"):
            with open("data/unit.txt", "r", encoding='utf-8') as file:
                for line in file.readlines():
                    if str(unit_id) == line.strip().split(", ")[0]:
                        return True
        return False
