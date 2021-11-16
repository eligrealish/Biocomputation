import config
from mutation import *
from selection import *
from populationTools import *
from crosssover import *
from createSpreadsheet import *
import time
from IPython.display import display, clear_output
from matplotlib import pyplot
import numpy as np
from numpy import arange
from random import uniform
import sys

import matplotlib.pyplot as plt
import matplotlib.animation as animation


# testing adaptive algorithm, with random reset and creep modified during experimentaion, tornamunt then survivor is used like in example
def test1():

    config.runData = "adaptive chance of random and creep selection but not adaprive step"

    randomResetProb = 0.5

    creepProb = 0.5

    finalProbabilitesForRun = [[0.0 for i in range(2)] for w in range(config.numberOfRuns)]

    selection = tournamentSelection
    crossover = uniformCrossover

    for run in range(config.numberOfRuns):
        config.run = run

        initialisePopulation()



        for gen in range(config.numberOfGenerations):
            config.gen = gen

            #Select Crossover Type
            mutProb = random.uniform(0,1)
            print("mutProb",mutProb)
            print("randomResetProb",randomResetProb)
            print("creepProb",creepProb)

            if mutProb > randomResetProb:
                mutation = randomResetting
            elif mutProb < creepProb:
                mutation = creepMutation

            print("mutation",mutation)





            print("run", run + 1)
            print("gen", gen + 1)
            print("Mutation rate", config.mutationRate)

            selection()
            crossover()
            mutation()

            calculateNewPopulationFitness()

            meanFitness()
            bestFitness()



            # Storing the current and best fitness for each generation
            config.allFitnessInfo[run][gen] = copy.deepcopy(config.currentFitness)

            # storing every fitness for each generation
            currentFitnesses = []
            for i in config.currentPopulation:
                currentFitnesses.append(i.fitness)
            config.allFitness[run][gen] = copy.deepcopy(currentFitnesses)


            # listOfGenes = []
            #
            # for i in config.currentPopulation:
            #     for j in i.chromosome:
            #         listOfGenes.append(j)
            #
            # config.allGeneStd[run][gen] = np.std(listOfGenes)

            # storing all memebers of the population
            config.allIndivduals[run][gen] = copy.deepcopy(config.currentPopulation)

            # print("------------")
            #
            # print("Creep Before ",creepProb)
            # print("Random Before ",randomResetProb)
            # print("Current mutation type",mutation)

            # Since there would be no data to calculate how well a generation has performed, sucsess of mutation can't be calculated till passed gen 1
            if gen > 0:
                # print("Passed Gen one",config.allFitnessInfo[run][gen-1][1])
                # print("Current Gen one",config.allFitnessInfo[run][gen][1])
                if config.allFitnessInfo[run][gen][1] < config.allFitnessInfo[run][gen-1][1]:
                    # print("current Rate better then previous")
                    if mutation is randomResetting:
                        # print("Randomresetting")
                        # Making random reset more likely and making creep less likley
                        randomResetProb = randomResetProb * 1.006
                        creepProb = 1 - randomResetProb
                    elif mutation is creepMutation:
                        # print("creepMutation")
                        # Making creep more likely and making random reset less likley
                        creepProb = creepProb * 1.006
                        randomResetProb = 1 - creepProb

                elif config.allFitnessInfo[run][gen][1] > config.allFitnessInfo[run][gen-1][1]:
                    # print("current Rate worse then previous")
                    if mutation is randomResetting:
                        creepProb = creepProb * 1.006
                        randomResetProb = 1 - creepProb
                        # print("Randomresetting")
                    elif mutation is creepMutation:
                        # print("creepMutation")
                        randomResetProb = randomResetProb * 1.006
                        creepProb = 1 - randomResetProb





            if randomResetProb > 1:
                randomResetProb = 1
            elif randomResetProb < 0:
                randomResetProb = 0

            if creepProb > 1:
                creepProb = 1
            elif creepProb < 0:
                creepProb = 0







            survirorSelection()

            # print("Creep After ", creepProb)
            # print("Random after ", randomResetProb)
            #
            # print("---------")


        config.allTopFitness[run] = copy.deepcopy(config.topFitness)
        config.allGenofFitness[run] = copy.deepcopy(config.genOfFitness)

        finalProbabilitesForRun[run][0] = copy.deepcopy(randomResetProb)
        finalProbabilitesForRun[run][1] = copy.deepcopy(creepProb)



    writeToSpreadSheet()

    print(finalProbabilitesForRun)


    # finish = False
    #
    # while not finish:
    #     decision = input('Enter v to view population or press e to end ')
    #     if decision == 'e':
    #         finish = True
    #     elif decision == 'v':
    #         run = int(input('Enter run '))
    #         gen = int(input('Enter gen '))
    #         printGenePopulation(config.allIndivduals[run - 1][gen - 1])



