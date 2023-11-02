import random

num = 2

def simulationList(simulations):
    simulations = 10

    launch = [random.randint(1, 6),random.randint(1, 6),random.randint(1, 6)]
    print(launch)

    simul1 = []
    for num in range(simulations):
        if launch == num:
            count +=1

    P = count/simulations

simulationList(10)