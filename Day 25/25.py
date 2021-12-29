if __name__=="__main__":
    f = open("input_small.txt")
    lines = f.read().split('\n')[:-1]
    field = []
    for line in lines:
        field.append([])
        for c in line:
            field[-1].append(c)
    i = 0
    while True:
        field_old = []
        for line in field:
            field_old.append([])
            for c in line:
                field_old[-1].append(c)
        moved = False
        for y in range(len(field)):
            for x in range(len(field[0])):
                if field_old[y][x] == ">" and field_old[y][(x + 1) % len(field[0])] == ".":
                    moved = True
                    field[y][(x+1)%len(field[0])] = ">"
                    field[y][x] = "."
        field_old = []
        for line in field:
            field_old.append([])
            for c in line:
                field_old[-1].append(c)
        for y in range(len(field)):
            for x in range(len(field[0])):
                if field_old[y][x] == "v" and field_old[(y+1)%len(field)][x] == ".":
                    moved = True
                    field[(y+1)%len(field)][x] = "v"
                    field[y][x] = "."
        i += 1
        if not moved:
            break
    print(i)