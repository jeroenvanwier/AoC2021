def bin_to_int(binnr):
    binnr = binnr[::-1]
    total = 0
    for i in range(len(binnr)):
        total += int(binnr[i]) * 2**i
    return total

def hex_to_bin(hexnr):
    hexmap = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A":"1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}
    tot = ""
    for c in hexnr:
        tot += hexmap[c]
    return tot

class Packet:
    def __init__(self, data, isbin = False):
        binstr = data
        if not isbin:
            binstr = hex_to_bin(data)
        self.version = bin_to_int(binstr[:3])
        self.typeid = bin_to_int(binstr[3:6])
        if self.typeid == 4:
            self.load_payload(binstr[6:])
        else:
            self.parse_packets(binstr[6:])
    
    def load_payload(self, binstr):
        packet = binstr[:5]
        payloadstr = packet[1:]
        binstr = binstr[5:]
        while packet[0] == "1":
            if len(binstr) < 5:
                print("Payload error")
                break
            packet = binstr[:5]
            payloadstr += packet[1:]
            binstr = binstr[5:]
        self.payload = bin_to_int(payloadstr)
    
    def first_packet_length(binstr):
        tid = bin_to_int(binstr[3:6])
        if tid == 4:
            num_packs = 1
            while binstr[6 + (num_packs - 1) * 5] != "0":
                num_packs += 1
            return 6 + 5 * num_packs
        else:
            if binstr[6] == "0":
                return 6 + 1 + 15 + bin_to_int(binstr[7:22])
            else:
                total = 6 + 1 + 11
                num_packs = bin_to_int(binstr[7:18])
                for i in range(num_packs):
                    total += Packet.first_packet_length(binstr[total:])
                return total
    
    def parse_packets(self, binstr):
        self.packets = []
        if binstr[0] == "0":
            packet_length = bin_to_int(binstr[1:16])
            parsestr = binstr[16:16+packet_length]
            while len(parsestr) > 0:
                next_length = Packet.first_packet_length(parsestr)
                self.packets.append(Packet(parsestr[:next_length], isbin=True))
                parsestr = parsestr[next_length:]
        else:
            num_packs = bin_to_int(binstr[1:12])
            parsestr = binstr[12:]
            for i in range(num_packs):
                next_length = Packet.first_packet_length(parsestr)
                self.packets.append(Packet(parsestr[:next_length], isbin=True))
                parsestr = parsestr[next_length:]
    
    def evaluate(self):
        typeid = self.typeid
        if typeid == 4:
            return self.payload
        elif typeid == 0:
            return sum([p.evaluate() for p in self.packets])
        elif typeid == 1:
            product = 1
            for p in self.packets:
                product *= p.evaluate()
            return product
        elif typeid == 2:
            return min([p.evaluate() for p in self.packets])
        elif typeid == 3:
            return max([p.evaluate() for p in self.packets])
        elif typeid == 5:
            if self.packets[0].evaluate() > self.packets[1].evaluate():
                return 1 
            else:
                return 0
        elif typeid == 6:
            if self.packets[0].evaluate() < self.packets[1].evaluate():
                return 1 
            else:
                return 0
        elif typeid == 7:
            if self.packets[0].evaluate() == self.packets[1].evaluate():
                return 1 
            else:
                return 0

def get_version_sum(packet):
    total = packet.version
    if packet.typeid != 4:
        for pack in packet.packets:
            total += get_version_sum(pack)
    return total

if __name__=="__main__":
    f = open("input.txt")
    lines = f.read().split('\n')[:-1]
    packet = Packet(lines[0])
    print(packet.evaluate())
    