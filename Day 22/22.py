class Cuboid:
    def __init__(self, coords):
        self.x1 = coords[0][0]
        self.x2 = coords[0][1]
        self.y1 = coords[1][0]
        self.y2 = coords[1][1]
        self.z1 = coords[2][0]
        self.z2 = coords[2][1]
    
    def get_intersect(self, other):
        x1 = max(self.x1, other.x1)
        y1 = max(self.y1, other.y1)
        z1 = max(self.z1, other.z1)
        x2 = min(self.x2, other.x2)
        y2 = min(self.y2, other.y2)
        z2 = min(self.z2, other.z2)
        if x1 <= x2 and y1 <= y2 and z1 <= z2:
            return Cuboid(((x1,x2),(y1,y2),(z1, z2)))
        else:
            return None
    
    def splitoff(self, other):
        cuboids = []
        other = self.get_intersect(other)
        if not other:
            return [self]
        if self.x1 < other.x1:
            cuboids.append(Cuboid(((self.x1, other.x1 - 1), (self.y1, self.y2), (self.z1, self.z2))))
        if self.x2 > other.x2:
            cuboids.append(Cuboid(((other.x2 + 1, self.x2), (self.y1, self.y2), (self.z1, self.z2))))
        if self.y1 < other.y1:
            cuboids.append(Cuboid(((other.x1, other.x2), (self.y1, other.y1 - 1), (self.z1, self.z2))))
        if self.y2 > other.y2:
            cuboids.append(Cuboid(((other.x1, other.x2), (other.y2 + 1, self.y2), (self.z1, self.z2))))
        if self.z1 < other.z1:
            cuboids.append(Cuboid(((other.x1, other.x2), (other.y1, other.y2), (self.z1, other.z1 - 1))))
        if self.z2 > other.z2:
            cuboids.append(Cuboid(((other.x1, other.x2), (other.y1, other.y2), (other.z2 + 1, self.z2))))
        return cuboids

    
    def addto(self, cubes):
        for cube in cubes[:]:
            inter = self.get_intersect(cube)
            if inter:
                for c in self.splitoff(inter):
                    c.addto(cubes)
                return
        cubes.append(self)
    
    def removefrom(self, cubes):
        for cube in cubes[:]:
            inter = self.get_intersect(cube)
            if inter:
                cubes.remove(cube)
                for c in cube.splitoff(inter):
                    cubes.append(c)
    
    def size(self):
        return (self.x2 - self.x1 + 1) * (self.y2 - self.y1 + 1) * (self.z2 - self.z1 + 1)
    
    def __str__(self):
        return f"({self.x1}-{self.x2}, {self.y1}-{self.y2}, {self.z1}-{self.z2})"

    def __repr__(self):
        return str(self)
    
    def issame(self, other):
        return self.x1 == other.x1 and self.x2 == other.x2 and self.z1 == other.z1 and self.z2 == other.z2 and self.y1 == other.y1 and self.y2 == other.y2

def parse_instruction(istr):
    i = istr.split()
    c = i[1].split(',')
    d = [v[2:].split('..') for v in c]
    e = [(int(v[0]), int(v[1])) for v in d]
    cu = Cuboid(e)
    return (i[0], cu)

if __name__=="__main__":
    f = open("input.txt")
    lines = f.read().split('\n')[:-1]
    instructions = [parse_instruction(line) for line in lines]
    cubes = []
    orig_cubes = []
    for i in instructions:
        if i[0] == "on":
            i[1].addto(cubes)
            orig_cubes.append(i[1])
        else:
            i[1].removefrom(cubes)
    print(sum([c.size() for c in cubes]))