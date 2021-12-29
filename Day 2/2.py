if __name__=="__main__":
    f = open("input.txt")
    x, y, aim = 0, 0, 0
    for line in f:
        order = line.split()
        d = int(order[1])
        if order[0] == "up":
            aim -= d
        elif order[0] == "down":
            aim += d
        elif order[0] == "forward":
            x += d
            y += aim * d
        else:
            print("Woops")
    print(x * y)
    