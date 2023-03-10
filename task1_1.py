from collections import defaultdict, deque


class Main1:
    def getEdges(self, adjMatrix):
        dictu = defaultdict(set)
        m = len(adjMatrix)
        n = len(adjMatrix[-1])
        for i in range(m):
            for j in range(n):
                if adjMatrix[i][j] == 1:
                    dictu[i].add(j)
        return dictu

    def getDegree(self, dictu):
        degree = {}
        for i in dictu:
            degree[i] = len(dictu[i])
        return degree

    def k_Core(self, adjMatrix, k):
        dictu = self.getEdges(adjMatrix)
        degree = self.getDegree(dictu)
        queue = deque()
        for i in degree:
            if degree[i] < k:
                queue.append(i)
        deleted = set()
        while queue:
            pop = queue.popleft()
            for i in dictu[pop]:
                dictu[i].remove(pop)
                degree[i] -= 1
                if degree[i] < k:
                    queue.append(i)
            del dictu[pop]
            deleted.add(pop)
        result = []
        for i in range(len(adjMatrix)):
            if i not in deleted:
                result.append(i)
        return result, list(deleted)


if __name__ == "__main__":
    adjMatrix = [[0, 1, 1, 1, 0, 0, 0, 0], [1, 0, 1, 1, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1, 0, 0],
                 [0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 0, 1, 1, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0]]
    k = 3
    result = Main1().k_Core(adjMatrix, k)
    print('deleted nodes are:', result[1])
    print('nodes that are in {0}-core of the graph are: '.format(k), end="")
    print(result[0])
