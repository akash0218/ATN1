from collections import defaultdict


class Node:
    def __init__(self, key, value, degree):
        self.prev = None
        self.key = key
        self.value = value
        self.degree = degree
        self.next = None


class DlLinkedList:
    def __init__(self, val):
        self.head = Node(-1, -1, val)
        self.tail = Node(-1, -1, val)
        self.head.next = self.tail
        self.tail.prev = self.head


class Main:
    def createAdjMatrix(self, m, dictu, adjMatrix):
        for i in range(m):
            for j in range(m):
                if adjMatrix[i][j] == 1:
                    dictu[i].add(j)

    def createDegree(self, degree, dictu):
        for i in dictu:
            degree[len(dictu[i])].append(i)

    def createLinkedList(self, temp, final, degree, dictu, n_dictu):
        head = DlLinkedList(-1)
        for i in range(len(temp)):
            dll = DlLinkedList(temp[i])
            if temp[i] not in final:
                final[temp[i]] = dll
            for j in degree[temp[i]]:
                node = Node(j, dictu[j], len(dictu[j]))
                n_dictu[j] = node
                node.next = dll.tail
                node.prev = dll.tail.prev
                node.prev.next = node
                node.next.prev = node
            if i == 0:
                dll.tail.next = head.tail
                dll.head.prev = head.head
                head.head.next = dll.head
                head.tail.prev = dll.tail
            else:
                dll.tail.next = head.tail
                dll.head.prev = head.tail.prev
                dll.head.prev.next = dll.head
                head.tail.prev = dll.tail
        return head

    def delete(self, node, degree, final):
        if node.prev.value == -1 and node.next.value == -1:
            if node.prev.prev:
                node.prev.prev.next = node.next.next
            if node.next.next:
                node.next.next.prev = node.prev.prev
            node.next.next = None
            node.prev.prev = None
            del degree[node.degree]
            del final[node.degree]
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = None

    def k_Core(self, adjMatrix, k):
        m = len(adjMatrix)
        dictu = defaultdict(set)
        degree = defaultdict(list)

        # creating adjMatrix dictionary
        self.createAdjMatrix(m, dictu, adjMatrix)

        # creating degree dictionary
        self.createDegree(degree, dictu)

        temp = list(degree.keys())
        temp.sort()
        final = {}
        n_dictu = {}

        # creating LinkedList
        head = self.createLinkedList(temp, final, degree, dictu, n_dictu)

        deleted = set()

        # k_core algorithm
        while head.head.next.degree < k and len(deleted) < m:
            key = head.head.next.next.key
            deleted.add(key)
            for i in dictu[key]:
                tail = None
                next = None
                node = n_dictu[i]
                dictu[i].remove(key)
                if node.prev.value == -1 and node.next.value == -1:
                    if node.prev.prev:
                        tail = node.prev.prev
                    if node.next.next:
                        next = node.next.next
                self.delete(node, degree, final)
                prev = node.degree
                node.degree -= 1
                if node.degree not in final:
                    dll = DlLinkedList(node.degree)
                    final[node.degree] = dll
                    node.next = dll.tail
                    node.prev = dll.tail.prev
                    node.prev.next = node
                    node.next.prev = node
                    if tail and head:
                        dll.head.prev = tail
                        dll.tail.next = next
                        tail.next = dll.head
                        next.prev = dll.tail
                    else:
                        dll.tail.next = final[prev].head
                        dll.head.prev = final[prev].head.prev
                        final[prev].head.prev.next = dll.head
                        final[prev].head.prev = dll.tail
                else:
                    node.next = final[node.degree].head.next
                    node.prev = final[node.degree].head
                    node.next.prev = node
                    node.prev.next = node
                degree[node.degree].append(node.key)
            node = n_dictu[key]
            self.delete(node, degree, final)
            del dictu[key]
        result = []
        deleted = list(deleted)
        deleted.sort()
        for i in range(m):
            if i not in deleted:
                result.append(i)
        return result, deleted


if __name__ == "__main__":
    adjMatrix = [[0, 1, 1, 1, 0, 0, 0, 0], [1, 0, 1, 1, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1, 0, 0],
                 [0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 0, 1, 1, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0]]
    k = 3
    result = Main().k_Core(adjMatrix, k)
    print('deleted nodes are:', result[1])
    print('nodes that are in {0}-core of the graph are: '.format(k), end="")
    print(result[0])
