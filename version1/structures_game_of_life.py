from conways_game_of_life import *

def create_something_cool():
    grid = create_empty_grid(42, 150)
    grid[22][75] = 1
    grid[24][74] = 1
    grid[21][75] = 1
    grid[23][77] = 1
    grid[22][73] = 1
    grid[22][74] = 1
    grid[24][76] = 1
    return grid

def give_me_a_gun():
    grid = create_empty_grid(42, 150)
    grid[8][1] = 1
    grid[8][2] = 1
    grid[9][1] = 1
    grid[9][2] = 1
    grid[7][12] = 1
    grid[8][12] = 1
    grid[9][12] = 1
    grid[6][13] = 1
    grid[10][13] = 1
    grid[5][14] = 1
    grid[11][14] = 1
    grid[6][15] = 1
    grid[10][15] = 1
    grid[7][16] = 1
    grid[8][16] = 1
    grid[9][16] = 1
    grid[7][17] = 1
    grid[8][17] = 1
    grid[9][17] = 1
    grid[5][22] = 1
    grid[6][22] = 1
    grid[7][22] = 1
    grid[4][23] = 1
    grid[5][23] = 1
    grid[7][23] = 1
    grid[8][23] = 1
    grid[4][24] = 1
    grid[5][24] = 1
    grid[7][24] = 1
    grid[8][24] = 1
    grid[4][25] = 1
    grid[5][25] = 1
    grid[6][25] = 1
    grid[7][25] = 1
    grid[8][25] = 1
    grid[3][26] = 1
    grid[4][26] = 1
    grid[8][26] = 1
    grid[9][26] = 1
    grid[4][31] = 1
    grid[5][31] = 1
    grid[6][35] = 1
    grid[7][35] = 1
    grid[6][36] = 1
    grid[7][36] = 1
    return grid

def create_horizontal_spaceship():
    grid = create_empty_grid(42, 100)
    grid[23][1] = 1
    grid[24][1] = 1
    grid[22][2] = 1
    grid[23][2] = 1
    grid[24][2] = 1
    grid[22][3] = 1
    grid[23][3] = 1
    grid[24][3] = 1
    grid[22][4] = 1
    grid[23][4] = 1
    grid[24][4] = 1
    grid[22][5] = 1
    grid[23][5] = 1
    grid[25][5] = 1
    grid[23][6] = 1
    grid[24][6] = 1
    grid[25][6] = 1
    grid[24][7] = 1
    return grid

def create_diagonal_spaceship():
    grid = create_empty_grid(42, 100)
    grid[6][1] = 1
    grid[8][1] = 1
    grid[7][2] = 1
    grid[8][2] = 1
    grid[7][3] = 1
    return grid



if __name__ == '__main__':
    '''simulate_life_fast_version(give_me_a_gun(), 200)
    simulate_life_slow_version(create_horizontal_spaceship(), 64)
    simulate_life_slow_version(create_diagonal_spaceship(), 50)'''
