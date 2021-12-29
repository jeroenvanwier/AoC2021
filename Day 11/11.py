def around(pos): # Adapted from day 9
    x, y = pos[0], pos[1]
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)]

def flash(octos, pos):
    if octos[pos[1]][pos[0]] <= 9:
        return
    octos[pos[1]][pos[0]] = -1000
    for p in around(pos):
        if not is_in(p, octos):
            continue
        octos[p[1]][p[0]] += 1
        if octos[p[1]][p[0]] > 9:
            flash(octos, p)
            
def is_in(pos, hmap): #Stolen from day 9
    return pos[0] >= 0 and pos[0] < len(hmap[0]) and pos[1] >= 0 and pos[1] < len(hmap)

if __name__=="__main__":
    f = open("input.txt")
    lines = f.read().split('\n')[:-1]
    octos = []
    for line in lines:
        octos.append([int(x) for x in line])
    total_flashes = 0
    for step in range(10000):
        did_all_flash = True
        for y in range(len(octos)):
            for x in range(len(octos[0])):
                octos[y][x] += 1
        for y in range(len(octos)):
            for x in range(len(octos[0])):
                flash(octos, (x, y))
        for y in range(len(octos)):
            for x in range(len(octos[0])):
                if octos[y][x] < 0:
                    octos[y][x] = 0
                    total_flashes += 1
                else:
                    did_all_flash = False
        if did_all_flash:
            print(f"All flashed on step {step + 1}")
            quit()
    print(total_flashes)