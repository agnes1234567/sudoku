
from constants import NUMBER_OF_ROWS, NUMBER_OF_COLS
from z3 import *

class Sudoku_solver():
    def __init__(self):
        self.solver = Solver()
        
    def solve(self, grid):
        self.solver = Solver()
        
        for row in range(NUMBER_OF_ROWS):
            for col in range(NUMBER_OF_COLS):
                if grid[row][col] != 0:
                    var = Int('%s_%s' % (row, col))
                    self.solver.add(var == grid[row][col])
                else:
                    var = Int('%s_%s' % (row, col))
                    self.solver.add(var >= 1, var <= 9)
                    
        for row in range(NUMBER_OF_ROWS):
            for col in range(NUMBER_OF_COLS):
                var = Int('%s_%s' % (row, col))
                for i in range(NUMBER_OF_ROWS):
                    if i != col:
                        var2 = Int('%s_%s' % (row, i))
                        self.solver.add(var != var2)
                for i in range(NUMBER_OF_COLS):
                    if i != row:
                        var2 = Int('%s_%s' % (i, col))
                        self.solver.add(var != var2)
                for i in range(3):
                    for j in range(3):
                        if row // 3 * 3 + i != row and col // 3 * 3 + j != col:
                            var2 = Int('%s_%s' % (row // 3 * 3 + i, col // 3 * 3 + j))
                            self.solver.add(var != var2)
                            
                    
        res = self.solver.check()
        if res == sat:
            grid = [[0 for i in range(NUMBER_OF_COLS)] for j in range(NUMBER_OF_ROWS)]
            for row in range(NUMBER_OF_ROWS):
                for col in range(NUMBER_OF_COLS):
                    var = Int('%s_%s' % (row, col))
                    grid[row][col] = self.solver.model()[var].as_long()
            return grid
                    
        elif res == unsat:
            return None
            


    
        
        

        