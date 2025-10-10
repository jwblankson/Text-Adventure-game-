import random
import time
import os

import numpy as numpy
#Matrix size

size = int(input("What is the size of your board"))

one = np.full((size,size),'@')
two = np.full((size,size),'*')

Star density = [0.8. 0.6, 0.4, 0.3, 0.2, 0.1]

def generate_sky():
row = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))
    sky = np.full((row, col), ' ')
    
    for i in range(row):
        for j in range(col):
            if random.random() < random.choice(Star_density):
                sky[i][j] = '*'
    
    return sky
import numpy as np

def print_sky(sky):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in sky:
        print(' '.join(row))

def animate_moon():
    for step in range(COLS):
    clear_screen() 
    sky = generate_sky()
    print_sky(sky)
    moon_row = ROWS
    moon_col = step
    if moon_col < COLS:
        sky[moon_row][moon_col] = 'O'
        print_sky(sky)
    time.sleep(0.1)
ROWS = 20
COLS = 50
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')    
def generate_sky():
    sky = np.full((ROWS, COLS), ' ')
    for i in range(ROWS):
        for j in range(COLS):
            if random.random() < random.choice(Star_density):
                sky[i][j] = '*' 
    return sky
import numpy as np

animate_moon()
    for i in range(size):
        for j in range(size):   
            if sky[i][j] == '*':
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()


while True:    sky = generate_sky()
    print_sky(sky)  
    time.sleep(1)
    clear_screen()
    animate_moon()
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    print_array(one)
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    print_array(two)
    time.sleep(1)