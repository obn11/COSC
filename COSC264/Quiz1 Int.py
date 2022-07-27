def convert (x, base):
    if type(x) != int:
        return -1
    if type(base) != int:
        return -1
    if x < 0:
        return -3
    if base < 2:
        return -4
    power = 0
    done = False
    while not done:
        if base**power < x:
            power += 1
        else:
            done = True
    lst = []
    while power != -1:
        coef = x // (base**power)
        lst.append(coef)
        x -= (coef * (base**power))
        power -= 1
    if lst[0] == 0:
        lst.remove(0)
    return lst

def hexstring(x):
    if type(x) != int:
        return -1
    if x < 0:
        return -2
    i = 0
    lst = convert(x, 16)
    out = '0x'
    while i < len(lst):
        if lst[i] < 10:
            out += str(lst[i])
        else:
            if lst[i] == 10:
                out += 'A'
            elif lst[i] == 11:
                out += 'B'
            elif lst[i] == 12:
                out += 'C'  
            elif lst[i] == 13:
                out += 'D'   
            elif lst[i] == 14:
                out += 'E'
            elif lst[i] == 15:
                out += 'F'
        i += 1
    return out
                
def transmission_delay (packetLength_bytes, rate_mbps):
    return (packetLength_bytes * 8) / (rate_mbps*10**6)

def total_time (cableLength_KM, packetLength_b):
    tdel = transmission_delay((packetLength_b / 8), 10000)
    pdel = cableLength_KM/200000
    delay_s = tdel + pdel
    ping = delay_s * 1000
    return ping

def queueing_delay (rate_bps, numPackets, packetLength_b):
    return (numPackets * packetLength_b) / rate_bps

def average_trials (P):
    return 1 / (1-P)

def per_from_ber (bitErrorProb, packetLen_b):
    return 1-((1-bitErrorProb)**packetLen_b)

def avg_trials_from_ber (bit_error_probability, packetLength_b):
    rate = per_from_ber(bit_error_probability, packetLength_b)
    avg =  average_trials(rate)
    return avg

def decodedate (x):
    m = (x & 0xF0000000) >> 28
    m += 1        
    d = (x & 0x0F800000) >> 23
    d += 1
    y = (x & 0x007FFFFF)
    out = "{}.{}.{}".format(d, m, y)
    return out

def encodedate (day, month, year):
    x = 0x00000000
    if month > 12 or month < 1:
        return -1
    m = (month - 1) << 28
    x = x | m
    if day > 31 or day < 1:
            return -1    
    d = (day - 1) << 23
    x = x | d
    if year > ((2**23) -1) or year < 0:
            return -1    
    y = (year)
    x = x | y
    return x

print(encodedate(5,5,2017))


