import typing
import sys
import random
import copy
import math

class World(object):
    def __init__(self):
        self.city_count = 0
        # This is n*n matrix, each row represents distances
        # of city i to all other citites.
        self.distance_vector = []

    def len(self):
        return self.city_count

    def construct(self):
        self.city_count = int(input("Number of cities : "))
        for city in range(self.city_count):
            self.distance_vector.append(
                    list(map(int,
                        input("Distances of city "
                            + str(city) + " to other cities : ").split())))

    def construct(self, file_name):
        file = open(file_name, 'r')
        line = file.readline()
        self.city_count = int(line)
        for city in range(self.city_count):
            line = file.readline()
            self.distance_vector.append(list(map(float, line.split())))

    def print(self):
        print(self.distance_vector)

    def distance(self, city1, city2):
        if city1 >=0 and city1 < self.city_count and city2 >=0 and city2 < self.city_count:
            return self.distance_vector[city1][city2]
        return -1

class Tour(object):
    # This represents a valid solution to TSP.
    # It contains a list of Cities, representing the order in the final path.
    def __init__(self, cities: typing.List[int], world: World) -> None:
        self.cities = cities
        self.world = world
        self.n = len(cities)

    def fitness(self):
        cost = 0
        for i in range(self.n):
            cost += world.distance(self.cities[i],
                                   self.cities[(i+1) % self.n])
        return cost

    def gen_neighbour(self):
        l = random.randint(2, self.n - 1)
        i = random.randint(0, self.n - l)
        cities = copy.deepcopy(self.cities)
        cities[i : (i+l)] = reversed(cities[i : (i+l)])
        return Tour(cities, self.world)

class SlsSolver(object):
    def __init__(self, world):
        if not isinstance(world, World):
            raise Exception("Invalid type of paramter")
        self.world = world
        self.n = world.len()
        self.city_nodes = list(range(self.n))
        self.alpha = 0.999
        self.T = 1000
        self.min_T = 1e-8
        self.max_iter = 100000

    def gen_initial_solution(self):
        curr_node = random.choice(self.city_nodes)
        tour = [curr_node]
        visited = [0]*self.n
        visited[curr_node] = 1

        while sum(visited) < self.n:
            distance = 10 ** 20
            next_node = -1
            for i in range(self.n):
                if visited[i] == 0 and self.world.distance(i, curr_node) < distance:
                    distance = self.world.distance(i, curr_node)
                    next_node = i
            tour.append(next_node)
            visited[next_node] = 1
            curr_node = next_node

        tour = Tour(tour, world)
        return tour

    def solve(self):
        curr_solution = self.gen_initial_solution()
        initial_solution = curr_solution
        initial_fitness = initial_solution.fitness()
        best_solution = curr_solution
        iterations = 0

        while self.T >= self.min_T and iterations < self.max_iter:
            next_solution = curr_solution.gen_neighbour()
            curr_fitness = curr_solution.fitness()
            next_fitness = next_solution.fitness()
            if next_fitness < curr_solution.fitness():
                curr_solution = next_solution
                if next_fitness < best_solution.fitness():
                    best_solution = next_solution
            else:
                if random.random() < math.exp(-abs(next_fitness - curr_fitness) / self.T):
                    curr_solution = next_solution
            self.T *= self.alpha
            iterations += 1

        best_fitness = best_solution.fitness()

        print("Initial solution : ", initial_solution)
        print("Initial fitness : ", initial_fitness)
        print("Best solution : ", best_solution)
        print("Best fitness : ", best_fitness)
        print("Total iterations : ", iterations)
        print("Best solution over initial solution improvement: ", 100 * (initial_fitness - best_fitness) / initial_fitness)

        return best_fitness

world = World()
if len(sys.argv) == 2:
    world.construct(sys.argv[1])
else:
    world.construct()

avg = 0
count = 0
for i in range(100):
    count += 1
    avg = avg*(count-1) + SlsSolver(world).solve()
    avg /= count

print("Average best tour cost : ", avg)
