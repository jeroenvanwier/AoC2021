def find_matching(char):
    if char == "}":
        return "{"
    elif char == ")":
        return "("
    elif char == "]":
        return "["
    elif char == ">":
        return "<"
    else:
        print(f"Whoops: {char}")
        return None

def char_value(char):
    if char == "}":
        return 1197
    elif char == ")":
        return 3
    elif char == "]":
        return 57
    elif char == ">":
        return 25137
    else:
        print(f"Whoopsie: {char}")
        return 0

def char_complete_value(char):
    if char == "{":
        return 3
    elif char == "(":
        return 1
    elif char == "[":
        return 2
    elif char == "<":
        return 4
    else:
        print(f"Whoopsies: {char}")
        return 0

def complete_value(seq):
    total = 0
    for char in seq:
        total *= 5
        total += char_complete_value(char)
    return total

if __name__=="__main__":
    f = open("input.txt")
    lines = f.read().split('\n')[:-1]
    errors = []
    completes = []
    opening = "<({["
    for line in lines:
        stack = []
        corrupt = False
        for char in line:
            if char in opening:
                stack.append(char)
            else:
                if stack[-1] == find_matching(char):
                    stack = stack[:-1]
                else:
                    errors.append(char)
                    corrupt = True
                    break
        if not corrupt:
            completes.append(stack[::-1])
    errorvs = [char_value(x) for x in errors]
    completevs = [complete_value(seq) for seq in completes]
    completevs.sort()
    print(completevs[int(len(completevs) / 2)])