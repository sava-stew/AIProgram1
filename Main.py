import math
from timeit import default_timer as timer

from SearchMethods import DepthFirst, BreadthFirst, BestFirst, IDDFS, AStar, Undirected

def readFiles(fileName):
    my_file = open(fileName, "r")
    file = my_file.read()
    fileList = file.split("\n")
    my_file.close()

    return fileList

def split(info):
    return info.split()

def propogateDict(key, value, dictionary):
    if key in dictionary:
        values = dictionary[key]
        if value in values:
            pass
        else:
            values.append(value)
            dictionary[key] = values
    else:
        values = []
        values.append(value)
        dictionary[key] = values

#used following stackoverflow article for findDistance function
#https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula
def findDistance(lat1, long1, lat2, long2):
    R = 6371
    dLat = deg2rad(lat1-lat2)
    dLong = deg2rad(long1-long2)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * math.sin(dLong/2) * math.sin(dLong/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = (R * c)/0.621371
    return d

#used following stackoverflow article for deg2rad function
#https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula
def deg2rad(deg):
    return deg * (math.pi/180)

if __name__ == '__main__':
    places = readFiles("Adjacencies.txt")
    coordinates = readFiles("coordinates.csv")

    placeInfo = {}
    coordinateInfo= {}

    splitPlaces = map(split, places)

    for i in list(splitPlaces):
        propogateDict(i[0], i[1], placeInfo)
        propogateDict(i[1], i[0], placeInfo)

    splitCoordinates = []
    for i in coordinates:
        info = i.split(",")
        splitCoordinates.append(info)
    del splitCoordinates[-1]

    for i in list(splitCoordinates):
        propogateDict(i[0], i[1], coordinateInfo)
        propogateDict(i[0], i[2], coordinateInfo)

    for i in placeInfo:
        valDistance = []
        for j in placeInfo[i]:
            placeDistance = []
            placeDistance.append(j)
            place1 = coordinateInfo[i]
            place2 = coordinateInfo[j]
            lat1 = float(place1[0])
            long1 = float(place1[1])
            lat2 = float(place2[0])
            long2 = float(place2[1])
            distance = findDistance(lat1, long1, lat2, long2)
            placeDistance.append(distance)
            valDistance.append(placeDistance)
        placeInfo[i] = valDistance

    print("Hello!")
    start = input("Please enter your starting city, substituting spaces with underscores: ")
    goal = input("Please enter your goal ending city, substituting spaces with underscores: ")
    userGo = 'y'
    while userGo != 'n':
        print("1 - Undirected \n"
              "2 - Depth-First \n"
              "3 - Breadth-First \n"
              "4 - IDDFS \n"
              "5 - Best-First \n"
              "6 - A*" )
        searchMethod = input("Please select one of the following search methods to calculate your route: ")

        if searchMethod == "1":
            startTime = timer()
            Undirected.undirected(placeInfo, start, goal)
            endTime = timer()
            print("Time to execute: ", (endTime - startTime), " seconds")
        if searchMethod == "2":
            startTime = timer()
            DepthFirst.depthFirst(placeInfo, start, goal)
            endTime = timer()
            print("Time to execute: ", (endTime - startTime), " seconds")
        if searchMethod == "3":
            startTime = timer()
            BreadthFirst.breadthFirst(placeInfo, start, goal)
            endTime = timer()
            print("Time to execute: ", (endTime - startTime), " seconds")
        if searchMethod == "4":
            startTime = timer()
            IDDFS.iddfs(placeInfo, start, goal)
            endTime = timer()
            print("Time to execute: ", (endTime - startTime), " seconds")
        if searchMethod == "5":
            startTime = timer()
            BestFirst.bestFirst(placeInfo, start, goal)
            endTime = timer()
            print("Time to execute: ", (endTime - startTime), " seconds")
        if searchMethod == "6":
            startTime = timer()
            AStar.aStar(placeInfo, start, goal)
            endTime = timer()
            print("Time to execute: ", (endTime - startTime), " seconds")


        userGo = input(("Would you like to test another search method? Enter y for yes and n for no: "))
