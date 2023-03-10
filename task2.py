class AdjMatrix:
    def getBinary(self, studentId):
        studentId = str(studentId)
        binary = ''
        for i in range(len(studentId)):
            if int(studentId[i]) % 2 == 0:
                binary = binary + '0'
            else:
                binary = binary + '1'
        return binary

    def getPrimaryMatrix(self, binary):
        adjMatrix = []
        ptr = 0
        for i in range(27):
            temp = []
            for j in range(27):
                temp.append(int(binary[ptr]))
                ptr += 1
            adjMatrix.append(temp)
        return adjMatrix

    def eliminateIsolatedNodes(self, adjMatrix):
        m = len(adjMatrix)
        n = len(adjMatrix[-1])
        isolatedNodes = []
        for i in range(m):
            flag = False
            for j in range(n):
                if adjMatrix[i][j] == 1 or adjMatrix[j][i] == 1:
                    flag = True
                    break
            if not flag:
                isolatedNodes.append(i)
        for i in isolatedNodes:
            adjMatrix[i][0] = 1
            adjMatrix[i][-1] = 1
            adjMatrix[0][i] = 1
            adjMatrix[-1][i] = 1
        return adjMatrix

    def replaceMainDiagonal(self, adjMatrix):
        m = len(adjMatrix)
        for i in range(m):
            adjMatrix[i][i] = 0
        return adjMatrix

    def makeSymmetric(self, adjMatrix):
        m = len(adjMatrix)
        for i in range(m):
            for j in range(i + 1, m):
                adjMatrix[i][j] = adjMatrix[j][i]
        return adjMatrix

    def getAdjMatrix(self, studentId):
        # getting binary number of my studentId and multiplying it 73 times
        binary = self.getBinary(studentId)
        binary *= 73
        # getting primary matrix
        adjMatrix = self.getPrimaryMatrix(binary)
        adjMatrix = self.eliminateIsolatedNodes(adjMatrix)
        adjMatrix = self.replaceMainDiagonal(adjMatrix)
        adjMatrix = self.makeSymmetric(adjMatrix)
        return adjMatrix


if __name__ == "__main__":
    studentId = 2021582933
    adjMatrix = AdjMatrix().getAdjMatrix(studentId)
    print('AdjacencyMatrix from the studentId {0} is:'.format(studentId))
    print(adjMatrix)
