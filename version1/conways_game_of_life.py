'''Exercice supplémentaire de la 6e série de TP sur le Jeu de la Vie de Conway.
NB : on suppose ici que grid n'est pas une matrice 1x1, ni une matrice vide'''

import time
import random

def next_state(grid, i, j):
    n = len(grid)
    m = len(grid[0])
    sum_square = 0 #somme des éléments autour de grid[i][j] (celui-ci inclus)
    if i == 0: #bord supérieur de grid
        if j == 0: #coin supérieur gauche de grid
            sum_square = grid[i][j] + grid[i][j+1] + grid[i+1][j] + grid[i+1][j+1]
        elif  j == m-1: #coin supérieur droit de grid
            sum_square = grid[i][j-1] + grid[i][j] + grid[i+1][j-1] + grid[i+1][j]
        else:
            for line in range(i, (i+1)+1):
                for column in range(j-1, (j+1)+1):
                    sum_square += grid[line][column]
    elif i == n-1: #bord inférieur de grid
        if j == 0: #coin inférieur gauche de grid
            sum_square = grid[i-1][j] + grid[i-1][j+1] + grid[i][j] + grid[i][j+1]
        elif j == m-1: #coin inférieur droit de grid
            sum_square = grid[i-1][j-1] + grid[i-1][j] + grid[i][j-1] + grid[i][j]
        else:
            for line in range(i-1, (i)+1):
                for column in range(j-1, (j+1)+1):
                    sum_square += grid[line][column]
    elif j == 0: #bord gauche de grid
        for line in range(i-1, (i+1)+1):
            for column in range(j, (j+1)+1):
                sum_square += grid[line][column]
    elif j == m-1: #bord droit de grid
        for line in range(i-1, (i+1)+1):
            for column in range(j-1, (j)+1):
                sum_square += grid[line][column]
    else:
        for line in range(i-1, (i+1)+1):
            for column in range(j-1, (j+1)+1):
                sum_square += grid[line][column]
    if grid[i][j] == 0:
        return sum_square == 3
    else: #elif grid[i][j]==1
        return sum_square == 2+1 or sum_square == 3+1 #'+1' car on a compté grid[i][j] dans sum_square




def next_grid(grid):
    new_grid = []
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        current_line = []
        for j in range(m):
            if next_state(grid, i, j):
                current_line.append(1)
            else:
                current_line.append(0)
        new_grid.append(current_line)
    return new_grid




def display_grid(grid):
    n = len(grid)
    m = len(grid[0])
    for line in range(n):
        for column in range(m):
            if grid[line][column] == 1:
                print('█', end='')
            else: #elif grid[line][column] == 0
                print(' ', end='')
        print('')

def simulate_life_slow_version(grid, t):
    if t == 0:
        print('Dernière itération !')
        display_grid(grid)
    else:
        print('Il reste : ', t, ' itérations.')
        display_grid(grid)
        input()
        simulate_life_slow_version(next_grid(grid), t-1)

    #supplément personnel

def simulate_life_fast_version(grid, t, speed = 0.2):
    print('Il reste ', t, 'tours')
    if t == 0:
        display_grid(grid)
    else:
        display_grid(grid)
        time.sleep(speed)
        simulate_life_fast_version(next_grid(grid), t-1, speed)


def create_empty_grid(n, m):
    grid = []
    for i in range(n):
        line = []
        for j in range(m):
            line.append(0)
        grid.append(line)
    return grid

def create_random_grid(n, m):
    grid = []
    for i in range(n):
        line = []
        for j in range(m):
            x = random.randint(0, 1)
            line.append(x)
        grid.append(line)
    return grid





if __name__ == '__main__':
    '''my_grid = [[1, 0, 1, 0, 1],[1, 1, 1, 1, 0],[0, 0, 0, 1, 0],[1, 1, 0, 0, 1],[1, 0, 0, 1, 0]]
    simulate_life(my_grid, 10)'''
    '''test_grid = [[0,0,0],[1,1,1],[0,0,1]]
    print(test_grid)
    display_grid(test_grid)
    print(next_grid(test_grid))
    display_grid(next_grid(test_grid))
    big_grid = create_empty_grid(40, 150)
    display_grid(big_grid)
    input()
    big_grid = create_empty_grid(40, 150)
    big_grid[24][75] = 1
    big_grid[26][74] = 1
    big_grid[23][75] = 1
    big_grid[25][77] = 1
    big_grid[24][73] = 1
    big_grid[24][74] = 1
    big_grid[26][76] = 1

    simulate_life_slow_version(big_grid, 42)
    my_simulator(big_grid)'''
