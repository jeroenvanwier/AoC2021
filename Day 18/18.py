import math

class Num:
    LIT = 0
    NODE = 1
    
    def __init__(self, desc="", left=None, right=None, parent=None):
        self.parent = parent
        if desc == "" and (left == None or right == None):
            print("Invalid num")
            return
        if desc == "":
            self.t = Num.NODE
            self.left = left
            self.right = right
            left.parent = self
            right.parent = self
            return
        if desc[0] == "[" and desc[-1] == "]":
            self.t = Num.NODE
            desc = desc[1:-1]
            i = 0
            if desc[0] != "[":
                i = 0
                while desc[i] != ",":
                    i += 1
            else:
                level = 1
                i += 1
                while level > 0:
                    if desc[i] == "[":
                        level += 1
                    elif desc[i] == "]":
                        level -= 1
                    i += 1
            self.left = Num(desc=desc[:i], parent=self)
            self.right = Num(desc=desc[i+1:], parent=self)
        else:
            self.t = Num.LIT
            self.value = int(desc)
        
    def __add__(self, other):
        num = Num(left=self, right=other, parent=self.parent)
        num.reduce()
        return num
    
    def __str__(self):
        if self.t == Num.LIT:
            return str(self.value)
        else:
            return f"[{self.left},{self.right}]"
    
    def find_level(self, level=4):
        if self.t == Num.LIT:
            return None
        if level == 0:
            return self
        l = self.left.find_level(level=level-1)
        if l:
            return l
        else:
            return self.right.find_level(level=level-1)
    
    def find_split(self):
        if self.t == Num.LIT and self.value >= 10:
            return self
        elif self.t == Num.NODE:
            target = self.left.find_split()
            if target:
                return target
            return self.right.find_split()
    
    def explode(self):
        if self.t != Num.NODE or self.right.t != Num.LIT or self.left.t != Num.LIT:
            print(f"Illegal explode {self}")
        current = self
        while current.parent and current.parent.left == current:
            current = current.parent
        if current.parent:
            current = current.parent.left
            while current.t == Num.NODE:
                current = current.right
            current.value += self.left.value
        current = self
        while current.parent and current.parent.right == current:
            current = current.parent
        if current.parent:
            current = current.parent.right
            while current.t == Num.NODE:
                current = current.left
            current.value += self.right.value
        self.t = Num.LIT
        self.value = 0
        del self.left
        del self.right
        
    
    def split(self):
        if self.t != Num.LIT or self.value < 10:
            return self
        half = self.value / 2
        self.left = Num(desc=str(int(math.floor(half))), parent=self)
        self.right = Num(desc=str(int(math.ceil(half))), parent=self)
        self.t = Num.NODE
        del self.value
    
    def clone(self):
        return Num(desc=str(self))
    
    def reduce(self):
        if self.t == Num.LIT:
            return
        target = self.find_level()
        if target:
            target.explode()
            self.reduce()
            return
        target = self.find_split()
        if target:
            target.split()
            self.reduce()
    
    def magnitude(self):
        if self.t == Num.LIT:
            return self.value
        else:
            return 3 * self.left.magnitude() + 2 * self.right.magnitude()

if __name__=="__main__":
    f = open("input.txt")
    lines = f.read().split('\n')[:-1]
    nums = [Num(desc=line) for line in lines]
    highest = 0
    for num1 in nums:
        for num2 in nums:
            if num1 == num2:
                continue
            mag = (num1.clone() + num2.clone()).magnitude()
            mag2 = (num2.clone() + num1.clone()).magnitude()
            highest = max([mag, mag2, highest])
    print(highest)
