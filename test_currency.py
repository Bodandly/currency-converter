from currency import *


USD_EUR = ("USD", "EUR", 0.74)

EUR_JPY = ("EUR", "JPY", 145.949)

def test_converter():
    assert convert(USD_EUR, 1, "USD", "EUR") == 0.74
    assert convert(USD_EUR, 1, "USD", "USD") == 1
    assert convert(USD_EUR, 1, "EUR", "USD") == 1.35
