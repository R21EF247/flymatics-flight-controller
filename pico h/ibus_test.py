import time
from ibus import IBus

ibus_in = IBus(1)


while True:
    res = ibus_in.read()
    # if signal then display immediately
    if (res[0] == 1):
        print ("{} {} {} {} {} {} {}".format(
            res[0],    # Status
            IBus.normalize(res[1]),
            IBus.normalize(res[2]),
            IBus.normalize(res[3]),
            IBus.normalize(res[4]),
            IBus.normalize(res[5], type="dial"),
            IBus.normalize(res[6], type="dial")),
            end="")
        print (" - {}".format(time.ticks_ms()))
    else:
        time.sleep(0.1)