#  similar to test one but predefined probablilites
def test2():

    config.runData = ["supposed to be an average of probablities for predermied run to differentate between adaptiing probablity or prederamiend"]

    randomResetProb = 0.9374260335333962,0.12642352792909106

    creepProb = 0.06257396646660385, 0.8735764720709089

    finalProbabilitesForRun = [[0.0 for i in range(2)] for w in range(config.numberOfRuns)]

    selection = tournamentSelection
    crossover = uniformCrossover

    for run in range(config.numberOfRuns):
        config.run = run

        initialisePopulation()

        for gen in range(config.numberOfGenerations):
            config.gen = gen

            # Select Crossover Type
            mutProb = random.uniform(0, 1)
            print("mutProb", mutProb)
            print("randomResetProb", randomResetProb)
            print("creepProb", creepProb)

            if mutProb > randomResetProb:
                mutation = randomResetting
            elif mutProb < creepProb:
                mutation = creepMutation

            print("mutation", mutation)

            print("run", run + 1)
            print("gen", gen + 1)
            print("Mutation rate", config.mutationRate)

            selection()
            crossover()
            mutation()

            calculateNewPopulationFitness()

            meanFitness()
            bestFitness()

            # Storing the current and best fitness for each generation
            config.allFitnessInfo[run][gen] = copy.deepcopy(config.currentFitness)

            # storing every fitness for each generation
            currentFitnesses = []
            for i in config.currentPopulation:
                currentFitnesses.append(i.fitness)
            config.allFitness[run][gen] = copy.deepcopy(currentFitnesses)

            # listOfGenes = []
            #
            # for i in config.currentPopulation:
            #     for j in i.chromosome:
            #         listOfGenes.append(j)
            #
            # config.allGeneStd[run][gen] = np.std(listOfGenes)

            # storing all memebers of the population
            config.allIndivduals[run][gen] = copy.deepcopy(config.currentPopulation)


            survirorSelection()

            # print("Creep After ", creepProb)
            # print("Random after ", randomResetProb)
            #
            # print("---------")

        config.allTopFitness[run] = copy.deepcopy(config.topFitness)
        config.allGenofFitness[run] = copy.deepcopy(config.genOfFitness)

        finalProbabilitesForRun[run][0] = copy.deepcopy(randomResetProb)
        finalProbabilitesForRun[run][1] = copy.deepcopy(creepProb)

    writeToSpreadSheet()

    print(finalProbabilitesForRun)

    # finish = False
    #
    # while not finish:
    #     decision = input('Enter v to view population or press e to end ')
    #     if decision == 'e':
    #         finish = True
    #     elif decision == 'v':
    #         run = int(input('Enter run '))
    #         gen = int(input('Enter gen '))
    #         printGenePopulation(config.allIndivduals[run - 1][gen - 1])


def test3():

    config.runData = "The following was done with an adaptive random reset prob and a mutation prob, the rate at which they happen is 0.01 for rest and 0.02 for muation "

    randomResetProb = 0.5

    creepProb = 0.5

    finalProbabilitesForRun = [[0.0 for i in range(2)] for w in range(config.numberOfRuns)]

    selection = tournamentSelection
    crossover = uniformCrossover

    for run in range(config.numberOfRuns):
        config.run = run

        initialisePopulation()



        for gen in range(config.numberOfGenerations):
            config.gen = gen

            #Select Crossover Type
            mutProb = random.uniform(0,1)
            print("mutProb",mutProb)
            print("randomResetProb",randomResetProb)
            print("creepProb",creepProb)

            if mutProb > randomResetProb:
                mutation = randomResetting
                config.mutationRate = 0.01
            elif mutProb < creepProb:
                mutation = creepMutation
                config.mutationRate = 0.02

            print("mutation",mutation)





            print("run", run + 1)
            print("gen", gen + 1)
            print("Mutation rate", config.mutationRate)

            selection()
            crossover()
            mutation()

            calculateNewPopulationFitness()

            meanFitness()
            bestFitness()



            # Storing the current and best fitness for each generation
            config.allFitnessInfo[run][gen] = copy.deepcopy(config.currentFitness)

            # storing every fitness for each generation
            currentFitnesses = []
            for i in config.currentPopulation:
                currentFitnesses.append(i.fitness)
            config.allFitness[run][gen] = copy.deepcopy(currentFitnesses)


            # listOfGenes = []
            #
            # for i in config.currentPopulation:
            #     for j in i.chromosome:
            #         listOfGenes.append(j)
            #
            # config.allGeneStd[run][gen] = np.std(listOfGenes)

            # storing all memebers of the population
            config.allIndivduals[run][gen] = copy.deepcopy(config.currentPopulation)

            # print("------------")
            #
            # print("Creep Before ",creepProb)
            # print("Random Before ",randomResetProb)
            # print("Current mutation type",mutation)

            # Since there would be no data to calculate how well a generation has performed, sucsess of mutation can't be calculated till passed gen 1
            if gen > 0:
                # print("Passed Gen one",config.allFitnessInfo[run][gen-1][1])
                # print("Current Gen one",config.allFitnessInfo[run][gen][1])
                if config.allFitnessInfo[run][gen][1] < config.allFitnessInfo[run][gen-1][1]:
                    # print("current Rate better then previous")
                    if mutation is randomResetting:
                        # print("Randomresetting")
                        # Making random reset more likely and making creep less likley
                        randomResetProb = randomResetProb * 1.006
                        creepProb = 1 - randomResetProb
                    elif mutation is creepMutation:
                        # print("creepMutation")
                        # Making creep more likely and making random reset less likley
                        creepProb = creepProb * 1.006
                        randomResetProb = 1 - creepProb

                elif config.allFitnessInfo[run][gen][1] > config.allFitnessInfo[run][gen-1][1]:
                    # print("current Rate worse then previous")
                    if mutation is randomResetting:
                        creepProb = creepProb * 1.006
                        randomResetProb = 1 - creepProb
                        # print("Randomresetting")
                    elif mutation is creepMutation:
                        # print("creepMutation")
                        randomResetProb = randomResetProb * 1.006
                        creepProb = 1 - randomResetProb





            if randomResetProb > 1:
                randomResetProb = 1
            elif randomResetProb < 0:
                randomResetProb = 0

            if creepProb > 1:
                creepProb = 1
            elif creepProb < 0:
                creepProb = 0







            survirorSelection()

            # print("Creep After ", creepProb)
            # print("Random after ", randomResetProb)
            #
            # print("---------")


        config.allTopFitness[run] = copy.deepcopy(config.topFitness)
        config.allGenofFitness[run] = copy.deepcopy(config.genOfFitness)

        finalProbabilitesForRun[run][0] = copy.deepcopy(randomResetProb)
        finalProbabilitesForRun[run][1] = copy.deepcopy(creepProb)



    writeToSpreadSheet()

    print(finalProbabilitesForRun)


    # finish = False
    #
    # while not finish:
    #     decision = input('Enter v to view population or press e to end ')
    #     if decision == 'e':
    #         finish = True
    #     elif decision == 'v':
    #         run = int(input('Enter run '))
    #         gen = int(input('Enter gen '))
    #         printGenePopulation(config.allIndivduals[run - 1][gen - 1])




