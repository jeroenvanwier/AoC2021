def is_large(cave):
    return cave[0] not in "abcdefghijklmnopqrstuvwxyz"

def is_connected(connections, cave, last_cave):
    if cave == last_cave:
        return False
    for con in connections:
        if cave in con and last_cave in con:
            return True
    return False

if __name__=="__main__":
    f = open("input.txt")
    lines = f.read().split('\n')[:-1]
    connections = [line.split('-') for line in lines]
    caves = ["start", "end"]
    for connection in connections:
        if connection[0] not in caves:
            caves.append(connection[0])
        if connection[1] not in caves:
            caves.append(connection[1])
    finished_paths = 0
    paths = [(False, ["start"])]
    while len(paths) > 0:
        path = paths[0]
        paths = paths[1:]
        if path[1][-1] == "end":
            finished_paths += 1
        else:
            last_cave = path[1][-1]
            for cave in caves:
                if is_connected(connections, cave, last_cave):
                    if is_large(cave) or cave not in path[1]:
                        paths.append((path[0], path[1] + [cave]))
                    elif cave != "start" and not path[0]:
                        paths.append((True, path[1] + [cave]))
                        #print((True, path[1] + [cave]))
    print(finished_paths)