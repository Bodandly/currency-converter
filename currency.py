def convert(rates, value, begin, to):
    if rates.index(begin) == rates.index(to):
        return (1 * value)
    elif rates.index(begin) == 1:
        return round(value * (1/rates[2]), 2)
    else:
        return round(value * rates[2], 2)
