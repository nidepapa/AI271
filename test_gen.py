import math
import sys
import random

def generateCities(num):
    created = []
    for i in range(num):
        # create different cities
        while 1:
            x = random.randint(0, num * 2)
            y = random.randint(0, num * 2)
            if (x, y) not in created:
                break
        created.append([x, y])
    return created

def eucledian_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def generateMatrix(num):
    cities = generateCities(num)
    distance_matrix = [[0]*num]*num
    print(num)
    for i in range(num):
        for j in range(num):
            distance_matrix[i][j] = eucledian_distance(cities[i], cities[j])
        print(*distance_matrix[i])

if len(sys.argv) != 2:
    raise Exception("Invalid usage, use as : test_gen.py <number of cities>")

n = int(sys.argv[1])
generateMatrix(n)
