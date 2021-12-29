def sim(x, y, i):
    pos = [0,0]
    for j in range(i):
        pos[0] += x
        if x > 0:
            x -= 1
        pos[1] += y
        y -= 1
    return pos

if __name__=="__main__":
    f = open("input.txt")
    lines = f.read().split('\n')[:-1]
    line = lines[0][13:]
    dims = [v[2:].split("..") for v in line.split(', ')]
    target = ((int(dims[0][0]), int(dims[0][1])), (int(dims[1][0]), int(dims[1][1])))
    # For first part: shooting up always arcs such that after 2y + 1 step the probe returns to y=0 with -y-1 velocity
    # So max y is -1 * lowest y bound + 1, max height is max_y * (max_y + 1) / 2 (Euler sum)
    # So in our case: y limit is -68, max y is 67, 67*68/2 = 2278
    max_y_vel =  target[1][0] * -1 - 1
    max_steps =  2 * max_y_vel + 2
    velos = []
    for i in range(1, max_steps + 1):
        for x in range(target[0][1] + 1):
            for y in range(target[1][0], max_y_vel + 1):
                pos = sim(x, y, i)
                if pos[0] <= target[0][1] and pos[0] >= target[0][0] and pos[1] >= target[1][0] and pos[1] <= target[1][1]:
                    if (x,y) not in velos:
                        velos.append((x,y))
    print(len(velos))