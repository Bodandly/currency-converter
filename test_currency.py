from currency import *


rate_list =  [("USD", "EUR", 2.003), ("EUR", "JPY", 300.00)]


def test_converter():
    assert convert(rate_list, 1, "USD", "EUR") == 2.00
    assert convert(rate_list, 1, "USD", "USD") == 1.00
    assert convert(rate_list, 1, "EUR", "USD") == 0.50
    assert convert(rate_list, 1, "EUR", "JPY") == 300.00
    assert convert(rate_list, 1, "JPY", "EUR") == 0.00
    assert convert(rate_list, 1, "JPY", "JPY") == 1


def test_rate_finder():
    assert rate_finder(rate_list, "USD", "EUR") == ("USD", "EUR", 2.003)
    assert rate_finder(rate_list, "EUR", "USD") == ("USD", "EUR", 2.003)
    assert rate_finder(rate_list, "JPY", "EUR") == ("EUR", "JPY", 300.00)
