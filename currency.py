def convert(rates, value, begin, to):
    if rates.index(begin) == rates.index(to):
        return (1 * value)
    elif rates.index(begin) == 1:
        return value * (1/rates[2])
    else:
        return value * rates[2]
