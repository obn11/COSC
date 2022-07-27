def queueingDelay (packetSize_bits, dataRate_bps, flagCurrentTransmission, numberInQueue):
    L = packetSize_bits
    R = dataRate_bps
    flag = flagCurrentTransmission
    N = numberInQueue
    if not flag:
        return 0
    return 0.5 * (L/R) + N * (L/R)


print(abs(queueingDelay(1000, 1000000, False, 0) - 0.0000) < 0.00001)




