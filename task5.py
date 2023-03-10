import random
import time

from task2 import AdjMatrix
from task3 import Simulate
from task4 import Plot


class Experiment:
    def getEdges(self, adjMatrix, k):
        result = []
        for i in range(len(adjMatrix)):
            for j in range(len(adjMatrix)):
                if adjMatrix[i][j] == 1:
                    adjMatrix[i][j] = 0
                    adjMatrix[j][i] = 0
                    K = Simulate().simualtion(adjMatrix, False)
                    if K != k:
                        result.append((i, j))
                    adjMatrix[i][j] = 1
                    adjMatrix[j][i] = 1
        return result

    def change(self, adjMatrix, edge, flag):
        if flag:
            adjMatrix[edge[0]][edge[1]] = 0
            adjMatrix[edge[1]][edge[0]] = 0
        else:
            adjMatrix[edge[0]][edge[1]] = 1
            adjMatrix[edge[1]][edge[0]] = 1
        return adjMatrix

    def simulate(self, adjMatrix):
        # task_3
        Simulate().simualtion(adjMatrix, True)
        # task_4
        Plot().plotting(adjMatrix)

    def Experimentation(self, adjMatrix, k):
        lst = self.getEdges(adjMatrix, k)
        print('list of edges, when deleted that makes graph from {0}-core to {1}-core are:'.format(k-1, k-2))
        print(lst)

        time.sleep(2)

        # randomly picking 2 edges
        int_1 = random.randrange(0, len(lst))
        while True:
            int_2 = random.randrange(0, len(lst))
            if int_1 != int_2:
                break

        edges = [lst[int_1], lst[int_2]]
        print(edges)
        for edge in edges:
            adjMatrix = self.change(adjMatrix, edge, True)
            adjMatrix = self.change(adjMatrix, edge, False)
            self.simulate(adjMatrix)


if __name__ == '__main__':
    adjMatrix = AdjMatrix().getAdjMatrix(2021582933)
    k = Simulate().simualtion(adjMatrix, False)
    Experiment().Experimentation(adjMatrix, k)
