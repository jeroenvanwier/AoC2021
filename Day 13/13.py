if __name__=="__main__":
    f = open("input.txt")
    lines = f.read().split('\n')[:-1]
    points = []
    folds = []
    for line in lines:
        if ',' in line:
            coords = line.split(',')
            points.append((int(coords[0]), int(coords[1])))
        elif '=' in line:
            folds.append(line.split()[2].split("="))
            folds[-1][1] = int(folds[-1][1])
    for fold in folds:
        new_points = []
        if fold[0] == "x":
            for point in points:
                p2a = point
                if point[0] > fold[1]:
                    p2a = (2 * fold[1] - point[0], point[1])
                if p2a not in new_points:
                    new_points.append(p2a)
        if fold[0] == "y":
            for point in points:
                p2a = point
                if point[1] > fold[1]:
                    p2a = (point[0], 2 * fold[1] - point[1])
                if p2a not in new_points:
                    new_points.append(p2a)
        points = new_points
    width, height = 0, 0
    for point in points:
        if point[0] > width:
            width = point[0]
        if point[1] > height:
            height = point[1]
    for y in range(height + 1):
        line = ""
        for x in range(width + 1):
            if (x, y) in points:
                line += "#"
            else:
                line += " "
        print(line)