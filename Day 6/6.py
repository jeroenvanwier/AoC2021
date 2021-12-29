import numpy as np


if __name__=="__main__":
    f = open("input.txt")
    ages = [0]*10
    ages_in = f.readline().split(',')
    for age in ages_in:
        ages[int(age)] += 1
    print(ages)
    for day in range(256):
        ages[9] = ages[0]
        ages[7] += ages[0]
        ages = ages[1:10]
        ages.append(0)
        print(ages)
    print(sum(ages))