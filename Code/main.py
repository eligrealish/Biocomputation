# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# BACK UP EVERY SINGLE DAYYYYYYY

import random
import copy


import numpy as np

from mutation import *
from selection import *
from populationTools import *
import config
from crosssover import *
from createSpreadsheet import *
import sys, os

# BACK UP EVERY SINGLE DAYYYYYYY
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    cycle = 1



    if cycle == 1:
        print("one")
        config.selectionType = "T"
        config.tornamuntSize = 2

        config.crossoverType = "O"

        config.mutationType = "C"
        config.mutationRate = 0.01
        config.mutationStep = 0.5

    elif cycle == 2:
        print("two")
        config.selectionType = "T"
        config.tornamuntSize = 2

        config.crossoverType = "O"

        config.mutationType = "C"
        config.mutationRate = 0.2
        config.mutationStep = 0.5

    elif cycle == 3:
        print("three")
        config.selectionType = "T"
        config.tornamuntSize = 2

        config.crossoverType = "O"

        config.mutationType = "C"
        config.mutationRate = 0.4
        config.mutationStep = 0.5

    elif cycle == 4:
        print("four")
        config.selectionType = "T"
        config.tornamuntSize = 2

        config.crossoverType = "O"

        config.mutationType = "C"
        config.mutationRate = 0.4
        config.mutationStep = 2


    elif cycle == 5:
        print("five")
        config.selectionType = "T"
        config.tornamuntSize = 2

        config.crossoverType = "O"

        config.mutationType = "C"
        config.mutationRate = 0.4
        config.mutationStep = 1


    elif cycle == 6:
        print("six")
        config.selectionType = "T"
        config.tornamuntSize = 4

        config.crossoverType = "O"

        config.mutationType = "C"
        config.mutationRate = 0.4
        config.mutationStep = 0.5

    elif cycle == 7:
        print("seven")
        config.selectionType = "T"
        config.tornamuntSize = 8

        config.crossoverType = "O"

        config.mutationType = "C"
        config.mutationRate = 0.4
        config.mutationStep = 0.5


    elif cycle == 8:
        print("eight")
        config.selectionType = "S"
        config.elitePercentage = 0.2

        config.crossoverType = "O"

        config.crossoverType = "C"
        config.mutationRate = 0.4
        config.mutationStep = 0.5

    elif cycle == 9:
        print("nine")
        config.selectionType = "S"
        config.elitePercentage = 0.4

        config.crossoverType = "O"

        config.crossoverType = "C"
        config.mutationRate = 0.4
        config.mutationStep = 0.5

    elif cycle == 10:
        print("ten")
        config.selectionType = "T"
        config.tornamuntSize = 2

        config.crossoverType = "O"

        config.mutationType = "R"


    elif cycle == 11:
        print("eleven")
        config.selectionType = "T"
        config.tornamuntSize = 2

        config.crossoverType = "O"

        config.mutationType = "S"


    elif cycle == 12:
        print("twelve")
        config.selectionType = "T"
        config.tornamuntSize = 2

        config.crossoverType = "SNA"
        config.arithmeticP = 0.7

        config.mutationType = "C"
        config.mutationRate = 0.4
        config.mutationStep = 0.5

    elif cycle == 13:
        print("thirteen")
        config.selectionType = "T"
        config.tornamuntSize = 2

        config.crossoverType = "SNA"
        config.arithmeticP = 0.4

        config.mutationType = "C"
        config.mutationRate = 0.4
        config.mutationStep = 0.5

    elif cycle == 14:
        print("fourteen")
        config.selectionType = "T"
        config.tornamuntSize = 2

        config.crossoverType = "SNA"
        config.arithmeticP = 0.1

        config.mutationType = "C"
        config.mutationRate = 0.4
        config.mutationStep = 0.5

    elif cycle == 15:
        print("fourteen")
        config.selectionType = "T"
        config.tornamuntSize = 2

        config.crossoverType = "U"

        config.mutationType = "C"
        config.mutationRate = 0.4
        config.mutationStep = 0.5


    exit()


    # Creating evolulation operator objects
    # Chosing selection
    if config.selectionType == "T":
        selection = tournamentSelection
    elif config.selectionType == "S":
        selection = survirorSelection
    elif config.selectionType == "F":
        selection = fitnessProportionateSelection

    # Chosing crossver
    if config.crossoverType == "O":
        crossover = onePointCrossover
    elif config.crossoverType == "SMA":
        crossover = simpleArithmeticRecombination
    elif config.crossoverType == "SNA":
        crossover = singleArithmeticRecombination
    elif config.crossoverType == "WA":
        crossover = wholeArithmeticRecombination
    elif config.crossoverType == "U":
        crossover = uniformCrossover

    # Chosing mutation
    if config.mutationType == "C":
        mutation = creepMutation
    elif config.mutationType == "S":
        mutation = scrambleMutation
    elif config.mutationType == "R":
        mutation = randomResetting



    print("allFitnessInfo=", config.allFitnessInfo)
    for run in range(config.numberOfRuns):
        # print("----New Run----")
        initialisePopulation()
        # printGenePopulation()
        config.run = run

        for gen in range(config.numberOfGenerations):
            # print("----New Generation----")

            config.gen = gen

            print("run", run + 1)
            print("gen", gen + 1)

            selection()
            crossover()
            # printGenePopulation()
            mutation()

            calculateNewPopulationFitness()

            meanFitness()
            bestFitness()

            # printGenePopulation()


            # print("Current Generation")
            # print("Mean =", config.currentFitness[0])
            # print("Lowest =", config.currentFitness[1])
            #
            # print()
            # print("Best Info")
            # print("Best Mean =", config.topFitness[0], "at generation ", config.genOfFitness[0])
            # print("Best Lowest =", config.topFitness[1], "at generation ", config.genOfFitness[1])

            # Storing the current and best fitness for each generation
            config.allFitnessInfo[run][gen] = copy.deepcopy(config.currentFitness)

            # storing every fitness for each generation
            currentFitnesses = []
            for i in config.currentPopulation:
                currentFitnesses.append(i.fitness)
            config.allFitness[run][gen] = copy.deepcopy(currentFitnesses)



        # print(config.allFitness)

        # storing best fitnesses for all run
        config.allTopFitness[run] = copy.deepcopy(config.topFitness)
        config.allGenofFitness[run] = copy.deepcopy(config.genOfFitness)

    # print("config.allFitnessInfo = ", config.allFitnessInfo)
    # print("config.allFitness = ", config.allFitness)
    # print("--------")
    # print("config.topFitnesssInfo = ", config.allTopFitness)
    # print("config.allGenofFitness = ", config.allGenofFitness)
    # writeToSpreadSheet()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
