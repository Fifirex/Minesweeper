import numpy as np
import random

MAX_SIZE = 25

class mine:

    def __init__(self, size, difficulty, seed):
        if (size < 5 or size > MAX_SIZE):
            self.exist = False
        elif (difficulty < 0 or difficulty > size**2):
            self.exist = False
        else:
            self.exist = True
            self.diff = difficulty
            self.size = size
            self.state = np.zeros((size, size), dtype = 'i')
            seed_x, seed_y = seed
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if ((seed_x+i < 0) or (seed_y+j >= self.size) or (seed_y+j < 0) or (seed_x+i >= self.size)):
                        continue
                    self.state[seed_x + i][seed_y + j] = -2
            while(difficulty!=0):
                place_x = random.randint(0, size - 1)
                place_y = random.randint(0, size - 1)
                while (self.state[place_x][place_y] == -1 or self.state[place_x][place_y] == -2):
                    place_x = random.randint(0, size - 1)
                    place_y = random.randint(0, size - 1)
                self.state[place_x][place_y] = -1
                self.adder (place_x, place_y)
                difficulty -= 1
            # final -2 compensation
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if ((seed_x+i < 0) or (seed_y+j >= self.size) or (seed_y+j < 0) or (seed_x+i >= self.size)):
                        continue
                    self.state[seed_x + i][seed_y + j] += 2

            self.state[seed_x][seed_y] = -2

    def adder(self, a, b):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i==0 and j==0):
                    continue
                elif ((a+i < 0) or (b+j >= self.size) or (b+j < 0) or (a+i >= self.size)):
                    continue
                elif (self.state[a + i][b + j] == -1):
                    continue
                self.state[a + i][b + j] += 1

# method of shifting 0 clusters can be tried