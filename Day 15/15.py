def around(pos): #Day 9
    x, y = pos[0], pos[1]
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

def is_in(pos, hmap): # Day 9
    return pos[0] >= 0 and pos[0] < len(hmap[0]) and pos[1] >= 0 and pos[1] < len(hmap)

if __name__=="__main__":
    f = open("input.txt")
    lines = f.read().split('\n')[:-1]
    field = []
    for line in lines:
        field.append([int(x) for x in line])
    width = len(field[0])
    for i in range(1,5):
        for line in field:
            new_line = [((x - 1 + i) % 9) + 1 for x in line[:width]]
            line += new_line
    height = len(field)
    for i in range(1,5):
        for line in field[:height]:
            new_line = [((x - 1 + i) % 9) + 1 for x in line]
            field.append(new_line)
    width, height = len(field[0]), len(field)
    shortest = [[-1]*width for i in range(height)]
    shortest[height - 1][width - 1] = field[height - 1][width - 1]
    queue = [(width - 2, height - 1), (width - 1, height - 2)]
    while len(queue) > 0:
        p = queue[0]
        queue = queue[1:]
        min_s = -1
        for s in around(p):
            if is_in(s, field) and shortest[s[1]][s[0]] != -1:
                if shortest[s[1]][s[0]] < min_s or min_s == -1:
                    min_s = shortest[s[1]][s[0]]
        if min_s == -1:
            print(f"No path found at {p}")
        if shortest[p[1]][p[0]] == -1 or shortest[p[1]][p[0]] > min_s + field[p[1]][p[0]]:
            shortest[p[1]][p[0]] = min_s + field[p[1]][p[0]]
            for s in around(p):
                if is_in(s, field):
                    queue.append(s)
    print(shortest[0][0] - field[0][0])