def test4():

    config.runData = "The following was done with an adaptive random reset prob and a mutation prob, the rate at which they happen is 0.01 for rest and 0.02 for muation, the step rate is big little, randomly chosen and adaptive big 1,4 little 0.5 1"

    randomResetProb = 0.5

    creepProb = 0.5

    bigLittleProb = 0.3 #represents an intial 30% of big creep being chosen


    finalProbabilitesForRun = [[0.0 for i in range(2)] for w in range(config.numberOfRuns)]

    selection = tournamentSelection
    crossover = uniformCrossover

    for run in range(config.numberOfRuns):
        config.run = run

        initialisePopulation()



        for gen in range(config.numberOfGenerations):
            config.gen = gen

            # print("------------")

            #Select Crossover Type
            mutProb = random.uniform(0,1)
            # print("mutProb",mutProb)
            # print("randomResetProb",randomResetProb)
            # print("creepProb",creepProb)

            if mutProb > randomResetProb:
                mutation = randomResetting
                config.mutationRate = 0.01
            elif mutProb < creepProb:
                mutation = creepMutation
                config.mutationRate = 0.02

                # Selecting creep rate
                creepSizeProb = random.uniform(0,1)
                # print("creepSizeProb",creepSizeProb)
                if bigLittleProb > creepSizeProb:
                    # print("Big creep chosen")
                    config.mutationStep = 2
                else:
                    # print("Little Creep chose")
                    config.mutationStep = 0.5

            # print("mutation",mutation)
            #
            #
            #
            print("run", run + 1)
            print("gen", gen + 1)
            # print("Mutation rate", config.mutationRate)

            selection()
            crossover()
            mutation()

            calculateNewPopulationFitness()

            meanFitness()
            bestFitness()



            # Storing the current and best fitness for each generation
            config.allFitnessInfo[run][gen] = copy.deepcopy(config.currentFitness)

            # storing every fitness for each generation
            currentFitnesses = []
            for i in config.currentPopulation:
                currentFitnesses.append(i.fitness)
            config.allFitness[run][gen] = copy.deepcopy(currentFitnesses)


            # listOfGenes = []
            #
            # for i in config.currentPopulation:
            #     for j in i.chromosome:
            #         listOfGenes.append(j)
            #
            # config.allGeneStd[run][gen] = np.std(listOfGenes)

            # storing all memebers of the population
            config.allIndivduals[run][gen] = copy.deepcopy(config.currentPopulation)



            # print("Creep Before ",creepProb)
            # print("Random Before ",randomResetProb)
            # print("Current mutation type",mutation)
            #
            #
            #
            # print("bigLittleProb",bigLittleProb)

            # Since there would be no data to calculate how well a generation has performed, sucsess of mutation can't be calculated till passed gen 1
            if gen > 0:
                # print("Passed Gen one",config.allFitnessInfo[run][gen-1][1])
                # print("Current Gen one",config.allFitnessInfo[run][gen][1])
                if config.allFitnessInfo[run][gen][1] < config.allFitnessInfo[run][gen-1][1]:
                    # print("current Rate better then previous")
                    if mutation is randomResetting:
                        # print("Randomresetting")
                        # Making random reset more likely and making creep less likley
                        randomResetProb = randomResetProb * 1.006
                        creepProb = 1 - randomResetProb

                    elif mutation is creepMutation:
                        # print("creepMutation")
                        # Making creep more likely and making random reset less likley
                        creepProb = creepProb * 1.006
                        randomResetProb = 1 - creepProb

                        if config.mutationStep == 0.5:
                            # print("0.5")
                            bigLittleProb = bigLittleProb / 1.006
                        elif config.mutationStep == 2:
                            # print("2")
                            bigLittleProb = bigLittleProb * 1.006


                elif config.allFitnessInfo[run][gen][1] > config.allFitnessInfo[run][gen-1][1]:
                    # print("current Rate worse then previous")
                    if mutation is randomResetting:
                        creepProb = creepProb * 1.006
                        randomResetProb = 1 - creepProb

                        # print("Randomresetting")
                    elif mutation is creepMutation:
                        # print("creepMutation")
                        randomResetProb = randomResetProb * 1.006
                        creepProb = 1 - randomResetProb
                        if config.mutationStep == 0.5:
                            # print("0.5")
                            bigLittleProb = bigLittleProb * 1.006
                        elif config.mutationStep == 2:
                            # print("2")
                            bigLittleProb = bigLittleProb / 1.006



            # print("bigLittleProb", bigLittleProb)




            if randomResetProb > 1:
                randomResetProb = 1
            elif randomResetProb < 0:
                randomResetProb = 0

            if creepProb > 1:
                creepProb = 1
            elif creepProb < 0:
                creepProb = 0







            survirorSelection()

            # print("Creep After ", creepProb)
            # print("Random after ", randomResetProb)
            #
            # print("---------")


        config.allTopFitness[run] = copy.deepcopy(config.topFitness)
        config.allGenofFitness[run] = copy.deepcopy(config.genOfFitness)

        finalProbabilitesForRun[run][0] = copy.deepcopy(randomResetProb)
        finalProbabilitesForRun[run][1] = copy.deepcopy(creepProb)



    writeToSpreadSheet()

    print(finalProbabilitesForRun)


    # finish = False
    #
    # while not finish:
    #     decision = input('Enter v to view population or press e to end ')
    #     if decision == 'e':
    #         finish = True
    #     elif decision == 'v':
    #         run = int(input('Enter run '))
    #         gen = int(input('Enter gen '))
    #         printGenePopulation(config.allIndivduals[run - 1][gen - 1])


