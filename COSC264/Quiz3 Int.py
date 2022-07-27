def connection_setup_delay (cableLength_km, speedOfLight_kms, dataRate_bps, messageLength_b, processingTimes_s):
    Prop = messageLength_b / dataRate_bps
    Trans = cableLength_km / speedOfLight_kms
    total = 4 * Prop + 4 * Trans + 4 * processingTimes_s
    return total 


def message_delay (connSetupTime_s, cableLength_km, speedOfLight_kms, messageLength_b, dataRate_bps):
    Prop = messageLength_b / dataRate_bps
    Trans = cableLength_km / speedOfLight_kms
    total = connSetupTime_s + Prop + 2 * Trans
    return total

import math
def total_number_bits (maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b, messageLength_b):
    S = maxUserDataBitsPerPacket_b
    O = overheadBitsPerPacket_b
    M = messageLength_b
    
    if M % S == 0:
        packets = M/S
        
    else:
        packets = M//S + 1
    total = packets * O + M
    return total

def packet_transfer_time (linkLength_km, speedOfLight_kms, processingDelay_s, dataRate_bps, maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b):
    L = linkLength_km
    C = speedOfLight_kms
    P = processingDelay_s
    R = dataRate_bps
    S = maxUserDataBitsPerPacket_b
    O = overheadBitsPerPacket_b
    PrD = (S + O) / R
    TrD = L / C
    total = PrD + TrD + P + PrD + TrD + P
    return total
    
def total_transfer_time (linkLength_km, speedOfLight_kms, processingDelay_s, dataRate_bps, maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b, messageLength_b):
    l = linkLength_km
    c = speedOfLight_kms
    p = processingDelay_s
    r = dataRate_bps
    s = maxUserDataBitsPerPacket_b
    o = overheadBitsPerPacket_b
    m = messageLength_b
    pan = m/s
    pas = s + o
    prd = pas / r
    trd = l / c
    total = (prd * (pan+1)) + (trd*2) + (2*p)
    return total

print ("{:.5f}".format(total_transfer_time(10000, 200000, 0.001, 1000000, 1000, 100, 1000000000)))
                       

	
