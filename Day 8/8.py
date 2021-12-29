def sort_pattern(pat):
    full = "abcdefg"
    out = ""
    for l in full:
        if l in pat:
            out += l
    return out

if __name__=="__main__":
    f = open("input.txt")
    lines_raw = f.read().split('\n')[:-1]
    lines_raw = [line.split(" | ") for line in lines_raw]
    lines = [(line[0].split(), line[1].split()) for line in lines_raw]
    total = 0
    for line in lines:
        pattern = [None]*10
        top_one = None # top segment of 1
        for x in line[0]:
            if len(x) == 2:
                pattern[1] = x
            elif len(x) == 3:
                pattern[7] = x
            elif len(x) == 4:
                pattern[4] = x
            elif len(x) == 7:
                pattern[8] = x
        for pat in line[0]:
            if len(pat) == 6 and (pattern[1][0] not in pat or pattern[1][1] not in pat):
                pattern[6] = pat
                if pattern[1][0] not in pat:
                    top_one = pattern[1][0]
                else:
                    top_one = pattern[1][1]
        for pat in line[0]:
            if len(pat) == 5:
                if pattern[1][0] in pat and pattern[1][1] in pat:
                    pattern[3] = pat
                elif top_one in pat:
                    pattern[2] = pat
                else:
                    pattern[5] = pat
        in3butnot7 = []
        for l in pattern[3]:
            if l not in pattern[7]:
                in3butnot7.append(l)
        for pat in line[0]:
            if len(pat) == 6 and pat != pattern[6]:
                if in3butnot7[0] in pat and in3butnot7[1] in pat:
                    pattern[9] = pat
                else:
                    pattern[0] = pat
        output = []
        pattern = [sort_pattern(p) for p in pattern]
        for out in line[1]:
            output.append(pattern.index(sort_pattern(out)))
        total += 1000*output[0] + 100*output[1] + 10*output[2] + output[3]
    print(total)
