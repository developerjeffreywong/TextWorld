# MIT LICENSE
# Copyright (c) 2014 Jeffrey Wong (contact@jeffreywong.ca)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# TextWorld
# a text based action game
# student name: put your name here

import os # used for operating system commands and info
if os.name=='nt': # check if windows
    import msvcrt # used to get key press in windows
else:
    import getch # used to get the key press in mac/linux

# clear the screen
#https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console?
def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear') 

# get the key (cross platform solution)
# https://pypi.org/project/getch/    
def getKey():
    return (msvcrt.getch() if os.name=='nt' else getch.getch())

# size of the map
mapWidth=20
mapHeight=10

# player coordinates
# (0,0) is the top left corner
# y increases as you move down the map
# x increases as you move to the right of the map
playerX = 5
playerY = 5

# the keys
quitKey = "q"
upKey = 'w'
downKey='s'
leftKey='a'
rightKey='d'
keyPressed = ' ' # the key we pressed

# start the main loop
# keep playing till we press the quit key
while keyPressed != quitKey:
    # clear the screen
    clearScreen()

    # draw our map and player
    for line in range(0,mapHeight+1):
        for column in range(0, mapWidth+1):
            if line==playerY and column==playerX:
                print("X", end="", flush=True)
            else:
                print(" ", end="", flush=True)
        print() # start new line

    # get the new key press to move player    
    keyPressed = getKey()

    # decide what to do

    # up key is pressed, move player up
    if keyPressed == upKey:
        playerY = playerY - 1

    # down key is pressed, move player down
    elif keyPressed == downKey:
        playerY = playerY + 1
    

# player done playing
print("Thanks for playing!")
