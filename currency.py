
rate_list =  [("USD", "EUR", 0.74), ("EUR", "JPY", 145.949)]

def convert(rates, value, begin, to):
    rate = rate_finder(rates, begin, to)
    if rate == False:
        return (1 * value)
    elif rate.index(begin) == 1:
        return round(value * (1/rate[2]), 2)
    else:
        return round(value * rate[2], 2)

def rate_finder(rates, begin, to):
    if begin == to:
        return False
    for entry in rates:
        if begin in entry and to in entry:
            return entry
