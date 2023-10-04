from collections import deque


class Undirected:
    def __int__(self, open, closed):
        self.openStack= open
        self.closedList = closed

    #following textbook definition of undirected search, basic implementation same as DFS
    #following outside definitions of undirected search, would find all possible combinations and then identify first one
    #this implementation follows the textbook definition
    def undirected(dictionary, start, goal):
        #although open is list type, functions performed cause it to act like stack
        open = []
        closed = []
        open.append(start)
        while len(open) != 0:
            current = open.pop()
            closed.append(current)
            if current == goal:
                print("Success")
                print(list(closed))
                return True
            else:
                children = dictionary[current]
                for i in children:
                    inClosed = False
                    for j in closed:
                        if i[0] == j:
                            inClosed = True
                            break
                    if (not inClosed):
                        open.append(i[0])
        print("Fail")
        return "fail"


class IDDFS:
    def __init__(self, open, closed):
        self.openStack = open
        self. closedList = closed

    def iddfs(dictionary, start, goal):
        #although open is list type, functions performed cause it to act like stack
        open = []
        closed = []
        open.append(start)
        level = 1
        i = 0
        while len(open) != 0:
            i = 0
            #evaluates nodes and children through one level of tree at a time
            while i != level:
                current = open.pop()
                closed.append(current)
                if current == goal:
                    print("Success")
                    print(list(closed))
                    return "Success"
                else:
                    children = dictionary[current]
                    for j in children:
                        inClosed = False
                        for k in closed:
                            if j[0] == k:
                                inClosed = True
                                break
                        if (not inClosed):
                            open.append(j[0])
                i += 1
            level += 1
        print("Failure")
        return "Failure"


class DepthFirst:
    def __init__(self, open, closed):
        self.openStack = open
        self.closedList = closed

    def depthFirst(dictionary, start, goal):
        #although open is list type, functions performed cause it to act like stack
        open = []
        closed = []
        open.append(start)
        while len(open) != 0:
            current = open.pop()
            closed.append(current)
            if current == goal:
                print("Success")
                print(list(closed))
                return True
            else:
                children = dictionary[current]
                for i in children:
                    inClosed = False
                    for j in closed:
                        if i[0] == j:
                            inClosed = True
                            break
                    if (not inClosed):
                        open.append(i[0])
        print("Fail")
        return "fail"


class BreadthFirst:
    def __init__(self, open, closed):
        self.openQueue = open
        self.closedList = closed

    def breadthFirst(dictionary, start, goal):
        open = deque()
        closed = []
        open.append(start)
        while len(open) != 0:
            current = open.popleft()
            closed.append(current)
            if current == goal:
                print("Success")
                print(list(closed))
                return "success"
            else:
                children = dictionary[current]
                for i in children:
                    inClosed = False
                    for j in closed:
                        if i[0] == j:
                            inClosed = True
                            break
                    if (not inClosed):
                        open.append(i[0])
        print("Fail")
        return "fail"


class BestFirst:
    def __init__(self, open, closed):
        self.openQueue = open
        self.closedList = closed

    #allows .sort() to sort elements by element in first index
    def sortKey(node):
        return node[1]

    def bestFirst(dictionary, start, goal):
        #although open is list type, functions performed cause it to act like a queue
        open = []
        closed = []
        open.append(start)
        current = open[0]
        while len(open) != 0:
            if goal == current:
                closed.append(current)
                print("Success")
                print(list(closed))
                return True
            if goal in current:
                closed.append(current[0])
                print(list(closed))
                return True
            else:
                #checks to see if current is of string type
                #if so, get full information from dictionary
                if isinstance(current, str) == True:
                    children = dictionary[current]
                else:
                    children = dictionary[current[0]]
                for i in children:
                    if (i in open):
                        continue
                    if (i[0] in closed):
                        continue
                    else:
                        open.append(i)
                if isinstance(current,str) == True:
                    closed.append(current)
                else:
                    closed.append(current[0])
                open.remove(current)
                open.sort(key = BestFirst.sortKey)
                current = open[0]
        return "Failure"


class AStar:
    def __init__(self, open, closed):
        self.openQueue = open
        self. closedList = closed

    #allows .sort() to sort elements by element in first index
    def sortKey(node):
        return node[1]

    def aStar(dictionary, start, goal):
        #although open is list type, functions performed cause it to act like queue
        open = []
        closed = []
        startList = [start, 0]
        open.append(startList)
        while len(open) != 0:
            current = open[0]
            closed.append(current[0])
            open.remove(current)
            if current[0] == goal:
                print("Success")
                print (list(closed))
                return True
            else:
                children = dictionary[current[0]]
                #creates a copy of the children to not alter the values in dictionary
                children = children.copy()
                for i in children:
                    #finds the sum of the current node and the child node
                    i[1] = current[1] + i[1]
                    if i in open:
                        continue
                    if i[0] in closed:
                        continue
                    else:
                        open.append(i)
                open.sort(key = AStar.sortKey)
        print("Failure")
        return "Failure"