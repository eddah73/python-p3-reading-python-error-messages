#!/usr/bin/env python3

# assert(1 != 2)
try:
    assert(1 == 2)

except AssertionError:
    print("Assertion Error raised as expected.")

