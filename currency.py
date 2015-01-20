
rate_list =  [("USD", "EUR", 0.74), ("EUR", "JPY", 145.949)]


def convert(rates, value, begin, to):
    """Takes a rate, then gets the proper rate for the given currencies.
    If the values in the begin and to parameters are the same it will return
    the value. Otherwise it will decide if it can multiply the value by the
    given conversion rate, or it will multiply the value by one over the given
    conversion rate."""
    rate = rate_finder(rates, begin, to)
    if begin == to:
        return value
    elif rate.index(begin) == 1:
        return round(value * (1/round(rate[2],2)), 2)
    else:
        return round(value * round(rate[2],2), 2)


def rate_finder(rates, begin, to):
    """From the list of tuples finds the correct tuple to use, for
    conversion."""
    if begin == to:
        return None
    for entry in rates:
        if begin in entry and to in entry:
            return entry
