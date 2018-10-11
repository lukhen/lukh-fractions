class LukhFraction:
    def __init__(self, num):
        self._num = num

    def plus(self, other):
        return LukhFraction(self._num + other._num)

    def getInt(self):
        return self._num
