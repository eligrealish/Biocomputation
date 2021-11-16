import config
import individual
import random
import numpy as np


def creepMutation():
    # print("-------CREEP MUTATION RUN-------")


    for i in range(0, len(config.currentPopulation)):



        for j in range(0, len(config.currentPopulation[i].chromosome)):
            mutprob = random.randint(0, 100)
            # print("mutation prob =", mutprob)
            if mutprob < (100 * config.mutationRate):
                alter = random.uniform(-config.mutationStep, config.mutationStep)
                config.currentPopulation[i].chromosome[j] = config.currentPopulation[i].chromosome[j] + alter
                # print("alter",alter)
                # print("BEFORE", config.currentPopulation[i].chromosome[j])
                # config.currentPopulation[i].chromosome[j] = config.currentPopulation[i].chromosome[j] + alter
                # print("AFTER",config.currentPopulation[i].chromosome[j])

            #IF currentIndivdaulGeneValue < minRange THEN
                # currentIndivdaulGeneValue == minRange
            #ELSE IF currentIndivdaulGeneValue > maxRange THEN
                # currentIndivdaulGeneValue = maxRange

            # config.currentPopulation[i].chromosome[j] = 5.12
            # print("BEFORE config.currentPopulation[i].chromosome[j] = ", config.currentPopulation[i].chromosome[j])

            if config.currentPopulation[i].chromosome[j] < config.minRange:
                # print("TEST LESS THEN OR LESS THEN EQUALS")
                config.currentPopulation[i].chromosome[j] = config.minRange

            if config.currentPopulation[i].chromosome[j] > config.maxRange:
                # print("TEST GREATER THEN OR GREATER THEN EQUALS")
                config.currentPopulation[i].chromosome[j] = config.maxRange

            # print("AFTER config.currentPopulation[i].chromosome[j] = ", config.currentPopulation[i].chromosome[j])


def scrambleMutation():
    # print("-------SCRMABLE MUTATION RUN-------")
    N = config.N

    for i in range(0, len(config.currentPopulation)):

        currentGene = config.currentPopulation[i].chromosome

        #to ensure the maximum value isn't chosen, N is subtracted by 2
        mutPoint1 = random.randint(0, N - 2)

        #to make sure the same value isn't chosen, mutpoint has 1 addde
        mutPoint2 = random.randint(mutPoint1 + 1, N - 1)

        # print("mutpoint1=",mutPoint1)
        #
        # print("mutpoint2=", mutPoint2)

        chromsonemid = currentGene[mutPoint1:mutPoint2]

        # print("currentGene = ",currentGene)
        #
        # print("chromsonemid",chromsonemid)

        random.shuffle(chromsonemid)

        # print("chromsonemid", chromsonemid)


        currentGene[mutPoint1:mutPoint2] = chromsonemid

        # print("currentGene = ", currentGene)
        #
        # print("currenpop[i]", config.currentPopulation[i].chromosome)



def randomResetting():
    # print("-------RANDOM RESETTING MUTATION RUN-------")
    for i in range(0, len(config.currentPopulation)):
        # print("i",i)

        # print("config.currentPopulation[i].chromosome", config.currentPopulation[i].chromosome)

        for j in range(0, len(config.currentPopulation[i].chromosome)):

            mutprob = random.randint(0, 100)
            # print("mutprob",mutprob)
            # print("j", j)
            if mutprob < (100 * config.mutationRate):
                # print("Mutation Triggered!!!")

                # print("config.currentPopulation[i].chromosome", config.currentPopulation[i].chromosome)
                # print("config.currentPopulation[i].chromosome[j]", config.currentPopulation[i].chromosome[j])


                newGene = random.uniform(config.minRange, config.maxRange)
                # print("newGene",newGene)

                config.currentPopulation[i].chromosome[j] = newGene

        # print("config.currentPopulation[i].chromosome", config.currentPopulation[i].chromosome)
        # print("Gene finished")


