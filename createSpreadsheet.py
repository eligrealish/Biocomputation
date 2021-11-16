import numpy as np

import config
import time
import csv

def writeToSpreadSheet():

    selectionType = config.selectionType

    crossoverType = config.crossoverType

    mutationType = config.mutationType

    N = config.N

    P = config.P

    mutationStep = config.mutationStep

    mutationRate = config.mutationRate

    numberOfGenerations = config.numberOfGenerations

    numberOfRuns = config.numberOfRuns

    fitnessFunction = config.fitnessFunction

    allfitness = config.allFitness

    allFitnessInfo = config.allFitnessInfo

    allTopFitness = config.allTopFitness

    allGenofFitness = config.allGenofFitness

    allGeneStd = config.allGeneStd

    runData = config.runData

    # fileName = selectionType + "-" + crossoverType + "-" + mutationType + "-N=" + str(N) + "-P=" + str(P) + "-Mstep="+str(mutationStep)+ "-mRate="+ str(mutationRate) + "-gen=" + str(numberOfGenerations) + "-run="+ str(numberOfRuns)+ "-func="+ str(fitnessFunction) +".csv"
    # fileName = str(config.cycle) +".csv"
    # print("filename=",fileName)
    # workbook = xlsxwriter.Workbook(fileName)
    # worksheet = workbook.add_worksheet()

    selectionVariables = []

    if selectionType == "T":
        selectionType = "Tornamunt"
        selectionVariables.append("Tornamunt Size")
        selectionVariables.append(str(config.tornamuntSize))
    elif selectionType =="S":
        selectionType = "Survivor"
        selectionVariables.append("Survivor Elite percentage")
        selectionVariables.append(str(config.elitePercentage))
    elif selectionType == "F":
        selectionType = "RouletteWheel"

    crossoverVariables = []

    if crossoverType == "O":
        crossoverType = "One Point"
    elif crossoverType == "SMA":
        crossoverType = "Simple Arithmetic Recombination"
        crossoverVariables.append("Arithmetic probabitly")
        crossoverVariables.append(str(config.arithmeticP))
    elif crossoverType == "SNA":
        crossoverType = "Single Arithmetic Recombination"
        crossoverVariables.append("Arithmetic probabitly")
        crossoverVariables.append(str(config.arithmeticP))
    elif crossoverType == "WA":
        crossoverType = "Whole Arithmetic Recombination"
        crossoverVariables.append("Arithmetic probabitly")
        crossoverVariables.append(str(config.arithmeticP))
    elif crossoverType == "U":
        crossoverType = "Uniform"
        crossoverVariables.append("Uniform probablitly")
        crossoverVariables.append(str(config.uniformP))

    mutationVariables = []

    if mutationType == "C":
        mutationType = "Creep"
        mutationVariables.append("Step size")
        mutationVariables.append(str(config.mutationStep))
        mutationVariables.append("Mutation Rate")
        mutationVariables.append(str(config.mutationRate))
    elif mutationType == "S":
        mutationType = "Scramble"

    elif mutationType == "R":
        mutationType = "Random Resetting"
        mutationVariables.append("Mutation Rate")
        mutationVariables.append(str(config.mutationRate))


    if fitnessFunction == 1:
        fitnessFunction = "10N + SUM(Gene - 10 x Cos(2pi x Gene)"
    elif fitnessFunction == 2:
        fitnessFunction = "-20*e(-0.2*sqrt(1/N*SUM(Gene^2))-e(1/N*SUM(Cos(2pi)*Gene)))"




    # field names

    # data rows of csv file
    outputList = []

    outputList.append(["Number of Runs", numberOfRuns])
    outputList.append(["Number of Generations", numberOfGenerations])
    outputList.append(["N (Size of Cromosome)", N])
    outputList.append(["P (Size of Population)", P])

    outputList.append([])

    outputList.append(["Selection",selectionType])
    outputList.append(selectionVariables)
    outputList.append(["Crossover", crossoverType])
    outputList.append(crossoverVariables)
    outputList.append(["Mutation", mutationType])
    outputList.append(mutationVariables)

    outputList.append([])

    outputList.append(["Fitness Function",fitnessFunction])


    outputList.append([])

    topRow = []

    for i in range(numberOfRuns):
        topRow.append("Run "+str(i+1))
        topRow.append("")
        topRow.append("")
        topRow.append("")

    # print("TopRow",topRow)
    outputList.append(topRow)

    rowTwo = []

    for i in range(numberOfRuns):
        rowTwo.append("Generations")
        rowTwo.append("Mean")
        rowTwo.append("Lowest")
        rowTwo.append("")

    # print("rowTwo",rowTwo)
    outputList.append(rowTwo)


    for i in range(0,numberOfGenerations):
        row = []
        # print("i+1",i+1)

        for j in range(0,numberOfRuns):
            row.append("Generation "+str(i+1))
            # print("row",row)
            row.append(allFitnessInfo[j][i][0])
            row.append(allFitnessInfo[j][i][1])
            # row.append(allGeneStd[j][i])
            row.append("")

        # print("row",row)

        outputList.append(row)

    # print("allFitnessInfo",allFitnessInfo)



    row = []

    for i in range(0,numberOfRuns):
            row.append("Best")
            row.append(allTopFitness[i][0])
            row.append(allTopFitness[i][1])
            row.append("")



    outputList.append(row)

    row = []

    # print("allGenofFitness",allGenofFitness)

    for i in range(0, numberOfRuns):
        row.append("Generation")
        row.append(allGenofFitness[i][0]+1)
        row.append(allGenofFitness[i][1]+1)
        row.append("")


    outputList.append(row)


    outputList.append([])

    named_tuple = time.localtime()
    time_string = time.strftime("%H-%M-%S", named_tuple)

    outputList.append([time_string])

    outputList.append([runData])

    fileName = time_string + ".csv"

    # writing to csv file
    with open(fileName, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the data rows
        csvwriter.writerows(outputList)


    # for i in config.allFitness:
    #
    #     for j in i :
    #         print("j, ", j)
    #         print("type(j), ", type(j))
    #         print("type(j), ", type(j[0]))


    # print("config.allFitness ,",config.allFitness)
    # print("config.allFitness type , ", type(config.allFitness))
    # print("config.allFitness type , ",type(config.allFitness.astype(numpy)))
    # print("config.allFitness type [0], ", type(config.allFitness[0]))

    config.allFitness = np.asarray(config.allFitness)

    # print("config.allFitness type , ",type(config.allFitness))

    config.allFitness = config.allFitness.reshape(-1,config.N)

    # print()
    # print()
    # print()
    #
    # print("config.allFitness ,", config.allFitness)
    # print("outputList ",outputList)
    #
    # exit()

    fitnessFileName = "fitness "+fileName

    # writing to csv file
    with open(fitnessFileName, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the data rows
        csvwriter.writerows(config.allFitness)
