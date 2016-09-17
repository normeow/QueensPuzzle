import random
import numpy as np

class Puzzle:
    def __init__(self, n):
        #cooling rate, choose it wisely
        self._alpha = 0.98

        self._n = n
        self._round = 1
        self._temperature = 1000
        #self.res = [i for i in range(n)]

        # queens are initially placed in random rows and columns such that each queen is in a different row and a different column
        self.res = [-1] * n
        for i in range(n):
            while (True):
                t = random.randint(0, n - 1)
                if t not in self.res:
                    self.res[i] = t
                    break
        random.seed()

    def _is_under_attack(self, i):
        for j in range(self._n):
            if (i != j) and (self.res[i] == self.res[j] or abs(self.res[i] - self.res[j]) == j - i):
                return True
        return False

    def _number_of_beats(self):
        res = 0;
        for i in range(self._n):
            for j in range(i + 1, self._n):
                if self.res[i] == self.res[j] or abs(self.res[i] - self.res[j]) == j-i:
                    res +=1
        return res

    def _get_probability(self, delta):
        return np.exp(-delta/self._temperature)

    def place_queens(self):
        beats = self._number_of_beats()
        eps = 0.00000001
        while (beats != 0 and self._temperature > eps):
            for i in range(self._n):
                self._round += 1;
                self._temperature *= self._alpha
                if self._is_under_attack(i):
                    prev_pos = self.res[i]
                    t = random.randint(0, self._n - 1)
                    self.res[i] = t
                    new_beats = self._number_of_beats()
                    delta = new_beats - beats
                    if delta < 0:
                        beats = new_beats
                    else:
                        # probabilities go on
                        rnd_value = random.random()
                        if rnd_value > self._get_probability(delta):
                            self.res[i] = prev_pos
                        else:
                            beats = self._number_of_beats()

        print("rounds:", self._round)
        print("beats:", beats)
        return(self.res)

puzzle = Puzzle(8)
print(puzzle.place_queens())
