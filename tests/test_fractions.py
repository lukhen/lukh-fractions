from lukh_fractions import LukhFraction


def test_0_plus_0():
    assert LukhFraction(0).plus(LukhFraction(0)).getInt() == 0
