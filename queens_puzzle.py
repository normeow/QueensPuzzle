import random
import numpy as np
class Puzzle:
    def __init__(self, n):
        #cooling rate, choose it wisely
        self._alpha = 0.7

        self._n = n
        self._round = 1
        self._temperature = 1000
        #queens are initially placed in random rows and columns such that each queen is in a different row and a different column
        self.res = [-1]*n
        for i in range(n):
            while(True):
                t = random.randint(0, n-1)
                if t not in self.res:
                    self.res[i] = t
                    break
        self.place_queens()

    def _is_under_attack(self, i):
        for j in range(self._n):
            if self.res[i] == self.res[j] or abs(self.res[i] - self.res[j] == abs(i - j)):
                return True
        return False

    def _number_of_attacked_queens(self):
        res = 0;
        for i in range(self._n):
            for j in range(i, self._n):
                if self.res[i] == self.res[j] or abs(self.res[i] - self.res[j] == abs(i-j)):
                    res +=1
        return res

    def _get_probability(self, delta):
        return np.exp(-delta/self._temperature)

    def place_queens(self):
        attacked_q = self._number_of_attacked_queens()



random.seed()
puzzle = Puzzle(8)
print(puzzle.place_queens())
