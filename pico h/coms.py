import time
from ibus import IBus

ibus_in = IBus(1)


def coms_data():
    res = ibus_in.read()
    # if signal then display immediately
    if (res[0] == 1):
            data=[res[0],IBus.normalize(res[1]),IBus.normalize(res[2]),IBus.normalize(res[3]),IBus.normalize(res[4]),IBus.normalize(res[5], type="dial"),IBus.normalize(res[6], type="dial")]
            return(data)
