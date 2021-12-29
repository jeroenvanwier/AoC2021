def play(player, p1, p2, s1 = 0, s2 = 0):
    #print(f"{player}: {s1}@{p1}, {s2}@{p2}")
    sp = (0,0,0,1,3,6,7,6,3,1)
    if s1 >= 21:
        return 1, 0
    if s2 >= 21:
        return 0, 1
    if player == 0:
        su1, su2 = 0, 0
        for step in range(3,10):
            new_pos = (p1 + step) % 10
            new_score = s1 + new_pos + 1
            n1, n2 = play(1, new_pos, p2, s1=new_score, s2=s2)
            su1 += sp[step] * n1
            su2 += sp[step] * n2
        return su1, su2
    else:
        su1, su2 = 0, 0
        for step in range(3,10):
            new_pos = (p2 + step) % 10
            new_score = s2 + new_pos + 1
            n1, n2 = play(0, p1, new_pos, s1=s1, s2=new_score)
            su1 += sp[step] * n1
            su2 += sp[step] * n2
        return su1, su2

if __name__=="__main__":
    f = open("input.txt")
    lines = f.read().split('\n')[:-1]
    players = []
    for line in lines:
        line = line.split()
        players.append(int(line[4]))
    w1, w2 = play(0, players[0] - 1, players[1] - 1)
    print((w1, w2))
    