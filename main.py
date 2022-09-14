import random
import os
import sys
sys.setrecursionlimit(10**6)


class Sudoku:
    def __init__(self):
        self.grid = []
    

    def generate(self):
        input('start')
        self.grid = [[0 for i in range(9)] for j in range(9)]
        # Populate -1 -1, 0 0, and 1 1 box
        diagonal_box_pos = [(0,3), (3,6), (6,9)]
        for pos in diagonal_box_pos:
            random_numbers = self.generate_random_numbers(1, 9)
            for j in range(pos[0], pos[1]):
                for i in range(pos[0], pos[1]):
                    self.grid[i][j] = random_numbers.pop(0)
        
        self.populate_rest()
    
    
    def find_empty_space(self):
        for j, row in enumerate(self.grid):
            for i, col in enumerate(row):
                if col == 0:
                    return (i, j)

        return False


    def populate_rest(self):
        is_spot_available = self.find_empty_space()

        if not is_spot_available:
            return True
        
        j, i = is_spot_available

        for guess in range(1, 10):
            if self.is_unused_box(self.get_box_num(i, j), guess) and self.is_unused_horizontal(i, guess) and self.is_unused_vertical(j, guess):
                self.grid[i][j] = guess
                # os.system('cls')
                # self.show()
                if self.populate_rest():
                    return 
                self.grid[i][j] = 0
        
        return False

    def get_box_num(self, i, j):
        box = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
        for idx, b in enumerate(box):
            if i >= b[0] and i < b[0] + 3 and j >= b[1] and j < b[1] + 3:
                return idx
        return -1


    def is_unused_horizontal(self, j, n):
        return self.grid[j].count(n) == 0
    

    def is_unused_vertical(self, i, n):
        return [row[i] for row in self.grid].count(n) == 0
    

    def is_unused_box(self, b, n):
        box = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
        return [self.grid[j][i] for j in range(box[b][0], box[b][0] + 3) for i in range(box[b][1], box[b][1] + 3)].count(n) == 0


    def generate_random_numbers(self, first, last):
        numbers = [i for i in range(first, last + 1)]
        random.shuffle(numbers)
        return numbers


    def show(self):
        print('-------------------------------------')
        for j, row in enumerate(self.grid):
            for i, col in enumerate(row):
                print((' .  | ' if (i + 1) % 3 == 0 else ' . ' if i != 0 else '|  . ') if col == 0 else (f' {col}  | ' if (i + 1) % 3 == 0 else f' {col} ' if i != 0 else f'|  {col} '), end='')
            print()
            if (j + 1) % 3 == 0:
                print('-------------------------------------')
                
def main():
    game = Sudoku()
    game.generate()
    # game.populate_rest()
    # game.grid[0][4] = 1
    # game.grid[2][5] = 9
    # print(game.is_unused_box(0, 2))
    game.show()


if __name__ == '__main__':
    main()