def test5():


    config.runData = "Scramble"
    randomResetProb = 0.5

    creepProb = 0.5

    finalProbabilitesForRun = [[0.0 for i in range(2)] for w in range(config.numberOfRuns)]

    selection = tournamentSelection
    crossover = uniformCrossover
    mutation = scrambleMutation

    for run in range(config.numberOfRuns):
        config.run = run

        initialisePopulation()



        for gen in range(config.numberOfGenerations):
            config.gen = gen

            print("run", run + 1)
            print("gen", gen + 1)


            selection()
            crossover()
            mutation()

            calculateNewPopulationFitness()

            meanFitness()
            bestFitness()



            # Storing the current and best fitness for each generation
            config.allFitnessInfo[run][gen] = copy.deepcopy(config.currentFitness)

            # storing every fitness for each generation
            currentFitnesses = []
            for i in config.currentPopulation:
                currentFitnesses.append(i.fitness)
            config.allFitness[run][gen] = copy.deepcopy(currentFitnesses)




            # storing all memebers of the population
            config.allIndivduals[run][gen] = copy.deepcopy(config.currentPopulation)




            survirorSelection()




        config.allTopFitness[run] = copy.deepcopy(config.topFitness)
        config.allGenofFitness[run] = copy.deepcopy(config.genOfFitness)

        finalProbabilitesForRun[run][0] = copy.deepcopy(randomResetProb)
        finalProbabilitesForRun[run][1] = copy.deepcopy(creepProb)



    writeToSpreadSheet()

    print(finalProbabilitesForRun)


    # finish = False
    #
    # while not finish:
    #     decision = input('Enter v to view population or press e to end ')
    #     if decision == 'e':
    #         finish = True
    #     elif decision == 'v':
    #         run = int(input('Enter run '))
    #         gen = int(input('Enter gen '))
    #         printGenePopulation(config.allIndivduals[run - 1][gen - 1])




