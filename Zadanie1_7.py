with open("signals.bin", "rb") as f:
    by = f.read()
    signals = {2:[0], 4:[0], 7:[0]}
    flags = {2:by[2] & 2**2 != 0, 4:by[2] & 2**4 != 0, 7:by[2] & 2**7 != 0}
    for i in range(0,len(by),3):
        for s in signals:
            if bool(by[i+2] & 2**s) != flags[s]:
                signals[s] += [int.from_bytes(by[i:i+2], "big") - sum(signals[s])] 
                flags[s] = not flags[s]
    count = iter(range(1,4))
    for s in signals:
        if len(signals[s]) % 2 != 0: signals[s]  = signals[s][0:len(signals[s])-1]
        signals[s] = round((sum(signals[s][2::2])  + sum(signals[s][3::2]))  /(len(signals[s][2:])/2))
        print(f"Частота сигнала {next(count)}: {1/signals[s] * 1000:.0f} Hz")
