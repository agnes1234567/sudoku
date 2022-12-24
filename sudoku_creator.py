from sudoku_solver import Sudoku_solver
import pygame 
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, FONT
from random import randint, shuffle

class Sudoku_creator:
    def __init__(self):
        self.solver = Sudoku_solver()
        
        
    def create(self):
        res = None 
        while not res:
            self.grid = [[0 for i in range(9)] for j in range(9)]
            self.set_one_subgrid()
            res = self.solver.solve(self.grid)
            
        self.grid = res
        self.remove_numbers()
        
    def remove_numbers(self):
        for i in range(9):
            for j in range(9):
                if randint(0, 1):
                    self.grid[i][j] = 0
    
    def set_one_subgrid(self):
        values = [i for i in range(1, 10)]
        shuffle(values)
        for i in range(3):
            for j in range(3):
                val = values.pop()
                self.grid[i][j] = val

        
        