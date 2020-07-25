

class Dice:
    def __init__(self, eyes: [int]):
        self.__eyes = eyes

    @property
    def eyes(self):
        return self.__eyes

    def top(self):
        return self.__eyes[0]

    def right(self):    # pragma no cover
        return self.__eyes[2]

    def roll_s(self):
        tmp = copy.copy(self.__eyes)
        tmp[0] = self.__eyes[4]
        tmp[1] = self.__eyes[0]
        tmp[2] = self.__eyes[2]
        tmp[3] = self.__eyes[3]
        tmp[4] = self.__eyes[5]
        tmp[5] = self.__eyes[1]
        self.__eyes = tmp

    def roll_e(self):
        tmp = copy.copy(self.__eyes)
        tmp[0] = self.__eyes[3]
        tmp[1] = self.__eyes[1]
        tmp[2] = self.__eyes[0]
        tmp[3] = self.__eyes[5]
        tmp[4] = self.__eyes[4]
        tmp[5] = self.__eyes[2]
        self.__eyes = tmp

    def roll_n(self):   # pragma no cover
        tmp = copy.copy(self.__eyes)
        tmp[0] = self.__eyes[1]
        tmp[1] = self.__eyes[5]
        tmp[2] = self.__eyes[2]
        tmp[3] = self.__eyes[3]
        tmp[4] = self.__eyes[0]
        tmp[5] = self.__eyes[4]
        self.__eyes = tmp

    def roll_w(self):   # pragma no cover
        tmp = copy.copy(self.__eyes)
        tmp[0] = self.__eyes[2]
        tmp[1] = self.__eyes[1]
        tmp[2] = self.__eyes[5]
        tmp[3] = self.__eyes[0]
        tmp[4] = self.__eyes[4]
        tmp[5] = self.__eyes[3]
        self.__eyes = tmp

    def turn_right(self):
        tmp = copy.copy(self.__eyes)
        tmp[0] = self.__eyes[0]
        tmp[1] = self.__eyes[3]
        tmp[2] = self.__eyes[1]
        tmp[3] = self.__eyes[4]
        tmp[4] = self.__eyes[2]
        tmp[5] = self.__eyes[5]
        self.__eyes = tmp

    def adjust_top(self, top: int):
        for _ in range(4):
            if self.top() is top:
                break
            self.roll_e()
        for _ in range(4):
            if self.top() is top:
                break
            self.roll_s()

    def adjust_front(self, front: int):
        for _ in range(4):
            if self.front() is front:
                break
            self.turn_right()

    def front(self):
        return self.__eyes[1]

    def roll(self, direction: str):   # pragma no cover
        if direction.lower() == 'n':
            self.roll_n()
        if direction.lower() == 'e':
            self.roll_e()
        if direction.lower() == 's':
            self.roll_s()
        if direction.lower() == 'w':
            self.roll_w()

    def __eq__(self, other):
        if isinstance(other, Dice):
            return self.__eyes == other.eyes
        return False


def resolve():
    pass