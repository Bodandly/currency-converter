from currency import *


rate_list =  [("USD", "EUR", 0.74), ("EUR", "JPY", 145.949)]

def test_converter():
    assert convert(rate_list, 1, "USD", "EUR") == 0.74
    assert convert(rate_list, 1, "USD", "USD") == 1
    assert convert(rate_list, 1, "EUR", "USD") == 1.35
    assert convert(rate_list, 1, "EUR", "JPY") == 145.95
    # assert convert(rate_list, 1)

def test_rate_finder():
    assert rate_finder(rate_list, "USD", "USD") == False
    assert rate_finder(rate_list, "USD", "EUR") == ("USD", "EUR", 0.74)
