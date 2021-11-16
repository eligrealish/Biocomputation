import copy
import random
import config
import numpy as np
from individual import individual

def tournamentSelection(population = None):
    # print("-------TOURNAMENT SELECTION RUN-------")
    #if a value not passed set to current population
    if not population:
        population = config.currentPopulation

    #Global variables are assigned for readability
    tornamuntSize = config.tornamuntSize
    P = config.P
    newPopulation = []

    # print("Population", population)
    # print("len(population)",len(population))


    for i in range(0,P):

        tornamuntPopulation = []

        while len(tornamuntPopulation) < tornamuntSize:


            randomIndivdual = population[random.randint(0,len(population)-1)]
            # print("randomIndivdual",randomIndivdual.fitness)

            #to avoid indviduals occouring more then once in population
            if randomIndivdual not in tornamuntPopulation:
                tornamuntPopulation.append(randomIndivdual)

            # print("tornamunt population",tornamuntPopulation)

        minPosition = 0

        for czonePosition in range(1,len(tornamuntPopulation)):
            if tornamuntPopulation[czonePosition].fitness < tornamuntPopulation[minPosition].fitness:
                minPosition = czonePosition

        # for i in tornamuntPopulation:
        #     print(i.fitness)
        # print("minPosition",minPosition)

        newPopulation.append(copy.deepcopy(tornamuntPopulation[minPosition]))



    # for i in newPopulation:
    #     print(i.fitness)

    config.currentPopulation = newPopulation


def survirorSelection():
    # print("-------SURVIROR SELECTION RUN-------")
    # Make 0.2 value adjustable in config file
    amountToBeRemoved = round(config.P * config.elitePercentage)

    # print("amountToBeRemoved",amountToBeRemoved)

    orderedIndivudals = copy.deepcopy(config.currentPopulation)

    for i in range(len(orderedIndivudals)):
        for j in range(i + 1, len(orderedIndivudals)):

            if orderedIndivudals[i].fitness > orderedIndivudals[j].fitness:
                orderedIndivudals[i], orderedIndivudals[j] = orderedIndivudals[j], orderedIndivudals[i]


    eliteIndividuals = orderedIndivudals[:-amountToBeRemoved]


    # print("------orderedIndivudals-----")
    # for x in orderedIndivudals:
    #     print(x.fitness)
    #
    # print("------eliteIndividuals-----")
    # for x in eliteIndividuals:
    #     print(x.fitness)

    tournamentSelection(eliteIndividuals)





def fitnessProportionateSelection():
    print("-------FITNESS PROPORTIONAL SELECTION RUN-------")

    # Global variable are assigned for readability
    currentPopulation = config.currentPopulation


    # Finesses bellow, not be worth correct segment of wheel if below 0, due to the nature of division with negative numbers
    # The smallest value must be found below, if one exists and is used to make every fitness positive
    currentMin = 0
    for i in range(0,len(currentPopulation)):
        if currentPopulation[i].fitness < 0:
            print("value thats less then 0",currentPopulation[i].fitness)
            if currentPopulation[i].fitness < currentPopulation[currentMin].fitness:
                currentMin = i

    print("currentMin",currentMin)

    positiveNormaliser = currentPopulation[currentMin].fitness * - 1

    print("positiveNormaliser",positiveNormaliser)

    fitnessAboveZero = []

    for i in currentPopulation:
        fitnessAboveZero.append(i.fitness + positiveNormaliser)

    for i in fitnessAboveZero:
        print("fitnessAboveZero,i",i)

    fitnessTotal = sum(fitnessAboveZero)

    print("fitTotal",fitnessTotal)

    normalisedFitness = []

    for i in fitnessAboveZero:
        normalisedFitness.append(fitnessTotal - i)

    print("normalisedFitness", normalisedFitness)

    smallestNormalisedFitness = min(normalisedFitness)

    print("smallestNormalisedFitness",smallestNormalisedFitness)

    for i in range(0,len(normalisedFitness)):

        normalisedFitness[i] = normalisedFitness[i] - smallestNormalisedFitness

    print("normalisedFitness",normalisedFitness)

    normalisedFitnessTotal = sum(normalisedFitness)

    print("-------")
    print("normalisedFitnessTotal",normalisedFitnessTotal)

    fitnessProbabilites = [0]

    for i in range(0,len(normalisedFitness)):

        fitnessProbabilites.append(fitnessProbabilites[i]+normalisedFitness[i]/normalisedFitnessTotal)


    print("fitnessProbabilites", fitnessProbabilites)


    newPopulation = []

    for i in range(config.P):

        # Since on some runs the maximum probability is 0.9 recurring, due to the decimal place python decides to round the number too
        # the max number for the uniform distribution is the highest number in the fitness either 1 or 0.999 to avoid potential errors later
        randomValue = random.uniform(0, fitnessProbabilites[len(fitnessProbabilites) - 1])
        print("randomValue",randomValue)

        for i in range(0,len(fitnessProbabilites)-1):
            if randomValue > fitnessProbabilites[i] and randomValue < fitnessProbabilites[i+1]:
                newPopulation.append(copy.deepcopy(currentPopulation[i]))



    config.currentPopulation = newPopulation

    # print("newPopulation",newPopulation)
    # for i in newPopulation:
    #     print("fitness i",i.fitness)

