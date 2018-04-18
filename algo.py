from functools import reduce
import copy
import sys

def parseDot(path):
    f = open(path, "r")
    data = f.read().replace(" ", "").replace(";", "").split("\n")
    return data[1:len(data)-2]

def getMatrix(data):
    d = {}
    [d.update({chr(i): i-65}) for i in range(ord("A"), ord("Z")+1)]
    adjList = list(map(lambda x: x.split("->"), data))
    depth = len(set(reduce(lambda a, i: a + i, adjList)))
    graph = GetNullMatrix(depth)

    for i in adjList:
        graph[d[i[0]]][d[i[1]]] = 1

    return graph

def getIncoming(graph, n):
    incoming = []

    for i in range(len(graph)):
        if graph[i][n] == 1:
            incoming.append(i) 

    return incoming

def getOutcoming(graph, n):
    outcoming = []

    for i in range(len(graph)):
        if graph[n][i] == 1:
            outcoming.append(i)

    return outcoming

def getAdjacents(graph, n):
    adjacents = []

    for i in range(len(graph)):
        if graph[i][n] == 1 or graph[n][i]:
            adjacents.append(i)

    return adjacents

def GetNullMatrix(n):
    m = []

    for i in range(n):
        m.append([])
        for j in range(n):
            m[i].append(0)

    return m

def getAllPaths(graph):
    paths = []
    stack = []
    stack.append(0)
    path = []

    while stack:
        node = stack.pop()  
        outs = getOutcoming(graph, node)
        ins = getIncoming(graph,node)

        for i in list(reversed(path)):
            if not i in ins:
                path.pop()
            else:
                break

        path.append(node)

        if not outs:
            paths.append(copy.copy(path))
            path.pop()

        for n in outs:
            stack.append(n)

    return paths

def printAsLetters(paths):
    list(map(lambda P: print("".join(chr(i+65) for i in P)), paths))

def main():
    try:
        path = sys.argv[1]
        data = parseDot(path)
        graph = getMatrix(data)
        paths = getAllPaths(graph)
        printAsLetters(paths)

    except:
        print("Unexpected error")

if __name__ == "__main__":
    main()
