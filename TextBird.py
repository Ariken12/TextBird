from random import *
import time


def draw(x, y, fly):
    global mp
    mp[y][x] = '.,.'
    if fly:
        mp[y][x+1] = '-'
        mp[y][x-1] = '-'
    else:
        mp[y][x+1] = '_'
        mp[y][x-1] = '_'


def clear():
    global  mp
    for i in range(len(mp)):
        for j in range(len(mp[i])):
            mp[i][j] = ' '


def show():
    global mp
    for i in mp:
        for j in i:
            print(j, end='')
        print()


x = 100
y = 5
bl = True
mp = []

for i in range(y):
    mp.append([])
    for j in range(x):
        mp[i].append('')



while True:
    clear()
    if bl == True:
        bl = False
        draw(randint(1, x-2), randint(1, y-2), True)
    else:
        bl = True
        draw(randint(1, x-2), randint(1, y-2), False)
    show()
    time.sleep(0)
