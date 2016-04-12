from functools import lru_cache


@lru_cache(maxsize=128)
def row(pos, bits=0):
    bits -= 1
    if bits <= 0:
        rpt = 2**pos // 2
        return "0" * rpt + "1" * rpt
    else:
        r = row(pos, bits) 
        return r + r[::-1]

def graycode(size: int):
    size += 1
    rows = [row(x, size - x) for x in range(1, size)]

    return ("".join(entry) for entry in zip(*rows[::-1]))
