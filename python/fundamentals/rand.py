import random
def randInt(min = 0, max= 100):
    num = random.random()*(max-min)+min
    return round(num)

print(randInt(max = 50))