import random
import config
import copy


def onePointCrossover():
    # print("-------ONE POINT CROSSOVER RUN-------")
    for i in range(0, len(config.currentPopulation), 2):
        # print("-----------------")
        crosspoint = random.randint(0, config.N)
        # print("crosspoint=", crosspoint)
        #
        # print("population[i].chromosome =", config.currentPopulation[i].chromosome)
        # print("population[i+1].chromosome =", config.currentPopulation[i + 1].chromosome)

        chromosomeA1 = config.currentPopulation[i].chromosome[0:crosspoint]
        chromosomeA2 = config.currentPopulation[i].chromosome[crosspoint:config.N]

        # print("chromosomeA1=", chromosomeA1)
        # print("chromosomeA2=", chromosomeA2)

        chromosomeB1 = config.currentPopulation[i + 1].chromosome[0:crosspoint]
        chromosomeB2 = config.currentPopulation[i + 1].chromosome[crosspoint:config.N]

        # print("chromosomeB1=", chromosomeB1)
        # print("chromosomeB2=", chromosomeB2)

        config.currentPopulation[i].chromosome = chromosomeA1 + chromosomeB2

        config.currentPopulation[i + 1].chromosome = chromosomeB1 + chromosomeA2

        # print("population[i].chromosome =", config.currentPopulation[i].chromosome)
        # print("population[i+1].chromosome =", config.currentPopulation[i + 1].chromosome)
        # print("-----------------")


def artimethicCombination(valueA,valueB,P):
    newValueA = (P * valueA) + (1-P)*valueB
    newValueB = (P * valueB) + (1-P)*valueA

    return newValueA,newValueB

def simpleArithmeticRecombination():
    # print("-------SIMPLE ARITHMETIC RECOMBINATION CROSSOVER RUN-------")

    for i in range(0, len(config.currentPopulation), 2):

        czoneA = config.currentPopulation[i].chromosome
        czoneB = config.currentPopulation[i+1].chromosome

        # print("czoneA", czoneA)
        # print("czoneB", czoneB)


        crosspoint = random.randint(0, config.N-1)

        # print("Crossvalue", crosspoint)

        for j in range(crosspoint, config.N):
            newValues = artimethicCombination(czoneA[j], czoneB[j], config.arithmeticP)
            czoneA[j] = newValues[0]
            czoneB[j] = newValues[1]

        # print("czoneA", czoneA)
        # print("czoneB", czoneB)
        #
        # print("------------")




def singleArithmeticRecombination():
    # print("-------SINGLE ARITHMETIC RECOMBINATION CROSSOVER RUN-------")

    for i in range(0, len(config.currentPopulation), 2):

        czoneA = config.currentPopulation[i].chromosome
        czoneB = config.currentPopulation[i+1].chromosome


        crossValue = random.randint(0, config.N-1)

        # print("Crossvalue",crossValue)
        #
        # print("czoneA",czoneA)
        # print("czoneB", czoneB)

        newValues = artimethicCombination(czoneA[crossValue], czoneB[crossValue], config.arithmeticP)
        czoneA[crossValue] = newValues[0]
        czoneB[crossValue] = newValues[1]

        # print("czoneA", czoneA)
        # print("czoneB", czoneB)



def wholeArithmeticRecombination():
    # print("-------WHOLE ARITHMETIC RECOMBINATION CROSSOVER RUN-------")

    for i in range(0, len(config.currentPopulation), 2):

        czoneA = config.currentPopulation[i].chromosome
        czoneB = config.currentPopulation[i+1].chromosome

        # print("czoneA", czoneA)
        # print("czoneB", czoneB)


        for j in range(0, config.N):
            newValues = artimethicCombination(czoneA[j], czoneB[j], config.arithmeticP)
            czoneA[j] = newValues[0]
            czoneB[j] = newValues[1]

        # print("czoneA", czoneA)
        # print("czoneB", czoneB)
        #
        # print("------------------")


def uniformCrossover():
    # print("-------UNIFORM CROSSOVER RUN-------")
    for i in range(0, len(config.currentPopulation), 2):

        czoneA = config.currentPopulation[i].chromosome
        czoneB = config.currentPopulation[i+1].chromosome


        for j in range(0, config.N):
            changingProb = random.uniform(0, 1)
            # print("Changing prob",changingProb )
            if changingProb > config.uniformP:
                # print("On Czone",i)
                # print("Triggerd during",j)
                tempGene = czoneA[j]
                czoneA[j] = czoneB[j]
                czoneB[j] = tempGene

