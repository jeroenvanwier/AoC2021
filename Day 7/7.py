import numpy as np

def fuel_used(a, b):
    if a > b:
        a, b = b, a
    diff = b - a
    return (diff * (diff + 1)) / 2

def calc_fuel(pos, target):
    fuel = 0
    for i in range(len(pos)):
        fuel += fuel_used(i, target) * pos[i]
    return fuel

if __name__=="__main__":
    f = open("input.txt")
    pos_in = f.readline().split(',')
    pos_in = [int(x) for x in pos_in]
    pos = [0]*(max(pos_in)+1)
    for p in pos_in:
        pos[int(p)] += 1
    fuels = [calc_fuel(pos, x) for x in range(len(pos))]
    print(min(fuels))