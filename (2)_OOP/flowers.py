"""A class that models flowers.

Created By: AJ Singh
Date: Feb 15, 2021
"""


class Flower:
    """A flower."""

    def __init__(self, name: str, petals: int, price: float):
        """Creates a new flower."""

        self.name = name
        self.petals = petals
        self.price = price

    def get_name(self):
        # print(self.name)
        return self.name

    def get_petals(self):
        # print(self.petals)
        return self.petals

    def get_price(self):
        # print(self.price)
        return self.price

    def set_name(self, new_name):
        self.name = new_name

    def set_petals(self, new_petals):
        self.petals = new_petals

    def set_price(self, new_price):
        self.price = new_price


if __name__ == "__main__":
    flower = Flower(name="Rose", petals=20, price=20.99)

    print(f"A {flower.get_name()} has {flower.get_petals()} petals, and is worth ${flower.get_price()}!")

    flower.set_name("Tulip")
    flower.set_petals(8)
    flower.set_price(9.95)

    print(f"A {flower.get_name()} has {flower.get_petals()} petals, and is worth ${flower.get_price()}!")
