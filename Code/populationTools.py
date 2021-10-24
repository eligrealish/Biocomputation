import random
import numpy as np
import config
from individual import individual


def calculateCzoneFitness(czone):
    # print("-------CALCUATING CHROMOSOME FITNESS-------")

    N = config.N

    if config.fitnessFunction == 1:
        fitnessPartB = 0
        for i in czone.chromosome:
            fitnessPartB = fitnessPartB + (i * i) - 10 * np.cos(2 * np.pi * i)
        czone.fitness = 10 * config.N + fitnessPartB
        # print("----------------------")
        # print("czone.chromosome=", czone.chromosome)
        # print("fitnessPartB=", fitnessPartB)
        # print("czone.fitness=", czone.fitness)

    elif config.fitnessFunction == 2:
        fitnessPartA = 0
        fitnessPartB = 0

        for i in czone.chromosome:
            fitnessPartA = fitnessPartA + (i * i)

            fitnessPartB = fitnessPartB + np.cos(2 * np.pi) * i

        czone.fitness = -20 * np.exp(1) * ((-0.2 * np.sqrt((1 / N) * fitnessPartA))) - np.exp(1) * ((1 / N) * fitnessPartB)




def printGenePopulation():
    # print("-------PRINTING POPULATION-------")
    for i in range(0, len(config.currentPopulation)):
        print(i)
        print(config.currentPopulation[i].chromosome)
        print("fitness=", config.currentPopulation[i].fitness)
        print()


def initialisePopulation():
    # print("-------INITIALISING POPULATION-------")


    config.currentPopulation = []
    for x in range(0, config.P):

        tempgene = []

        for x in range(0, config.N):
            tempgene.append(random.uniform(config.minRange, config.maxRange))

        newind = individual()
        newind.chromosome = tempgene.copy()

        calculateCzoneFitness(newind)

        config.currentPopulation.append(newind)

def calculateNewPopulationFitness():
    # print("-------CALCULATING NEW POPULATION FITNESS-------")
    for i in config.currentPopulation:
        calculateCzoneFitness(i)


#total fitness function must be run before this for an accurate result
def meanFitness():
    # print("-------CALCULATING MEAN FITNESS-------")
    gen = config.gen

    currentTotal = 0
    for i in config.currentPopulation:
        currentTotal = currentTotal + i.fitness

    # print("current total",currentTotal)


    currentMean = currentTotal / config.P
    bestMean = config.topFitness[0]
    bestPosition = config.genOfFitness[0]

    if gen == 0:
        bestMean = currentMean
        bestPosition = gen
    if currentMean < bestMean:
        bestMean = currentMean
        bestPosition = gen
    # print("currentMean =", currentMean)
    # print("bestMean =", bestMean)
    # print("bestPosition =", bestPosition)
    config.topFitness[0] = bestMean
    config.genOfFitness[0] = bestPosition
    config.currentFitness[0] = currentMean

def bestFitness():
    # print("-------CALCULATING BEST FITNESS-------")
    gen = config.gen

    bestBest = config.topFitness[1]
    bestPosition = config.genOfFitness[1]
    currentBest = config.currentPopulation[0].fitness

    # print("currentbest=" ,currentBest)
    for i in range(1,config.P):
        if config.currentPopulation[i].fitness < currentBest:
            currentBest = config.currentPopulation[i].fitness

    if gen == 0:
        bestBest = currentBest
        bestPosition = 0

    if currentBest < bestBest:
        bestBest = currentBest
        bestPosition = gen

    config.topFitness[1] = bestBest
    config.genOfFitness[1] = bestPosition
    config.currentFitness[1] = currentBest












