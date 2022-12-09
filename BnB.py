import copy
import heapq
import time
from typing import List

# the dimension of matrix
import util

N = 0


class Node:
    def __init__(self, matrix, new_path, new_level, i, j):
        self.cost = 0
        # assign current city number
        self.number = j
        self.level = new_level
        self.reducedMatrix = copy.deepcopy(matrix)
        self.path = copy.copy(new_path)
        if self.level != 0:
            # update path and matrix
            self.path.append(j)
            # todo not sure
            self.reducedMatrix[j][i] = float("inf")
            for k in range(N):
                self.reducedMatrix[i][k] = float("inf")
                self.reducedMatrix[k][j] = float("inf")

    def __lt__(self, other):
        if self.cost < other.cost:
            return True
        else:
            return False

    def colReduction(self) -> List[float]:
        col = [float("inf")] * N
        # get the min of each col
        for i in range(N):
            for j in range(N):
                if col[j] > self.reducedMatrix[i][j]:
                    col[j] = self.reducedMatrix[i][j]
        # reduce the minimum value from each element in each row
        for i in range(N):
            for j in range(N):
                if self.reducedMatrix[i][j] != float("inf") and col[j] != float("inf"):
                    self.reducedMatrix[i][j] -= col[j]
        return col

    def rowReduction(self) -> List[float]:
        row = [float("inf")] * N
        # get the min of each row
        for i in range(N):
            for j in range(N):
                if row[i] > self.reducedMatrix[i][j]:
                    row[i] = self.reducedMatrix[i][j]
        # reduce the minimum value from each element in each row
        for i in range(N):
            for j in range(N):
                if self.reducedMatrix[i][j] != float("inf") and row[i] != float("inf"):
                    self.reducedMatrix[i][j] -= row[i]
        return row

    def calculateCost(self) -> float:
        cost = 0
        row = self.rowReduction()
        col = self.colReduction()
        for i in range(N):
            cost += row[i] if row[i] != float("inf") else 0
            cost += col[i] if col[i] != float("inf") else 0
        return cost


def generateMatrix(cities: List[util.City]) -> List[List[int]]:
    matrix = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            matrix[i][j] = cities[i].distTo(cities[j]) if i != j else float("inf")
    return matrix


def BnB_DFS_TSP(matrix):
    global N
    N = len(matrix)
    expandingNum = -1

    #[node]
    heap = []
    path = [0]
    root = Node(matrix, path, 0, -1, 0)
    root.cost = root.calculateCost()

    heapq.heappush(heap, root)

    while heap:
        expandingNum += 1
        minNode = heapq.heappop(heap)

        i = minNode.number
        # if all cities are visited
        if minNode.level == N - 1:
            return minNode.cost, expandingNum

        for j in range(N):
            if minNode.reducedMatrix[i][j] != float("inf"):
                # expand
                child = Node(minNode.reducedMatrix, minNode.path, minNode.level + 1, i, j)
                child.cost = minNode.cost + minNode.reducedMatrix[i][j] + child.calculateCost()
                heapq.heappush(heap, child)



