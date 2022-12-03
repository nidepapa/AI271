import math
import typing
from random import random


class City(object):
    # This maintains the x and y coordinates of a city.
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def distTo(self, city2) -> int:
        # city2 is another City object.
        return int(math.sqrt((self.x - city2.x) ** 2 + (self.y - city2.y) ** 2))


class Tour(object):
    # This represents a valid solution to TSP.
    # It contains a list of Cities, representing the order in the final path.
    def __init__(self, cities: typing.List[City]) -> None:
        self.cities = cities  # list of City objects

    def cost(self) -> int:
        # Cost of the Tour
        # returns cost of city[0].distTo(city[1]) + city[1].distTo(city[2]) + … city[-1].distTo(city[0])
        res = 0
        for i in range(len(self.cities) - 1):
            res += self.city[i].distTo(self.city[i + 1])
        return res * 2

    def twoOpt(self) -> None:
        idx1 = random.randint(0, len(self.cities))
        idx2 = random.randint(0, len(self.cities))
        while idx1 == idx2:
            idx2 = random.randint(0, len(self.cities))
        self.cities[idx1], self.cities[idx2] = self.cities[idx2], self.cities[idx1]

    def translate(self, idx: typing.List[int]) -> None:
        # change the order of cities in this object. Ex : Cities : [A, B, C] translate(2, 1, 0) will change it to [C,
        # B, A]
        route = []
        for i in idx:
            route.append(self.cities[i])
        self.cities = route
