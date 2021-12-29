def add_seg(segments, seg, qty):
    if seg in segments:
        segments[seg] += qty
    else:
        segments[seg] = qty

if __name__=="__main__":
    f = open("input.txt")
    lines = f.read().split('\n')[:-1]
    string = lines[0]
    rules = {}
    segments = {}
    for line in lines[2:]:
        rule = line.split(" -> ")
        rules[rule[0]] = rule[1]
    for i in range(1,len(string)):
        seg = string[i - 1: i + 1]
        add_seg(segments, seg, 1)
    for i in range(40):
        new_segments = {}
        for seg in segments:
            if seg in rules:
                add_seg(new_segments, seg[0] + rules[seg], segments[seg])
                add_seg(new_segments, rules[seg] + seg[1], segments[seg])
            else:
                add_seg(new_segments, seg, segments[seg])
        segments = new_segments
    counts = {}
    for seg in segments:
        add_seg(counts, seg[0], segments[seg])
        add_seg(counts, seg[1], segments[seg])
    add_seg(counts, string[0], 1)
    add_seg(counts, string[-1], 1)
    most_common, least_common = 0, 0
    for letter in counts:
        if counts[letter] > most_common:
            most_common = counts[letter]
        if counts[letter] < least_common or least_common == 0:
            least_common = counts[letter]
    print((most_common - least_common) / 2)