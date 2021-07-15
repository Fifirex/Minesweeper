import generator as gen
import sys

def cover(arr, size, click):
    newArr = [ [0 for _ in range(gen.MAX_SIZE) ] for _ in range(gen.MAX_SIZE)]
    click_x, click_y = click
    # print (size)
    for i in range (size):
        for j in range (size):
            newArr[i][j] = "X"
    flag = 1
    while (flag == 1):
        flag = 0
        a = 3
        row_limit = size
        if(row_limit > 0):
            column_limit = size
        j = max(0, click_y - a)
        for i in range (max(0, click_x - a) + 1, min(click_x + a, row_limit - 1)): # upper limb
            if (arr[i][j] == 0):
                flag = 1
                newArr[i][j] = 0
            elif (arr[i][j] != -1 and arr[i+1][j] == 0):
                newArr[i][j] = arr[i][j]
        j = min(click_y + a, column_limit - 1)
        for i in range (max(0, click_x - a) + 1, min(click_x + a, row_limit - 1)): # lower limb
            if (arr[i][j] == 0):
                flag = 1
                newArr[i][j] = 0
            elif (arr[i][j] != -1 and arr[i-1][j] == 0):
                newArr[i][j] = arr[i][j]
        i = max(0, click_x - a)
        for j in range (max(0, click_y - a) + 1, min(click_y + a, column_limit - 1)): # left limb
            if (arr[i][j] == 0):
                flag = 1
                newArr[i][j] = 0
            elif (arr[i][j] != -1 and arr[i][j+1] == 0):
                newArr[i][j] = arr[i][j]
        i = min(click_x + a, row_limit - 1)
        for j in range (max(0, click_y - a) + 1, min(click_y + a, column_limit - 1)): # right limb
            if (arr[i][j] == 0):
                flag = 1
                newArr[i][j] = 0
            elif (arr[i][j] != -1 and arr[i][j-1] == 0):
                newArr[i][j] = arr[i][j]

    return newArr

def main():
    size = int(input(" Enter the size : "))
    diff = int(input(" Enter the difficulty : "))
    str = input(" Enter the seed : ")
    seed = str.split()
    for i in range (len(seed)):
        seed [i] = int(seed[i])
    initArr = gen.mine (size, diff, seed)
    showArr = cover (initArr.state, size, seed)
    if (initArr.exist == False):
        sys.exit("err")
    print (showArr)

if __name__ == "__main__":
    main()