def test6():

    config.runData = "50/50 random reset and and creep"
    randomResetProb = 0.5

    creepProb = 0.5

    finalProbabilitesForRun = [[0.0 for i in range(2)] for w in range(config.numberOfRuns)]

    selection = tournamentSelection
    crossover = uniformCrossover


    for run in range(config.numberOfRuns):
        config.run = run



        initialisePopulation()



        for gen in range(config.numberOfGenerations):
            config.gen = gen

            print("run", run + 1)
            print("gen", gen + 1)

            mutProb = random.uniform(0, 1)

            if mutProb > randomResetProb:
                mutation = randomResetting
            elif mutProb < creepProb:
                mutation = creepMutation

            selection()
            crossover()
            mutation()

            calculateNewPopulationFitness()

            meanFitness()
            bestFitness()



            # Storing the current and best fitness for each generation
            config.allFitnessInfo[run][gen] = copy.deepcopy(config.currentFitness)

            # storing every fitness for each generation
            currentFitnesses = []
            for i in config.currentPopulation:
                currentFitnesses.append(i.fitness)
            config.allFitness[run][gen] = copy.deepcopy(currentFitnesses)




            # storing all memebers of the population
            config.allIndivduals[run][gen] = copy.deepcopy(config.currentPopulation)




            survirorSelection()




        config.allTopFitness[run] = copy.deepcopy(config.topFitness)
        config.allGenofFitness[run] = copy.deepcopy(config.genOfFitness)

        finalProbabilitesForRun[run][0] = copy.deepcopy(randomResetProb)
        finalProbabilitesForRun[run][1] = copy.deepcopy(creepProb)



    writeToSpreadSheet()

    print(finalProbabilitesForRun)


    # finish = False
    #
    # while not finish:
    #     decision = input('Enter v to view population or press e to end ')
    #     if decision == 'e':
    #         finish = True
    #     elif decision == 'v':
    #         run = int(input('Enter run '))
    #         gen = int(input('Enter gen '))
    #         printGenePopulation(config.allIndivduals[run - 1][gen - 1])


def test7():
    config.runData = "3rd chance each of random reset, creep and scramble things are chosen"

    randomResetProb = 1/3

    creepProb = 1/3

    scrambleProb = 1/3


    finalProbabilitesForRun = [[0.0 for i in range(2)] for w in range(config.numberOfRuns)]

    selection = tournamentSelection
    crossover = uniformCrossover

    for run in range(config.numberOfRuns):
        config.run = run

        initialisePopulation()

        for gen in range(config.numberOfGenerations):
            config.gen = gen

            # Select Crossover Type
            mutProb = random.uniform(0, 1)
            print("mutProb", mutProb)
            print()
            print("randomResetProb", randomResetProb)
            print("creepProb", creepProb)
            print("scrambleProb", scrambleProb)
            print()

            if mutProb > 0 and mutProb < randomResetProb:
                mutation = randomResetting
                print("Random reset")
            elif mutProb > randomResetProb and mutProb < randomResetProb + creepProb:
                mutation = creepMutation
                print("Creep mutation")
            elif mutProb > randomResetProb + creepProb and mutProb < 1:
                print("Scramble")
                creepMutation()


            print("mutation", mutation)

            print("run", run + 1)
            print("gen", gen + 1)
            print("Mutation rate", config.mutationRate)

            selection()
            crossover()
            mutation()

            calculateNewPopulationFitness()

            meanFitness()
            bestFitness()

            # Storing the current and best fitness for each generation
            config.allFitnessInfo[run][gen] = copy.deepcopy(config.currentFitness)

            # storing every fitness for each generation
            currentFitnesses = []
            for i in config.currentPopulation:
                currentFitnesses.append(i.fitness)
            config.allFitness[run][gen] = copy.deepcopy(currentFitnesses)



            # storing all memebers of the population
            config.allIndivduals[run][gen] = copy.deepcopy(config.currentPopulation)



            survirorSelection()



        config.allTopFitness[run] = copy.deepcopy(config.topFitness)
        config.allGenofFitness[run] = copy.deepcopy(config.genOfFitness)

        finalProbabilitesForRun[run][0] = copy.deepcopy(randomResetProb)
        finalProbabilitesForRun[run][1] = copy.deepcopy(creepProb)

    writeToSpreadSheet()

    print(finalProbabilitesForRun)


