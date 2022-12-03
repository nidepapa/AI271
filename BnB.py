import copy


class Node:
    def __init__(self, matrix, new_path, new_level, i, j):
        self.path = new_path
        #todo verify this value
        self.cost = float("inf")
        self.number = j
        self.level = new_level
        self.reducedMatrix = copy.deepcopy(matrix)

        self.reducedMatrix[i][j] = float("inf")
        for k in range(len(self.reducedMatrix)):
            self.reducedMatrix[i][k] = float("inf")
            self.reducedMatrix[k][j] = float("inf")


def BnB_DFS_TSP():