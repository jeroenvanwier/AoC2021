def extend(field, bg):
    new_field = []
    new_field.append(bg*(len(field[0]) + 2))
    for line in field:
        new_field.append(bg + line + bg)
    new_field.append(bg*(len(field[0]) + 2))
    return new_field

def fieldstr_to_int(fstr):
    total = 0
    fstr = fstr[::-1]
    for i in range(len(fstr)):
        if fstr[i] == "#":
            total += 2**i
    return total

def evolve(field, rules, bg):
    field = extend(field, bg)
    bga = rules[fieldstr_to_int(bg*9)]
    new_field = [bga*len(field[0])]
    for y in range(1, len(field) - 1):
        new_field.append(bga)
        for x in range(1, len(field[0]) - 1):
            fstr = field[y-1][x - 1: x + 2] + field[y][x - 1: x + 2] + field[y+1][x - 1: x + 2]
            outp = rules[fieldstr_to_int(fstr)]
            new_field[y] += outp
        new_field[y] += bga
    new_field.append(bga*len(field[0]))
    return new_field, bga

if __name__=="__main__":
    f = open("input.txt")
    lines = f.read().split('\n')[:-1]
    rules = lines[0]
    field = lines[2:]
    field = extend(field, ".")
    bg = "."
    for i in range(50):
        field, bg = evolve(field, rules, bg)
    count = 0
    for line in field:
        for c in line:
            if c == "#":
                count += 1
    print(count)
    print("\n".join(field))