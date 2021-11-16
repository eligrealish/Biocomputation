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
from adaptive import *

# BACK UP EVERY SINGLE DAYYYYYYY
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # config.arithmeticP = 0.1
    test11()
    exit()

    config.arithmeticP = 0.5
    test12()







    for cycle in range(10,11):
        print(cycle,"cycle")

        config.cycle = cycle

        # print("ten")
        # config.selectionType = "T"
        # config.tornamuntSize = 2
        #
        # config.crossoverType = "O"
        #
        # config.mutationType = "R"
        #
        # config.mutationRate = 0.4
        #
        # if cycle == 1:
        #     print("one")
        #     config.selectionType = "T"
        #     config.tornamuntSize = 2
        #
        #     config.crossoverType = "O"
        #
        #     config.mutationType = "C"
        #     config.mutationRate = 0.01
        #     config.mutationStep = 0.5
        #
        # elif cycle == 2:
        #     print("two")
        #     config.selectionType = "T"
        #     config.tornamuntSize = 2
        #
        #     config.crossoverType = "O"
        #
        #     config.mutationType = "C"
        #     config.mutationRate = 0.2
        #     config.mutationStep = 0.5
        #
        # elif cycle == 3:
        #     print("three")
        #     config.selectionType = "T"
        #     config.tornamuntSize = 2
        #
        #     config.crossoverType = "O"
        #
        #     config.mutationType = "C"
        #     config.mutationRate = 0.4
        #     config.mutationStep = 0.5
        #
        # elif cycle == 4:
        #     print("four")
        #     config.selectionType = "T"
        #     config.tornamuntSize = 2
        #
        #     config.crossoverType = "O"
        #
        #     config.mutationType = "C"
        #     config.mutationRate = 0.4
        #     config.mutationStep = 2
        #
        #
        # elif cycle == 5:
        #     print("five")
        #     config.selectionType = "T"
        #     config.tornamuntSize = 2
        #
        #     config.crossoverType = "O"
        #
        #     config.mutationType = "C"
        #     config.mutationRate = 0.4
        #     config.mutationStep = 1
        #
        #
        # elif cycle == 6:
        #     print("six")
        #     config.selectionType = "T"
        #     config.tornamuntSize = 4
        #
        #     config.crossoverType = "O"
        #
        #     config.mutationType = "C"
        #     config.mutationRate = 0.4
        #     config.mutationStep = 0.5
        #
        # elif cycle == 7:
        #     print("seven")
        #     config.selectionType = "T"
        #     config.tornamuntSize = 8
        #
        #     config.crossoverType = "O"
        #
        #     config.mutationType = "C"
        #     config.mutationRate = 0.4
        #     config.mutationStep = 0.5
        #
        #
        # elif cycle == 8:
        #     print("eight")
        #     config.selectionType = "S"
        #     config.elitePercentage = 0.2
        #
        #     config.crossoverType = "O"
        #
        #     config.crossoverType = "C"
        #     config.mutationRate = 0.4
        #     config.mutationStep = 0.5

        # elif cycle == 9:
        #     print("nine")
        #     config.selectionType = "S"
        #     config.elitePercentage = 0.4
        #
        #     config.crossoverType = "O"
        #
        #     config.mutationType = "C"
        #     config.mutationRate = 0.4
        #     config.mutationStep = 0.5
        #
        # elif cycle == 10:
        #     print("ten")
        #     config.selectionType = "T"
        #     config.tornamuntSize = 2
        #
        #     config.crossoverType = "O"
        #
        #     config.mutationType = "R"
        #
        #
        # elif cycle == 11:
        #     print("eleven")
        #     config.selectionType = "T"
        #     config.tornamuntSize = 2
        #
        #     config.crossoverType = "O"
        #
        #     config.mutationType = "S"
        #
        #
        # elif cycle == 12:
        #     print("twelve")
        #     config.selectionType = "T"
        #     config.tornamuntSize = 2
        #
        #     config.crossoverType = "SMA"
        #     config.arithmeticP = 0.7
        #
        #     config.mutationType = "C"
        #     config.mutationRate = 0.4
        #     config.mutationStep = 0.5
        #
        # elif cycle == 13:
        #     print("thirteen")
        #     config.selectionType = "T"
        #     config.tornamuntSize = 2
        #
        #     config.crossoverType = "SMA"
        #     config.arithmeticP = 0.4
        #
        #     config.mutationType = "C"
        #     config.mutationRate = 0.4
        #     config.mutationStep = 0.5
        #
        # elif cycle == 14:
        #     print("fourteen")
        #     config.selectionType = "T"
        #     config.tornamuntSize = 2
        #
        #     config.crossoverType = "SMA"
        #     config.arithmeticP = 0.1
        #
        #     config.mutationType = "C"
        #     config.mutationRate = 0.4
        #     config.mutationStep = 0.5
        #
        # elif cycle == 15:
        #     print("fourteen")
        #     config.selectionType = "T"
        #     config.tornamuntSize = 2
        #
        #     config.crossoverType = "U"
        #
        #     config.mutationType = "C"
        #     config.mutationRate = 0.4
        #     config.mutationStep = 0.5



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



        # print("allFitnessInfo=", config.allFitnessInfo)
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
                print("Mutation rate",config.mutationRate)

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

                # print("allFitnessInfo mean", config.allFitnessInfo)
                # # printGenePopulation()
                #
                #
                # print("current mean",config.allFitnessInfo[run][gen][0])
                # print("current lowest", config.allFitnessInfo[run][gen][1])

                # if round(config.allFitnessInfo[run][gen][0],4) == round(config.allFitnessInfo[run][gen][1],4):
                #     mutation = randomResetting
                #     config.mutationRate = 0.00001
                #     print("Lowest Value and mean are the same")
                #     print("mutation set to random restting",mutation)


                # if gen >= 15:
                #     fifteenGenAgoMean = config.allFitnessInfo[run][gen - 15][0]
                #     currentGenMean = config.allFitnessInfo[run][gen][0]
                #
                #     print("The mean fifteeen generatations ago ", fifteenGenAgoMean)
                #     print("The current mean gen", currentGenMean)
                #
                #     fitnessRatio = currentGenMean / fifteenGenAgoMean
                #     print("fittnessRatio", fitnessRatio)
                #     if fitnessRatio > 0.9:
                #         # config.mutationRate = 0.01
                #         print("Better fitness has slowed")
                #     else:
                #         # config.mutationRate = 0.1
                #         print("Good fitness has continued")


                # finding and storing the standard deviation of all genes in a population

                listOfGenes = []

                for i in config.currentPopulation:
                    for j in i.chromosome:
                        listOfGenes.append(j)

                config.allGeneStd[run][gen] = np.std(listOfGenes)

                # storing all memebers of the population
                config.allIndivduals[run][gen] = copy.deepcopy(config.currentPopulation)

                if gen == 30 or gen == 55 or  gen == 105  or  gen == 155  or  gen == 205 or  gen == 255 or  gen == 305 or  gen == 355 or  gen == 405 or  gen == 455 or  gen == 505 or  gen == 555 or  gen == 605 or  gen == 655 or  gen == 705or  gen == 755 or  gen == 805:
                    print("if 1")
                    mutation = creepMutation
                    config.mutationRate = 0.02
                    config.mutationStep = 1
                    config.elitePercentage = 0.4
                elif gen == 50  or  gen == 100  or  gen == 150  or  gen == 200 or  gen == 250 or  gen == 300 or  gen == 350 or  gen == 400 or  gen == 450 or  gen == 500 or  gen == 550 or  gen == 600 or  gen == 650 or  gen == 700 or  gen == 750 or  gen == 800:
                    print("if 2")
                    mutation = randomResetting
                    config.mutationRate = 0.01
                elif gen >= 810:
                    config.mutationRate = 0.01
                    config.mutationStep = 0.5
                    config.elitePercentage = 0.6

                if gen >= 1000 and gen % 9 == 0 and gen % 5 == 0:
                    mutation = randomResetting
                    config.mutationRate = 0.01










                # if round(config.allGeneStd[run][gen],2) > 1.6:
                #     print("Diverse")
                #     config.mutationRate = 0.01
                # else:
                #     print("Staggering Diversity")
                #     config.mutationRate = 0.02
                #     config.uniformP = 0.7
                #     config.elitePercentage = 0.4

                # print("listOfGenes",listOfGenes)
                #
                # print("config.StdOfGenes", config.allGeneStd)

            # print(config.allFitness)

            # storing best fitnesses for all run
            config.allTopFitness[run] = copy.deepcopy(config.topFitness)
            config.allGenofFitness[run] = copy.deepcopy(config.genOfFitness)

        # print("config.allFitnessInfo = ", config.allFitnessInfo)
        # print("config.allFitness = ", config.allFitness)
        # print("--------")
        # print("config.topFitnesssInfo = ", config.allTopFitness)
        # print("config.allGenofFitness = ", config.allGenofFitness)




        writeToSpreadSheet()
        # printGenePopulation()

        finish = False

        while not finish:
            decision = input('Enter v to view population or press e to end ')
            if decision == 'e':
                finish = True
            elif decision == 'v':
                run = int(input('Enter run '))
                gen = int(input('Enter gen '))
                printGenePopulation(config.allIndivduals[run-1][gen-1])







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
