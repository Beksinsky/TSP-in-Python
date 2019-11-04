import random
import sys
import time

start = time.time()

fileName = sys.argv[1]
popNum = int(sys.argv[2])

with open(fileName, "r") as file:
    lines = list(map(str.split, file.read().splitlines()))

    missing_values = []

    for index in range(len(lines)):
        missing_values.append([line[index] for line in lines[index + 1:]])

    matrix = [line + values for line, values in zip(lines, missing_values)]


def showMatrix():
    for row in matrix:
        print(row)


def member():
    global memb
    memb = []
    i = 0
    while i < len(matrix):
        x = random.randint(0, len(matrix) - 1)
        if x not in memb:
            # print(x)
            memb.append(x)
            i += 1
    return memb


def template():
    global membersTemplate
    membersTemplate = []
    n = 0
    while n < len(matrix):
        membersTemplate.append(n)
        n += 1


def population(n):
    global populationArray
    populationArray = [[], []]
    i = 0
    while i < n:
        random.shuffle(membersTemplate)
        populationArray[0].append(membersTemplate[:])
        i += 1


def fitness():
    i = 0
    while i < len(populationArray[0]):
        j = 0
        fit = 0
        while j < len(populationArray[0][i]):
            if j + 1 != len(populationArray[0][i]):
                fit += int(matrix[populationArray[0][i][j]][populationArray[0][i][j + 1]])
                #koleny while od lenth -1 do index 0
            else:
                fit += int(matrix[populationArray[0][i][j]][populationArray[0][i][0]])
                populationArray[1].append(fit)
            j += 1
        i += 1


def saveWynik():
    wynik = open("wynik.txt", "w+")
    i = 0
    for _list in populationArray[0]:
        j = 0
        for _miasto in _list:
            if j != len(_list) - 1:
                wynik.write(str(_miasto) + "-")
            else:
                wynik.write(str(_miasto) + " ")
            j += 1
        wynik.write(str(populationArray[1][i]))
        wynik.write('\n')
        i += 1
    wynik.close()


# showMatrix()
template()
population(popNum)
fitness()
saveWynik()
print(populationArray[0])
print(populationArray[1])
print()
print("--- %s seconds ---" % (time.time() - start))
