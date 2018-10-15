class LukhFraction:
    def __init__(self, num, den=1):
        gcd = find_gcd(*sorted([num, den]))
        self._num = num / gcd
        self._den = den / gcd

    def plus(self, other):
        if self._den == other.getDen():
            return LukhFraction(self._num + other.getNum(), self._den)
        else:
            res_num = self._num * other.getDen() + other.getNum() * self._den
            res_den = self._den * other.getDen()
            return LukhFraction(res_num, res_den)

    def getNum(self):
        return self._num

    def getDen(self):
        return self._den


def find_gcd(x1, x2):
    """
    Find Greatest Common Denominator
    x1, x2: integers
    x1 >= x2
    """
    if x1 == 1 or x2 == 1:
        return 1
    else:
        r = x1 % x2
        if r == 0:
            return x2
        else:
            return find_gcd(x2, r)
