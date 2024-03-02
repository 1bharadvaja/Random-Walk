import random

total = 0

def randWalk(ruin, win, curr, counter):
    if (curr == win or curr == ruin):
        return counter
    return randWalk(ruin, win, curr + 2*random.randint(0, 1) - 1, counter + 1)

i = 0
while (i <= 10000):
    total += randWalk(-10, 7, 0, 0)
    i += 1

print(total/i)