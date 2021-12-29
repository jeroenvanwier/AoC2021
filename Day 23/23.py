class Board:
    dest = {'A':3, 'B':5, 'C':7, 'D':9}
    
    def __init__(self, desc, data=None):
        #############
        #123456789  #0
        ###3#5#7#9###1
          #3#5#7#9#  2
          #3#5#7#9#  3
          #3#5#7#9#  4
          #########
        #  
        if data:
            self.field = data
            return
        self.field = desc[1:-1]
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        field = self.field
        fstr = '\n'.join(field)
        return f"#############\n{fstr}\n  #########"

    def __eq__(self, other):
        f = "".join(self.field)
        g = "".join(other.field)
        return f == g
    
    def __ne__(self, other):
        return not self == other
    
    def idx(self):
        total = 0
        i = 0
        value = {".": 0, "A": 1, "B": 2, "C": 3, "D": 4}
        for x in range(1,12):
            for y in range(5):
                if is_valid((x, y)):
                    total += value[self.at((x, y))] * 5**i
                    i += 1
        return total
    
    def inq(self, l):
        for i in range(len(l) - 1, -1, -1):
            if l[i][1] == self:
                return True
        return False
    
    def clone(self):
        new_field = [row[:] for row in self.field]
        return Board("", data=new_field)
    
    def move(self, x1, y1, x2, y2):
        self.field[y2] = self.field[y2][:x2] + self.field[y1][x1] + self.field[y2][x2 + 1:]
        self.field[y1] = self.field[y1][:x1] + '.' + self.field[y1][x1 + 1:]
        return self

    def is_empty(self, p):
        return self.field[p[1]][p[0]] == "."
    
    def at(self, p):
        return self.field[p[1]][p[0]]
    
    def get_moves(self, p):
        f = self.field
        ps = []
        q = [p]
        des_x = Board.dest[f[p[1]][p[0]]]
        added = True
        while added:
            added = False
            for v in q:
                for z in around(v):
                    if self.is_empty(z) and z not in q:
                        q.append(z)
                        added = True
        q = [v for v in q if v not in [(3,0), (5,0), (7,0), (9,0), p]]
        if p[1] == 0:
            new_q = []
            for v in q:
                if v[1] > 0 and v[0] == des_x:
                    if v[1] == 4:
                        new_q.append(v)
                    else:
                        contains_other = False
                        for i in range(v[1] + 1, 5):
                            if self.at((v[0], i)) != self.at(p):
                                contains_other = True
                        if not contains_other:
                            new_q.append(v)
            return new_q
        else:
            new_q = []
            for v in q:
                if v[1] == 0:
                    if p[0] != des_x:
                        new_q.append(v)
                    else:
                        for i in range(p[1] + 1, 5):
                            if self.at((p[0], i)) != self.at(p):
                                new_q.append(v)
                                break
            return new_q
    
    def get_neigbours(self):
        f = self.field
        moves = []
        cost = {'A':1, 'B':10, 'C':100, 'D':1000}
        dest = Board.dest
        for x in range(1,12):
            for y in range(5):
                if not is_valid((x,y)) or f[y][x] == ".":
                    continue
                if f[y][x] in ["#", " "]:
                    print((x,y))
                    print(self)
                for (x2, y2) in self.get_moves((x, y)):
                    moves.append((cost[f[y][x]] * dst((x, y), (x2, y2)), self.clone().move(x,y,x2,y2)))
        return moves

def dst(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def around(pos):
    x, y = pos[0], pos[1]
    return [p for p in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if is_valid(p)]

def first(pair):
    return pair[0]

def is_valid(pos):
    (x, y) = pos
    if y == 0:
        return x >= 1 and x <= 11
    if y >= 1 and y <= 4:
        return x >= 3 and x <= 9 and x % 2 == 1
    return False

def insort_q(a, x, lo=0, hi=None): #adapted from bisect module
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x[0] < a[mid][0]:
            hi = mid
        else:
            lo = mid+1
    a.insert(lo, x)

def insort(a, x, lo=0, hi=None): #adapted from bisect module
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid+1
    a.insert(lo, x)

def sortsearch(a, x, lo=0, hi=None): #adapted from bisect module
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x[0] < a[mid][0]:
            hi = mid
        elif x[0] == a[mid][0]:
            return a[mid]
        else:
            lo = mid+1
    return None

if __name__=="__main__":
    f = open("input.txt")
    lines = f.read().split('\n')[:-1]
    board = Board(lines)
    queue = [(0, board)]
    done = []
    target = Board("", data=["#...........#","###A#B#C#D###","  #A#B#C#D#  ","  #A#B#C#D#  ","  #A#B#C#D#  "])
    last = 0
    target_score = target.idx()
    while not sortsearch(done, (target_score,)) and len(queue) > 0:
        q = queue[0]
        queue = queue[1:]
        score = q[1].idx()
        if sortsearch(done, (score,)):
            continue
        if q[0] > last:
            print(f"Current score: {q[0]}, Q:{len(queue)}, D:{len(done)}")
            last = q[0]
            #new_queue = []
            #for v in queue:
            #    if not v[1].inq(new_queue):
            #        new_queue.append(v)
            #queue = new_queue
        insort_q(done, (score, q[0], q[1]))
        moves = q[1].get_neigbours()
        new_qs = [(m[0] + q[0], m[1]) for m in moves]
        for v in new_qs:
            insort_q(queue, v)
    print(sortsearch(done, (target_score,))[1])