def test8():
    # BROKEN
    config.runData = "Adaptive mutation between random reset, creep and scrmable"

    randomResetProb = 1 / 3

    creepProb = 1 / 3

    scrambleProb = 1 / 3

    finalProbabilitesForRun = [[0.0 for i in range(2)] for w in range(config.numberOfRuns)]

    selection = tournamentSelection
    crossover = uniformCrossover

    for run in range(config.numberOfRuns):
        config.run = run

        initialisePopulation()

        for gen in range(config.numberOfGenerations):
            config.gen = gen
            print()
            print()
            print()
            print()
            print()
            # Select Crossover Type
            mutProb = random.uniform(0, 1)
            print("mutProb", mutProb)

            print("randomResetProb", randomResetProb)
            print("creepProb", creepProb)
            print("scrambleProb", scrambleProb)
            print()

            if mutProb > 0 and mutProb < randomResetProb:
                mutation = randomResetting
                print("Random reset")
            elif mutProb > randomResetProb and mutProb < randomResetProb + creepProb:
                mutation = creepMutation
                print("Creep mutation")
            elif mutProb > randomResetProb + creepProb and mutProb < 1:
                print("Scramble")
                mutation = scrambleMutation



            print("mutation", mutation)

            print("run", run + 1)
            print("gen", gen + 1)
            print("Mutation rate", config.mutationRate)

            selection()
            crossover()
            mutation()

            calculateNewPopulationFitness()

            meanFitness()
            bestFitness()

            # Storing the current and best fitness for each generation
            config.allFitnessInfo[run][gen] = copy.deepcopy(config.currentFitness)

            # storing every fitness for each generation
            currentFitnesses = []
            for i in config.currentPopulation:
                currentFitnesses.append(i.fitness)
            config.allFitness[run][gen] = copy.deepcopy(currentFitnesses)

            # storing all memebers of the population
            config.allIndivduals[run][gen] = copy.deepcopy(config.currentPopulation)


            print("randomResetProb",randomResetProb)
            print("creepProb", creepProb)
            print("scrambleProb", scrambleProb)
            print()
            # Since there would be no data to calculate how well a generation has performed, sucsess of mutation can't be calculated till passed gen 1
            if gen > 0:
                print("Passed Gen one",config.allFitnessInfo[run][gen-1][1])
                print("Current Gen one",config.allFitnessInfo[run][gen][1])
                if config.allFitnessInfo[run][gen][1] < config.allFitnessInfo[run][gen - 1][1]:
                    print("current Rate better then previous")
                    if mutation is randomResetting:
                        randomResetProb = round(randomResetProb * 101/100,4)

                        creepProb = round(creepProb * 299/300,4)

                        scrambleProb = round(scrambleProb * 299/300,4)

                    elif mutation is creepMutation:
                        randomResetProb = round(randomResetProb * 299/300,4)

                        creepProb = round(creepProb * 101/100,4)

                        scrambleProb = round(scrambleProb * 299/300,4)

                    elif mutation is scrambleMutation:

                        randomResetProb = round(randomResetProb * 299/300,4)

                        creepProb = round(creepProb * 299/300,4)

                        scrambleProb = round(scrambleProb * 101/100,4)

            print("randomResetProb", randomResetProb)
            print("creepProb", creepProb)
            print("scrambleProb", scrambleProb)

            print("Sum=",randomResetProb+creepProb+scrambleProb)

            # if randomResetProb > 1:
            #     randomResetProb = 1
            # elif randomResetProb < 0:
            #     randomResetProb = 0
            #
            # if creepProb > 1:
            #     creepProb = 1
            # elif creepProb < 0:
            #     creepProb = 0

            survirorSelection()

            # print("Creep After ", creepProb)
            # print("Random after ", randomResetProb)
            #
            # print("---------")

            print()
            print()
            print()
            print()
            print()

        config.allTopFitness[run] = copy.deepcopy(config.topFitness)
        config.allGenofFitness[run] = copy.deepcopy(config.genOfFitness)

        finalProbabilitesForRun[run][0] = copy.deepcopy(randomResetProb)
        finalProbabilitesForRun[run][1] = copy.deepcopy(creepProb)

    writeToSpreadSheet()

    print(finalProbabilitesForRun)

