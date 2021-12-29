class Scanner:
    def __init__(self, points):
        self.points = []
        self.pos = (0,0,0)
        for point in points:
            p = point.split(',')
            self.points.append((int(p[0]), int(p[1]), int(p[2])))
    
    def rotateZ(self, num=1):
        (px, py, pz) = self.pos
        self.offset((-px, -py, -pz))
        new_points = [(y, -1 * x, z) for (x, y , z) in self.points]
        self.points = new_points
        self.offset((px, py, pz))
        if num == 1:
            return self
        else:
            return self.rotateZ(num=num-1)
    
    def rotateX(self, num=1):
        (px, py, pz) = self.pos
        self.offset((-px, -py, -pz))
        new_points = [(x, -1 * z , y) for (x, y , z) in self.points]
        self.points = new_points
        self.offset((px, py, pz))
        if num == 1:
            return self
        else:
            return self.rotateX(num=num-1)
            
    def rotateY(self, num=1):
        (px, py, pz) = self.pos
        self.offset((-px, -py, -pz))
        new_points = [(z, y , -1 * x) for (x, y , z) in self.points]
        self.points = new_points
        self.offset((px, py, pz))
        if num == 1:
            return self
        else:
            return self.rotateY(num=num-1)
    
    def reset(self):
        (px, py, pz) = self.pos
        self.offset((-px, -py, -pz))
    
    def offset(self, offset):
        (dx, dy, dz) = offset
        (px, py, pz) = self.pos
        self.pos = (px + dx, py + dy, pz + dz)
        new_points = [(x + dx, y + dy, z + dz) for (x, y , z) in self.points]
        self.points = new_points
        return self
    
    def match_points(self, other):
        other.reset()
        for candidate in other.points[:]:
            for reference in self.points:
                (cx, cy, cz) = candidate
                (rx, ry, rz) = reference
                other.offset((rx - cx, ry - cy, rz - cz))
                count = 0
                for point in other.points:
                    if point in self.points:
                        count += 1
                if count >= 12:
                    return True
                other.reset()
    
    def match(self, other):
        for _ in range(4):
            for _ in range(4):
                if self.match_points(other):
                    return True
                other.rotateZ()
            other.rotateY()
        other.rotateX()
        for _ in range(4):
            if self.match_points(other):
                return True
            other.rotateZ()
        other.rotateX(num=2)
        for _ in range(4):
            if self.match_points(other):
                return True
            other.rotateZ()
        other.rotateX()
        return False

def dst(p1, p2):
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    dz = abs(p1[2] - p2[2])
    return dx + dy + dz
    
def cmp(p):
    return 10**10 * p[0] + 10**5 * p[1] + p[2]

if __name__=="__main__":
    f = open("input.txt")
    lines = f.read().split('\n')[:-1]
    i = 0
    unmapped_scanners = []
    while i < len(lines):
        start = i
        while i < len(lines) and lines[i] != "":
            i += 1
        unmapped_scanners.append(Scanner(lines[start + 1:i]))
        i += 1
    scanners = [unmapped_scanners[0]]
    unmapped_scanners = unmapped_scanners[1:]
    last = len(unmapped_scanners) + 1
    while len(unmapped_scanners) < last:
        last = len(unmapped_scanners)
        for scanner in unmapped_scanners[:]:
            for scanref in scanners:
                if scanref.match(scanner):
                    print(f"Matched scanner! Only {len(unmapped_scanners)} left.")
                    unmapped_scanners.remove(scanner)
                    scanners.append(scanner)
                    break
    furthest = 0
    points = []
    for scanner in scanners:
        for scanner2 in scanners:
            d = dst(scanner.pos, scanner2.pos)
            if d > furthest:
                furthest = d
    print(furthest)