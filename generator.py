import numpy as np
import random

def adder(arr, a, b):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i==0 and j==0):
                continue
            elif ((a+i < 0) or (b+j >= len(arr)) or (b+j < 0) or (a+i >= len(arr))):
                continue
            elif (arr[a + i][b + j] == -1):
                continue
            arr[a + i][b + j] += 1

class mine:
    def __init__(self, size, difficulty):
        self.diff = difficulty
        self.size = size
        self.state = np.zeros((size, size), dtype = 'i')
        # size -= 1
        while(difficulty!=0):
            place_x = random.randint(0, size - 1)
            place_y = random.randint(0, size - 1)
            while (self.state[place_x][place_y] == -1):
                place_x = random.randint(0, size - 1)
                place_y = random.randint(0, size - 1)
            # print (place_x)
            # print (place%size if (place%size != 0) else 4)
            self.state[place_x][place_y] = -1
            adder (self.state, place_x, place_y)
            difficulty -= 1

def main():
    test = mine(18, 40)
    print (test.state)

if __name__ == "__main__":
    main()
