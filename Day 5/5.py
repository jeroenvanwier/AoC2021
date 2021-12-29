import numpy as np


if __name__=="__main__":
    f = open("input.txt")
    raw_lines = f.read().split('\n')
    lines = []
    for line in raw_lines[:-1]:
        se = line.split(" -> ")
        s = se[0].split(',')
        e = se[1].split(',')
        lines.append([(int(s[0]),int(s[1])), (int(e[0]),int(e[1]))])
    m = 0
    for line in lines:
        for c in line:
            for d in c:
                if d > m:
                    m = d
    grid = np.zeros((m + 1, m + 1))
    for line in lines:
        if line[0][0] == line[1][0]:
            x = line[0][0]
            sy, ey = line[0][1], line[1][1]
            if sy > ey:
                sy, ey = ey, sy
            for y in range(sy, ey + 1):
                grid[x][y] += 1
        elif line[0][1] == line[1][1]:
            y = line[0][1]
            sx, ex = line[0][0], line[1][0]
            if sx > ex:
                sx, ex = ex, sx
            for x in range(sx, ex + 1):
                grid[x][y] += 1
        else:
            sx, ex = line[0][0], line[1][0]
            if sx > ex:
                sx, ex = ex, sx
                line = line[::-1]
            sy, ey = line[0][1], line[1][1]
            if sy < ey:
                for i in range(ex - sx + 1):
                    grid[sx + i][sy + i] += 1
            else:
                for i in range(ex - sx + 1):
                    grid[sx + i][sy - i] += 1
    total = 0
    for line in grid:
        for pos in line:
            if pos > 1:
                total += 1
    print(total)