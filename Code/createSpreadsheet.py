import config
import xlsxwriter
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

    # fileName = selectionType + "-" + crossoverType + "-" + mutationType + "-N=" + str(N) + "-P=" + str(P) + "-Mstep="+str(mutationStep)+ "-mRate="+ str(mutationRate) + "-gen=" + str(numberOfGenerations) + "-run="+ str(numberOfRuns)+ "-func="+ str(fitnessFunction) +".csv"
    fileName = "sel=" + selectionType + ",cross=" +  crossoverType + ",mut=" + mutationType + ",gen=" + str(
        numberOfGenerations) + ",run=" + str(numberOfRuns) + ",func=" + str(fitnessFunction) +  ",N="+ str(config.N) + ",P="+ str(config.P)+".csv"
    print("filename=",fileName)
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


    for i in range(1,numberOfRuns+1):
        outputList.append([])

        outputList.append(["Run " + str(i)])

        infoMarkers = [""] * (P + 4)

        infoMarkers.append("Mean")
        infoMarkers.append("Best")
        outputList.append(infoMarkers)

        for j in range(1,numberOfGenerations+1):
            generationList = []
            generationList.append("Generation " + str(j))

            for fitness in allfitness[i-1][j-1]:
                generationList.append(fitness)

            generationList.append("")
            generationList.append("")
            generationList.append("")


            for info in allFitnessInfo[i-1][j-1]:
                generationList.append(info)

            outputList.append(generationList)

        outputList.append([])



        bestMean = ["Best Mean"]
        bestMean.append(allTopFitness[i - 1][0])
        outputList.append(bestMean)

        meanGen = ["Best Mean Generation"]
        meanGen.append(allGenofFitness[i - 1][0]+1)
        outputList.append(meanGen)
        outputList.append([])

        bestBest = ["Lowest"]
        bestBest.append(allTopFitness[i - 1][1])
        outputList.append(bestBest)

        bestGen = ["Lowest Generation"]
        bestGen.append(allGenofFitness[i - 1][1]+1)
        outputList.append(bestGen)
        outputList.append([])



        outputList.append([])

    outputList.append([])

    for i in range(1,numberOfRuns+1):
        outputList.append(["Run " + str(i)])

        infoMarkers = [""]
        infoMarkers.append("Mean")
        infoMarkers.append("Lowest")
        outputList.append(infoMarkers)

        for j in range(1, numberOfGenerations + 1):
            generationList = []
            generationList.append("Generation " + str(j))

            for info in allFitnessInfo[i - 1][j - 1]:
                generationList.append(info)

            outputList.append(generationList)

        outputList.append([])

        bestMean = ["Best Mean"]
        bestMean.append(allTopFitness[i - 1][0])
        outputList.append(bestMean)

        meanGen = ["Best Mean Generation"]
        meanGen.append(allGenofFitness[i - 1][0] + 1)
        outputList.append(meanGen)
        outputList.append([])

        bestBest = ["Lowest"]
        bestBest.append(allTopFitness[i - 1][1])
        outputList.append(bestBest)

        bestGen = ["Lowest Generation"]
        bestGen.append(allGenofFitness[i - 1][1] + 1)
        outputList.append(bestGen)
        outputList.append([])

        outputList.append([])





    print(outputList)



    # writing to csv file
    with open(fileName, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the data rows
        csvwriter.writerows(outputList)

