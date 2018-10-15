from lukh_fractions import LukhFraction


def test_0_plus_0():
    assert LukhFraction(0).plus(LukhFraction(0)).getNum() == 0


def test_0_plus_NonZero():
    assert LukhFraction(0).plus(LukhFraction(1)).getNum() == 1


def test_NonZero_plus_NonZero():
    assert LukhFraction(1).plus(LukhFraction(2)).getNum() == 3


def test_Zero_plus_Fraction():
    sum_result = LukhFraction(0).plus(LukhFraction(1, 2))
    assert (sum_result.getNum(), sum_result.getDen()) == (1, 2)


def test_adding_fractions_with_common_denominator_1():
    sum_result = LukhFraction(1, 3).plus(LukhFraction(1, 3))
    assert (sum_result.getNum(), sum_result.getDen()) == (2, 3)


def test_adding_fractions_with_common_denominator_2():
    sum_result = LukhFraction(1, 2).plus(LukhFraction(3, 2))
    assert (sum_result.getNum(), sum_result.getDen()) == (2, 1)


def test_adding_fractions_no_common_denominator1():
    sum_result = LukhFraction(1, 2).plus(LukhFraction(1, 3))
    assert (sum_result.getNum(), sum_result.getDen()) == (5, 6)


def test_adding_fractions_no_common_denominator2():
    sum_result = LukhFraction(1, 6).plus(LukhFraction(1, 4))
    assert (sum_result.getNum(), sum_result.getDen()) == (5, 12)


def test_reduce_fraction():
    f = LukhFraction(1701, 3768)
    assert (f.getNum(), f.getDen()) == (567, 1256)
