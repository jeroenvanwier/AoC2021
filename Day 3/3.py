if __name__=="__main__":
    f = open("input.txt")
    l_o = f.read().split('\n')
    l_o = l_o[:-1]
    l_c = l_o[:]
    for current_bit in range(len(l_o[0])):
        if len(l_o) <= 1:
            break
        total = 0
        for line in l_o:
            total += int(line[current_bit])
        most_common = '0'
        if total >= len(l_o) / 2:
            most_common = '1'
        filtered = []
        for line in l_o:
            if line[current_bit] == most_common:
                filtered.append(line)
        l_o = filtered
    for current_bit in range(len(l_c[0])):
        if len(l_c) <= 1:
            break
        total = 0
        for line in l_c:
            total += int(line[current_bit])
        most_common = '1'
        if total >= len(l_c) / 2:
            most_common = '0'
        filtered = []
        for line in l_c:
            if line[current_bit] == most_common:
                filtered.append(line)
        l_c = filtered
    n_o, n_c = 0, 0
    b_o, b_c = l_o[0][::-1], l_c[0][::-1]
    for i in range(len(b_o)):
        n_o += int(b_o[i]) * 2**i
        n_c += int(b_c[i]) * 2**i
    print(f"{b_o}, {b_c}, {n_o*n_c}")
    