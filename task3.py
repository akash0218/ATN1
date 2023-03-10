from task1 import Main
from task1_1 import Main1
from task2 import AdjMatrix
from task4 import Plot


class Simulate:
    def simualtion(self, adjMatrix, flag):
        k = 1
        while True:
            result_1 = Main1().k_Core(adjMatrix, k)
            result_2 = Main().k_Core(adjMatrix, k)
            if len(result_1[0]) > 0 and len(result_2[0]) > 0:
                if flag:
                    print()
                    print('Method-1: Using Breadth First Search')
                    print('deleted nodes are:', result_1[1])
                    print('nodes that are in {0}-core of the graph are: '.format(k), end="")
                    print(result_1[0])
                    print()
                    print('Method-2: Using LinkedLists')
                    print('deleted nodes are:', result_2[1])
                    print('nodes that are in {0}-core of the graph are: '.format(k), end="")
                    print(result_2[0])
            else:
                break
            k += 1
        if flag:
            print()
            print('Given adjMatrix is {0}-core.'.format(k-1))
            return 'in {0}-core the k-core algorithm produced empty k-cores.'.format(k)
        return k


if __name__ == "__main__":
    adjMatrix = AdjMatrix().getAdjMatrix(2021582933)
    print(Simulate().simualtion(adjMatrix, True))
