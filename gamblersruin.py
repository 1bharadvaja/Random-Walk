import random


def returnEV(iterations, ruin, win):
    total = 0
    def randWalk(ruin, win, curr, counter):
        if (curr == win or curr == ruin):
            return counter
        return randWalk(ruin, win, curr + 2*random.randint(0, 1) - 1, counter + 1)

    i = 0
    while (i <= iterations):
        total += randWalk(ruin, win, 0, 0)
        i += 1

    return total/iterations #EV comes out to -ruin*win which checks out

returnEV(10000, -10, 7)