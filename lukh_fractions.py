class LukhFraction:
    def __init__(self, num, den=1):
        self._num = num
        self._den = den

    def plus(self, other):
        return LukhFraction(self._num + other._num, other.getDen())

    def getNum(self):
        return self._num

    def getDen(self):
        return self._den
