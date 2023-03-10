import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from task2 import AdjMatrix


class Plot:
    def plotting(self, adjMatrix):
        matplotlib.use('TkAgg')

        adj_matrix = np.array(adjMatrix)

        G = nx.from_numpy_array(adj_matrix)
        nx.draw(G, with_labels=True)
        plt.show()


if __name__ == '__main__':
    adjMatrix = AdjMatrix().getAdjMatrix(2021582933)
    Plot().plotting(adjMatrix)