def test9():

    config.runData = "adaptive between scramble and creep"

    scrambleProb = 0.5

    creepProb = 0.5

    finalProbabilitesForRun = [[0.0 for i in range(2)] for w in range(config.numberOfRuns)]

    selection = tournamentSelection
    crossover = uniformCrossover

    for run in range(config.numberOfRuns):
        config.run = run

        initialisePopulation()



        for gen in range(config.numberOfGenerations):
            config.gen = gen

            #Select Crossover Type
            mutProb = random.uniform(0,1)
            print("mutProb",mutProb)
            print("scrambleProb",scrambleProb)
            print("creepProb",creepProb)

            if mutProb > scrambleProb:
                mutation = scrambleMutation
            elif mutProb < creepProb:
                mutation = creepMutation

            print("mutation",mutation)





            print("run", run + 1)
            print("gen", gen + 1)
            print("Mutation rate", config.mutationRate)

            selection()
            crossover()
            mutation()

            calculateNewPopulationFitness()

            meanFitness()
            bestFitness()



            # Storing the current and best fitness for each generation
            config.allFitnessInfo[run][gen] = copy.deepcopy(config.currentFitness)

            # storing every fitness for each generation
            currentFitnesses = []
            for i in config.currentPopulation:
                currentFitnesses.append(i.fitness)
            config.allFitness[run][gen] = copy.deepcopy(currentFitnesses)


            listOfGenes = []

            for i in config.currentPopulation:
                for j in i.chromosome:
                    listOfGenes.append(j)

            std = np.std(listOfGenes)
            mean = np.std(listOfGenes)

            step = np.random.normal(loc=mean ,scale=std)

            config.mutationStep = step

            # storing all memebers of the population
            config.allIndivduals[run][gen] = copy.deepcopy(config.currentPopulation)

            # print("------------")
            #
            # print("Creep Before ",creepProb)
            # print("Random Before ",randomResetProb)
            # print("Current mutation type",mutation)

            # Since there would be no data to calculate how well a generation has performed, sucsess of mutation can't be calculated till passed gen 1
            if gen > 0:
                # print("Passed Gen one",config.allFitnessInfo[run][gen-1][1])
                # print("Current Gen one",config.allFitnessInfo[run][gen][1])
                if config.allFitnessInfo[run][gen][1] < config.allFitnessInfo[run][gen-1][1]:
                    # print("current Rate better then previous")

                    if mutation is scrambleMutation:
                        # print("Randomresetting")
                        # Making random reset more likely and making creep less likley
                        scrambleProb = scrambleProb * 1.006
                        creepProb = 1 - scrambleProb
                    elif mutation is creepMutation:
                        # print("creepMutation")
                        # Making creep more likely and making random reset less likley
                        creepProb = creepProb * 1.006
                        scrambleProb = 1 - creepProb






            if scrambleProb >= 0.97:
                scrambleProb = 0.97
                creepProb = 0.03
            elif scrambleProb < 0.05:
                scrambleProb = 0.03
                creepProb = 0.97

            if creepProb >= 0.97:
                scrambleProb = 0.03
                creepProb = 0.97
            elif creepProb < 0.05:
                scrambleProb = 0.95
                creepProb = 0.03







            survirorSelection()

            # print("Creep After ", creepProb)
            # print("Random after ", randomResetProb)
            #
            # print("---------")


        config.allTopFitness[run] = copy.deepcopy(config.topFitness)
        config.allGenofFitness[run] = copy.deepcopy(config.genOfFitness)

        finalProbabilitesForRun[run][0] = copy.deepcopy(scrambleProb)
        finalProbabilitesForRun[run][1] = copy.deepcopy(creepProb)



    writeToSpreadSheet()

    print(finalProbabilitesForRun)

    finish = False

    while not finish:
        decision = input('Enter v to view population or press e to end ')
        if decision == 'e':
            finish = True
        elif decision == 'v':
            run = int(input('Enter run '))
            gen = int(input('Enter gen '))
            printGenePopulation(config.allIndivduals[run - 1][gen - 1])



def test11():

    config.runData = "adaptive between scramble and creep, whole arithmetic"

    scrambleProb = 0.5

    creepProb = 0.5

    finalProbabilitesForRun = [[0.0 for i in range(2)] for w in range(config.numberOfRuns)]

    selection = survirorSelection
    mutation = creepMutation
    crossover = uniformCrossover

    for run in range(config.numberOfRuns):
        config.run = run

        initialisePopulation()

        for gen in range(config.numberOfGenerations):
            config.gen = gen

            #Select Crossover Type
            mutProb = random.uniform(0,1)
            print("mutProb",mutProb)
            print("scrambleProb",scrambleProb)
            print("creepProb",creepProb)

            if mutProb > scrambleProb:
                mutation = scrambleMutation
            elif mutProb < creepProb:
                mutation = creepMutation

            print("mutation",mutation)





            print("run", run + 1)
            print("gen", gen + 1)
            print("Mutation rate", config.mutationRate)

            selection()
            crossover()
            mutation()

            calculateNewPopulationFitness()

            meanFitness()
            bestFitness()



            # Storing the current and best fitness for each generation
            config.allFitnessInfo[run][gen] = copy.deepcopy(config.currentFitness)

            # storing every fitness for each generation
            currentFitnesses = []
            for i in config.currentPopulation:
                currentFitnesses.append(i.fitness)
            config.allFitness[run][gen] = copy.deepcopy(currentFitnesses)


            listOfGenes = []

            for i in config.currentPopulation:
                for j in i.chromosome:
                    listOfGenes.append(j)

            std = np.std(listOfGenes)
            mean = np.std(listOfGenes)

            step = np.random.normal(loc=mean ,scale=std)

            config.mutationStep = step

            # storing all memebers of the population
            config.allIndivduals[run][gen] = copy.deepcopy(config.currentPopulation)

            # print("------------")
            #
            # print("Creep Before ",creepProb)
            # print("Random Before ",randomResetProb)
            # print("Current mutation type",mutation)

            # Since there would be no data to calculate how well a generation has performed, sucsess of mutation can't be calculated till passed gen 1
            if gen > 0:
                # print("Passed Gen one",config.allFitnessInfo[run][gen-1][1])
                # print("Current Gen one",config.allFitnessInfo[run][gen][1])
                if config.allFitnessInfo[run][gen][1] < config.allFitnessInfo[run][gen-1][1]:
                    # print("current Rate better then previous")

                    if mutation is scrambleMutation:
                        # print("Randomresetting")
                        # Making random reset more likely and making creep less likley
                        scrambleProb = scrambleProb * 1.006
                        creepProb = 1 - scrambleProb
                    elif mutation is creepMutation:
                        # print("creepMutation")
                        # Making creep more likely and making random reset less likley
                        creepProb = creepProb * 1.006
                        scrambleProb = 1 - creepProb






            if scrambleProb >= 0.97:
                scrambleProb = 0.97
                creepProb = 0.03
            elif scrambleProb < 0.05:
                scrambleProb = 0.03
                creepProb = 0.97

            if creepProb >= 0.97:
                scrambleProb = 0.03
                creepProb = 0.97
            elif creepProb < 0.05:
                scrambleProb = 0.95
                creepProb = 0.03







            survirorSelection()

            # print("Creep After ", creepProb)
            # print("Random after ", randomResetProb)
            #
            # print("---------")


        config.allTopFitness[run] = copy.deepcopy(config.topFitness)
        config.allGenofFitness[run] = copy.deepcopy(config.genOfFitness)

        finalProbabilitesForRun[run][0] = copy.deepcopy(scrambleProb)
        finalProbabilitesForRun[run][1] = copy.deepcopy(creepProb)



    writeToSpreadSheet()

    print(finalProbabilitesForRun)

    finish = False

    while not finish:
        decision = input('Enter v to view population or press e to end ')
        if decision == 'e':
            finish = True
        elif decision == 'v':
            run = int(input('Enter run '))
            gen = int(input('Enter gen '))
            printGenePopulation(config.allIndivduals[run - 1][gen - 1])


