def packetSwitching (numberRouters, messageSize_b, userDataSize_b,
                     overheadSize_b, processingTime_s, dataRate_bps,
                     propagationDelay_s):

    N  =  numberRouters
    M  =  messageSize_b
    S  =  userDataSize_b
    O  =  overheadSize_b
    P  =  processingTime_s
    R  =  dataRate_bps
    T  =  propagationDelay_s
    PT = (S+O) / R
    TR = PT * ((M/S) + N)
    total_T = T * (N+1)
    total_P = P * N
    total = total_T + total_P + TR
    return total

def IPToString (addr):
    byte1 = addr >> 24
    byte2 = (addr & 0xFF0000) >> 16
    byte3 = (addr & 0xFF00) >> 8
    byte4 = addr & 0xFF
    str = "{}.{}.{}.{}".format(byte1, byte2, byte3, byte4)
    return str

import math
def number_fdma_channels (b_hz, g_hz, u_hz):
     return (b_hz-g_hz) // (u_hz+g_hz)


def number_tdma_users (s_s, g_s, u_s):
    return int(s_s // (u_s + g_s))

def p_persistent_csma_collision_probability (p):
    r = (1-p)**2
    return (p ** 2) / (1 - r)

print ("{:.3f}".format(p_persistent_csma_collision_probability(0.2)))