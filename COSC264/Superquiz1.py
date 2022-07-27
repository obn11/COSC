def composepacket (version, hdrlen, tosdscp, totallength, identification, flags, fragmentoffset, timetolive, protocoltype, headerchecksum, sourceaddress, destinationaddress):
    if version != 4 or version < 0:
        return 1
    if hdrlen > 15 or hdrlen < 0:
        return 2
    if tosdscp > 63 or tosdscp < 0:
        return 3
    if totallength > 65535 or totallength < 0:
        return 4
    if identification > 65535 or identification < 0:
        return 5
    if flags > 7 or flags < 0:
        return 6
    if fragmentoffset > 8191 or fragmentoffset < 0:
        return 7
    if timetolive > 255 or timetolive < 0:
        return 8
    if protocoltype > 255 or protocoltype < 0:
        return 9
    if headerchecksum > 65535 or headerchecksum < 0:
        return 10
    if sourceaddress > 4294967295 or sourceaddress < 0:
        return 11
    if destinationaddress > 4294967295 or destinationaddress < 0:
        return 12
    x = bytearray()
    b = (version << 4) | hdrlen
    x.append(b)
    x.append((tosdscp << 2))
    listy = [totallength, identification, flags, fragmentoffset, timetolive, protocoltype, headerchecksum, sourceaddress, destinationaddress]
    x = cbytes2(listy[0], x)
    x = cbytes2(listy[1], x)
    x = cbytesF(listy[2], listy[3], x)
    x.append(listy[4])
    x.append(listy[5])
    x = cbytes2(listy[6], x)
    x = cbytes4(listy[7], x)
    x = cbytes4(listy[8], x)
    return x
    
def cbytes2(i, x):
    a = (i & 0xFF00) >> 8
    b = i & 0x00FF
    x.append(a)
    x.append(b)
    return x

def cbytesF(i, j, x):
    a = (i << 5) | (j >> 8)
    b = j & 0x0FF
    x.append(a)
    x.append(b)
    return x

def cbytes4(i, x):
    a = (i & 0xFF000000) >> 24
    b = (i & 0x00FF0000) >> 16
    c = (i & 0x0000FF00) >> 8
    d = i & 0x000000FF
    x.append(a)
    x.append(b)
    x.append(c)
    x.append(d)
    return x

def basicpacketcheck (pkt):
    if len(pkt) < 20:
        return 1
    
    if pkt[0] >> 4 != 4:
        return 2
    
    x = sum(list10(pkt))
    while x > 0xFFFF:
        a = x & 0xFFFF
        b = x >> 16
        x = a + b
    if x != 0xFFFF:
        return 3
    
    if ((pkt[3] << 8) | pkt[4]) // 256 != len(pkt):
        return 4
    
    return True
    
def list10(pkt):
    listy = []
    i = 0
    while i < 20:
        listy.append((pkt[i] << 8) | pkt[i+1])
        i += 2
    return listy

def destaddress (pkt):
    a = (pkt[16] << 24) | (pkt[17]) << 16 | (pkt[18]) << 8 | pkt[19]
    dd = '{}.{}.{}.{}'.format(pkt[16], pkt[17], pkt[18], pkt[19])
    return a, dd

def payload (pkt):
    hdl = pkt[0] & 0x0F
    i = hdl * 4
    x = bytearray()
    while i < len(pkt):
        x.append(pkt[i])
        i += 1
    return x

def revisedcompose (hdrlen, tosdscp, identification, flags, fragmentoffset, timetolive, protocoltype, sourceaddress, destinationaddress, payload):
    version = 4
    if hdrlen > 15 or hdrlen < 5:
        return 2
    if tosdscp > 63 or tosdscp < 0:
        return 3
    totallength = ((hdrlen * 4) + len(payload))
    if identification > 65535 or identification < 0:
        return 5
    if flags > 7 or flags < 0:
        return 6
    if fragmentoffset > 8191 or fragmentoffset < 0:
        return 7
    if timetolive > 255 or timetolive < 0:
        return 8
    if protocoltype > 255 or protocoltype < 0:
        return 9
    if sourceaddress > 4294967295 or sourceaddress < 0:
        return 11
    if destinationaddress > 4294967295 or destinationaddress < 0:
        return 12
    x = bytearray()
    b = (version << 4) | hdrlen
    x.append(b)
    x.append((tosdscp << 2))
    headerchecksum = 0x0000
    listy = [totallength, identification, flags, fragmentoffset, timetolive, protocoltype, headerchecksum, sourceaddress, destinationaddress]
    x = cbytes2(listy[0], x)
    x = cbytes2(listy[1], x)
    x = cbytesF(listy[2], listy[3], x)
    x.append(listy[4])
    x.append(listy[5])
    x = cbytes2(listy[6], x)
    x = cbytes4(listy[7], x)
    x = cbytes4(listy[8], x)
    if hdrlen > 5:
        for j in range(4):
            x.append(0x00)
    X = sum(listN(x))
    while X > 0xFFFF:
        a = X & 0xFFFF
        b = X >> 16
        X = a + b
    X = ~X
    cbytes2m(X, x)
    for i in payload:
        x.append(i)        
    return x

def cbytes2m(i, x):
    a = (i & 0xFF00) >> 8
    b = i & 0x00FF
    x[10] = a
    x[11] = b
    return x

def listN(pkt):
    listy = []
    i = 0
    while i < len(pkt):
        listy.append((pkt[i] << 8) | pkt[i+1])
        i += 2
    return listy

print(revisedcompose (6, 24, 4711, 0, 22, 64, 0x06, 0x22334455, 0x66778899, bytearray([0x10, 0x11, 0x12, 0x13, 0x14, 0x15])))