def objective(x):
    return 10 + x ** 2 - (10 * np.cos(2 * np.pi * x))


def plot_n_points(x):

    # define range for input
    r_min, r_max = -5.12, 5.12
    # sample input range uniformly at 0.1 increments
    inputs = arange(r_min, r_max, 0.1)
    # compute targets
    results = objective(inputs)



    print("x", x)

    clear_output(wait=True)
    print("x", x)

    # corrects offset to plot on graph
    x_plot = np.add(x, 5)
    print("x add 5", x_plot)

    x_plot = np.multiply(x, 10)
    print("x * 10", x_plot)

    x_plot = np.round(x_plot).astype(int)
    print("x rounded ", x_plot)
    print("x rounded dtype ", type(x_plot[0]))

    pyplot.plot(inputs, results, '-bD', markevery=[x_plot])

    pyplot.show()
    time.sleep(0.25)

def test12():
    config.runData = "non adaptive, whole aethmetic and scramble"

    # for learning visualiser
    all_objective_mean_individuals = np.array([])


    finalProbabilitesForRun = [[0.0 for i in range(2)] for w in range(config.numberOfRuns)]

    selection = survirorSelection
    mutation = creepMutation
    crossover = uniformCrossover

    for run in range(config.numberOfRuns):
        config.run = run

        initialisePopulation()

        for gen in range(config.numberOfGenerations):
            config.gen = gen



            print("run", run + 1)
            print("gen", gen + 1)


            selection()
            crossover()
            mutation()

            calculateNewPopulationFitness()

            meanFitness()
            bestFitness()

            # Storing the current and best fitness for each generation
            config.allFitnessInfo[run][gen] = copy.deepcopy(config.currentFitness)

            debug_counter = 0

            mean_indivudals = np.array([])

            # storing every fitness for each generation
            currentFitnesses = []
            for i in config.currentPopulation:
                currentFitnesses.append(i.fitness)

                chromsomes =  i.chromosome
                mean_of_chromsomes = np.mean(chromsomes)

                mean_indivudals = np.append(mean_indivudals,mean_of_chromsomes)


                # print("mean_of_chromsomes",mean_of_chromsomes)

            print("mean_indivudals", mean_indivudals)
            print("mean indv shape", mean_indivudals.shape)




            # plot vector on graph
            # print("reduces_fitness ",objective(mean_indivudals))

            objective_mean_indivudals = mean_indivudals

            # interface to visualiser goes here
            # plot_n_points(mean_indivudals)
            all_objective_mean_individuals = np.append(all_objective_mean_individuals,mean_indivudals)



            config.allFitness[run][gen] = copy.deepcopy(currentFitnesses)



            # storing all memebers of the population
            config.allIndivduals[run][gen] = copy.deepcopy(config.currentPopulation)


            # survirorSelection()

            # print("Creep After ", creepProb)
            # print("Random after ", randomResetProb)
            #
            # print("---------")

        config.allTopFitness[run] = copy.deepcopy(config.topFitness)
        config.allGenofFitness[run] = copy.deepcopy(config.genOfFitness)


    writeToSpreadSheet()

    # print(finalProbabilitesForRun)



    finish = False

    while not finish:
        decision = input('Enter v to view population or press e to end ')
        if decision == 'e':
            finish = True
        elif decision == 'v':
            run = int(input('Enter run '))
            gen = int(input('Enter gen '))
            printGenePopulation(config.allIndivduals[run - 1][gen - 1])

