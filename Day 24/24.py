import math

class Machine:
    def __init__(self, x, y, z, w, i):
        self.state = {}
        self.state["x"] = x
        self.state["y"] = y
        self.state["z"] = z
        self.state["w"] = w
        self.i = i
    
    def ins(self, ins, inputs):
        ins = ins.split()
        if ins[0] == "inp":
            self.state[ins[1]] = inputs[self.i]
            self.i += 1
        else:
            if ins[2] in ["x", "y", "z", "w"]:
                self.state[ins[1]] = Machine.calculate(ins[0], self.state[ins[1]], self.state[ins[2]])
            else:
                self.state[ins[1]] = Machine.calculate(ins[0], self.state[ins[1]], int(ins[2]))
    
    def calculate(ins, a, b):
        if ins == "mul":
            return a * b
        elif ins == "add":
            return a + b
        elif ins == "div":
            r = a / b
            if r > 0:
                r = math.floor(r)
            else:
                r = math.ceil(r)
            return int(r)
        elif ins == "mod":
            return a % b
        elif ins == "eql":
            if a == b:
                return 1
            else:
                return 0
        else:
            print(f"Illegal instruction: {ins} {a} {b}")
            return 0

def is_in(e, l):
    for i in l:
        if i[1] == e:
            return True
    return False

if __name__=="__main__":
    f = open("input.txt")
    lines = f.read().split('\n')[:-1]
    blocks = []
    for line in lines:
        if line[:3] == "inp":
            blocks.append([])
        blocks[-1].append(line)
    z_states = {14: [(0,0,0)]}
    for i in range(14):
        z_states[i] = []
    for i in range(13, 0, -1):
        for z in range(10000):
            for v in range(1, 10):
                values = [0]*14
                values[i] = v
                machine = Machine(0,0,z,0,i)
                for line in blocks[i]:
                    machine.ins(line, values)
                if is_in(machine.state["z"], z_states[i+1]) and not is_in(z, z_states[i]):
                    z_states[i].append((v, z, machine.state["z"]))
        print(i)
    for v in range(1, 10):
        values = [0]*14
        values[0] = v
        machine = Machine(0,0,0,0,0)
        for line in blocks[0]:
            machine.ins(line, values)
        if is_in(machine.state["z"], z_states[1]) and not is_in(0, z_states[0]):
            z_states[0].append((v, 0, machine.state["z"]))
    inp = ""
    cur_state = 0
    for i in range(14):
        for state in z_states[i]:
            if state[1] == cur_state:
                inp += str(state[0])
                cur_state = state[2]
                break
    print(inp)