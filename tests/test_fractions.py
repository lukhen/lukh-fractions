from lukh_fractions import LukhFraction


def test_0_plus_0():
    assert LukhFraction(0).plus(LukhFraction(0)).getInt() == 0


def test_0_plus_NonZero():
    assert LukhFraction(0).plus(LukhFraction(1)).getInt() == 1


def test_NonZero_plus_NonZero():
    assert LukhFraction(1).plus(LukhFraction(2)).getInt() == 3
