
#-------System Constants------ MAYBE RENAME THESE NOTES
#GENERATION AND RUNS
gen = 0

run = 0





# Number of Genes
N = 10

# Population size, must be factor of 2
P = 10


numberOfGenerations = 5

numberOfRuns = 1

#-------System Algorithm Parameters-----
# Chosing mutation type
selectionType = "T"

# Tournament size for tournament selection
tornamuntSize = 2

# The elite percentage for survivor Selection,note it is the inverse, if =0.2(20%), the eliete indivudals are the other 80%
elitePercentage = 0.2


#CROSSOVER PARAMETERS

# Chosing crossover type
crossoverType = "O"

# Arthimetic probabliltiy for the three types of arithmetic crossover
arithmeticP = 0.7

#probability off swapping a gene in uniform crossover
uniformP = 0.5

#MUATION PARAMETERS

# Chosing mutation type
mutationType = "C"


# Chosing the mutation step size for mutation creep

mutationStep = 0.5

# Mutation rate i.e how often mutation occurs for mstep and random resetting
mutationRate = 0.01




#--------Blank Population List---------
currentPopulation = []

listOfPopulation = []

#-----Blank total ,higest and mean fitness lists-----
#----2D ARRAY,POS 0 Mean Fitness, Pos 1 Best Fitness---

#the current best and mean fitness
currentFitness = [0.0, 0.0]

#the best record best and mean fitness for a given run
topFitness = [0.0, 0.0]

#the generation this best and mean fitness occured
genOfFitness = [0.0, 0.0]

#every run and generations best and mean
allFitnessInfo = [[[0.0 for i in range(2)] for j in range(numberOfGenerations)] for w in range(numberOfRuns)]

#every indivudal fitness for every run and generation
allFitness = [[[0.0 for i in range(N)] for j in range(numberOfGenerations)] for w in range(numberOfRuns)]

#every the best and mean fitness recorded after each run
allTopFitness = [[0.0 for i in range(2)] for w in range(numberOfRuns)]

#every generation the best and mean fitness recorded after each run
allGenofFitness = [[0.0 for i in range(2)] for w in range(numberOfRuns)]

# Fitness function
fitnessFunction = 1

if fitnessFunction == 1:
    minRange,maxRange = -5.12, 5.12
elif fitnessFunction == 2:
    minRange,maxRange = -32.0, 32.0






