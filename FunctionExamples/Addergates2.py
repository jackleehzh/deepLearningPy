# coding: utf-8
import numpy as np

class Gates():
    def __init__(self, x1, x2):
        self.b = -3
        self.electric = np.array([x1, x2])
        self.ws = np.array([2, 2])
        self.result = np.sum(self.electric * self.ws) + self.b

    def AND(self):
        if self.result <= 0:
            return 0
        else:
            return 1

    def OR(self):
        if self.result <= -3:
            return 0
        else:
            return 1

    def NAND(self):
        if self.result <= 0:
            return 1
        else:
            return 0

    def XOR(self):
        self.electric = np.array([self.OR(), self.NAND()])
        self.result = np.sum(self.electric * self.ws) + self.b
        return self.AND()

if __name__ == '__main__':
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        gate = Gates(xs[0], xs[1])
        print("AND:" + str(xs) + " -> " + str(gate.AND()))
        print("OR:" + str(xs) + " -> " + str(gate.OR()))
        print("NAND:" + str(xs) + " -> " + str(gate.NAND()))
        print("XOR:" + str(xs) + " -> " + str(gate.XOR()))
