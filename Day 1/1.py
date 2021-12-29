if __name__=="__main__":
    f = open("i1.txt")
    buffer = []
    total = 0
    for x in f:
        buffer.append(int(x))
        if len(buffer) < 4:
            continue
        if buffer[0] < buffer[3]:
            total += 1
        buffer = buffer[1:]
    print(total)
    