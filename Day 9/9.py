def around(pos):
    x, y = pos[0], pos[1]
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

def is_in(pos, hmap):
    return pos[0] >= 0 and pos[0] < len(hmap[0]) and pos[1] >= 0 and pos[1] < len(hmap)

def find_basin(hmap, basin, current):
    for pos in around(current):
        if is_in(pos, hmap) and pos not in basin and hmap[pos[1]][pos[0]] < 9:
            basin.append(pos)
            find_basin(hmap, basin, pos)

if __name__=="__main__":
    f = open("input.txt")
    raw_map = f.read().split('\n')[:-1]
    hmap = []
    for line in raw_map:
        hmap.append([int(x) for x in line])
    low_points = []
    for y in range(len(hmap)):
        for x in range(len(hmap[0])):
            if x == 0 or hmap[y][x-1] > hmap[y][x]:
                if x == len(hmap[0]) - 1 or hmap[y][x+1] > hmap[y][x]:
                    if y == 0 or hmap[y-1][x] > hmap[y][x]:
                        if y == len(hmap) - 1 or hmap[y+1][x] > hmap[y][x]:
                            low_points.append((x, y))
    basins = []
    for point in low_points:
        basin = [point]
        find_basin(hmap, basin, point)
        basins.append(len(basin))
    basins.sort(reverse=True)
    print(basins[0] * basins[1] * basins[2])