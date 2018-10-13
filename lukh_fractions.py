class LukhFraction:
    def __init__(self, num, den=1):
        self._num = num
        self._den = den

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
