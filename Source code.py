# In a gameshow contestants want to guess which of the three closed doors contain the cash prize
# the odds of choosing the corrent door are 1 in 3...
# given that the host opens one door and reveals that it is a goat (not the cash prize)
# should the contestant stay with the door they picked or change?

# the approach
# create a simulation where a contestant will pick a door and not change. find the probability of him winning
# create another simulation where the contestant does change and find the probability of him winning

import numpy as np
import scipy as sp

# the number of simulations to run
nsim = 10000

#creates a random array of 0s 1s and 2s. the prize will be behind door '0' '1' or '2'

def simulate_prizedoor(nsim):
    return np.random.randint(0, 3, (nsim))

# The initial guess of the contestant in this case i have set that to be 0 each time
def simulate_guess(nsim):
    return np.zeros(nsim,dtype =np.int)

#the door which is opened after the contestant has picked a door. the door will contain a goat
def goat_door(prizedoors,guesses):
    # generate random answers and keep updating until they are'nt a prizedoor or guess

    result = np.random.randint(0,3,prizedoors.size)
    while True:
        bad = (result == prizedoors) | (result == guesses)
        if not bad.any():
            return result
        result[bad] = np.random.randint(0,3,bad.sum())

#creates the option to change a contestants initial pick after the host opens the door
def switch_guess(guesses,goatdoors):
    result = np.zeros(guesses.size)
    switch = {(0,1): 2,(0,2): 1,(1,0): 2,(1,2): 1,(2,0): 1,(2,1): 0}
    for i in [0,1,2]:
        for j in [0,1,2]:
            mask = (guesses == i) & (goatdoors == j)
            if not mask.any():
                continue
            result = np.where(mask, np.ones_like(result) * switch[(i, j)], result)
    return result

# simple calculation for getting the win percentage of contestant
def win_percentage(guesses, prizedoors):
    return 100 * (guesses == prizedoors).mean()


# percentage of win for intitial guess
print("Win percentage when keeping original door")
print(win_percentage(simulate_prizedoor(nsim), simulate_guess(nsim)))

#percentage of win for changed guess
pd = simulate_prizedoor(nsim)
guess = simulate_guess(nsim)
goats = (goat_door(pd,guess))
guess = switch_guess(guess,goats)

print("win percentage when switching doors")
print(win_percentage(pd, guess).mean())












